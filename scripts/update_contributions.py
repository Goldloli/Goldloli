#!/usr/bin/env python3
"""Refresh the open-source contribution table in README.md.

Data source: GitHub REST API — merged pull requests authored by GH_LOGIN,
plus the star count of each upstream repository.
Output: rewrites the block between the contributions markers in README.md.
Standard library only — runs on the ubuntu-latest runner as-is.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request

API = "https://api.github.com"
LOGIN = os.environ.get("GH_LOGIN", "Goldloli")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
README = os.environ.get("README_PATH", "README.md")
START_MARK = "<!-- contributions:start -->"
END_MARK = "<!-- contributions:end -->"
MAX_ROWS = 12


def api(url: str) -> dict | list:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_merged_prs() -> list[dict]:
    prs: list[dict] = []
    page = 1
    while page <= 10:
        url = (
            f"{API}/search/issues?q=is:pr+is:merged+author:{LOGIN}"
            f"&per_page=100&page={page}&sort=updated"
        )
        items = api(url).get("items", [])
        prs.extend(items)
        if len(items) < 100:
            break
        page += 1
    return prs


def human_stars(n: int) -> str:
    if n >= 1000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


def build_block(prs: list[dict]) -> str:
    grouped: dict[str, int] = {}
    for pr in prs:
        repo = pr["repository_url"].split("/repos/", 1)[-1]
        if repo.lower().startswith(LOGIN.lower() + "/"):
            continue  # only contributions to other people's repositories
        grouped[repo] = grouped.get(repo, 0) + 1

    if not grouped:
        return f"{START_MARK}\n_暂无统计到的上游贡献，稍后自动更新。_\n{END_MARK}"

    rows = []
    for repo, count in grouped.items():
        try:
            stars = int(api(f"{API}/repos/{repo}").get("stargazers_count") or 0)
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError):
            stars = 0
        rows.append({"repo": repo, "stars": stars, "n": count})

    rows.sort(key=lambda r: (-r["stars"], r["repo"].lower()))
    hidden = max(0, len(rows) - MAX_ROWS)
    shown = rows[:MAX_ROWS]

    total_merged = sum(r["n"] for r in rows)
    total_stars = sum(r["stars"] for r in rows)

    lines = [
        START_MARK,
        f"**{total_merged}** 个已合并 PR · **{len(rows)}** 个上游项目 · "
        f"合计 **{human_stars(total_stars)}** stars",
        "",
        "| 项目 | Stars |",
        "| --- | ---: |",
    ]
    for r in shown:
        lines.append(
            f"| [{r['repo']}](https://github.com/{r['repo']}) | {human_stars(r['stars'])} |"
        )
    if hidden:
        lines.append("")
        lines.append(f"<sub>另有 {hidden} 个贡献较少的项目未列出。</sub>")
    lines.append(END_MARK)
    return "\n".join(lines)


def main() -> int:
    with open(README, encoding="utf-8") as fh:
        text = fh.read()
    if START_MARK not in text or END_MARK not in text:
        print(f"markers not found in {README}", file=sys.stderr)
        return 1

    block = build_block(fetch_merged_prs())
    pattern = re.compile(
        re.escape(START_MARK) + r".*?" + re.escape(END_MARK), re.DOTALL
    )
    new_text = pattern.sub(lambda _: block, text, count=1)

    if new_text == text:
        print("contributions up to date")
        return 0
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(new_text)
    print("contributions updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
