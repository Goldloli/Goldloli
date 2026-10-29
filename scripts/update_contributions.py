#!/usr/bin/env python3
"""Refresh the open-source contribution table in README.md.

Data source: GitHub REST API (merged PRs authored by GH_LOGIN + repository stars).
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
from datetime import datetime, timezone

API = "https://api.github.com"
LOGIN = os.environ.get("GH_LOGIN", "Goldloli")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
README = os.environ.get("README_PATH", "README.md")
START_MARK = "<!-- contributions:start -->"
END_MARK = "<!-- contributions:end -->"
MAX_PRS_PER_REPO = 2
MAX_ROWS = 12


def api(url: str) -> dict | list:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_prs() -> list[dict]:
    """All pull requests authored by the user (merged and still in review)."""
    prs: list[dict] = []
    page = 1
    while page <= 10:
        url = (
            f"{API}/search/issues?q=is:pr+author:{LOGIN}"
            f"&per_page=100&page={page}&sort=updated"
        )
        data = api(url)
        items = data.get("items", [])
        prs.extend(items)
        if len(items) < 100:
            break
        page += 1
    return prs


def repo_of(pr: dict) -> str:
    return pr["repository_url"].split("/repos/", 1)[-1]


def human_stars(n: int) -> str:
    if n >= 1000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


def short_title(title: str, limit: int = 46) -> str:
    title = " ".join(title.split())
    return title if len(title) <= limit else title[: limit - 1].rstrip() + "…"


def build_block(prs: list[dict]) -> str:
    # only contributions to repositories the user does not own
    grouped: dict[str, list[dict]] = {}
    for pr in prs:
        repo = repo_of(pr)
        if repo.lower().startswith(LOGIN.lower() + "/"):
            continue
        merged = bool(pr.get("pull_request", {}).get("merged_at"))
        if not merged and pr.get("state") != "open":
            continue  # closed without merge is not a contribution
        grouped.setdefault(repo, []).append(pr)

    if not grouped:
        return (
            f"{START_MARK}\n"
            "_暂无统计到的上游贡献，稍后自动更新。_\n"
            f"{END_MARK}"
        )

    rows = []
    for repo, items in grouped.items():
        try:
            meta = api(f"{API}/repos/{repo}")
            stars = int(meta.get("stargazers_count") or 0)
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError):
            stars = 0
        items.sort(
            key=lambda p: (
                bool(p.get("pull_request", {}).get("merged_at")),
                p.get("closed_at") or p.get("created_at") or "",
            ),
            reverse=True,
        )
        links, states = [], []
        for pr in items[:MAX_PRS_PER_REPO]:
            merged = bool(pr.get("pull_request", {}).get("merged_at"))
            links.append(
                f"[#{pr['number']}]({pr['html_url']}) {short_title(pr['title'])}"
            )
            states.append("已合并" if merged else "审核中")
        if len(items) > MAX_PRS_PER_REPO:
            links.append(f"等 {len(items)} 个 PR")
            states.append("…")
        rows.append(
            {
                "repo": repo,
                "stars": stars,
                "merged": sum(1 for p in items if p.get("pull_request", {}).get("merged_at")),
                "open": sum(1 for p in items if not p.get("pull_request", {}).get("merged_at")),
                "cell": "<br>".join(links),
                "state": "<br>".join(states),
            }
        )

    rows.sort(key=lambda r: (-r["stars"], r["repo"].lower()))
    hidden = max(0, len(rows) - MAX_ROWS)
    rows = rows[:MAX_ROWS]

    total_merged = sum(r["merged"] for r in rows)
    total_open = sum(r["open"] for r in rows)
    total_stars = sum(r["stars"] for r in rows)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    summary = [f"**{total_merged}** 个已合并 PR"]
    if total_open:
        summary.append(f"**{total_open}** 个审核中")
    summary.append(f"**{len(rows) + hidden}** 个上游项目")
    summary.append(f"合计 **{human_stars(total_stars)}** stars")

    lines = [
        START_MARK,
        " · ".join(summary),
        "",
        "| 项目 | Stars | 状态 | 我的贡献 |",
        "| --- | ---: | :---: | --- |",
    ]
    for r in rows:
        lines.append(
            f"| [{r['repo']}](https://github.com/{r['repo']}) | "
            f"{human_stars(r['stars'])} | {r['state']} | {r['cell']} |"
        )
    if hidden:
        lines.append("")
        lines.append(f"<sub>另有 {hidden} 个贡献较少的项目未列出。</sub>")
    lines.append("")
    lines.append(f"<sub>数据自动更新于 {stamp}（UTC）</sub>")
    lines.append(END_MARK)
    return "\n".join(lines)


def main() -> int:
    with open(README, encoding="utf-8") as fh:
        text = fh.read()
    if START_MARK not in text or END_MARK not in text:
        print(f"markers not found in {README}", file=sys.stderr)
        return 1

    block = build_block(fetch_prs())
    pattern = re.compile(
        re.escape(START_MARK) + r".*?" + re.escape(END_MARK), re.DOTALL
    )
    new_text = pattern.sub(block.replace("\\", r"\\"), text, count=1)

    if new_text == text:
        print("contributions up to date")
        return 0
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(new_text)
    print("contributions updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
