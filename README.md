<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/banner-light.svg">
    <img src="./assets/banner-light.svg" alt="Goldloli · 小卡塔克 — 本地优先的 AI 工具" width="100%">
  </picture>
</p>

<p align="center">
  <b>把大模型塞进本地设备里。</b><br>
  <i>Putting large models onto local devices.</i><br>
  <sub>本地优先的 AI 工具作者 · 开源项目 PR 贡献者（翻译与本地化 / AI 工具链 / 基础设施）<br>
  Local-first AI tooling author · PR contributor across open-source repos (translation &amp; localization · AI tooling · infra)</sub>
</p>

## 开源仓库 · Open Source Repositories

几个自己维护的仓库，都还在慢慢做，欢迎试用和提 issue · *Repos I maintain — still evolving, issues welcome:*

- **[ASRbox](https://github.com/Goldloli/asrbox)** — 音视频转写与 AI 字幕工作台，支持 25 个本地 ASR 模型，macOS / Windows / Docker 都能跑。
  <i>Audio/video transcription and AI-subtitle workbench with 25 local ASR models — runs on macOS, Windows, and Docker.</i>
- **[bilidown](https://github.com/Goldloli/bilidown)** — B 站视频、番剧、课程和音频下载工具，提供 macOS 与 Windows 桌面客户端。
  <i>Bilibili videos, anime, courses, and audio downloader, with macOS and Windows desktop clients.</i>
- **[image-studio](https://github.com/Goldloli/image-studio)** — 本地优先的 AI 图像工作台：文生图、按指令改图、去背景和 4 倍放大，提供 macOS 与 Windows 桌面客户端。
  <i>Local-first AI image workbench — text-to-image, instruction-based editing, background removal, and 4× upscaling, with desktop clients.</i>
- **[XiaoSeek LX04](https://github.com/Goldloli/xiaoai-deepseek-lx04)** — 在小爱触屏音箱上接入 DeepSeek 的成功尝试，老设备 AI 时代起死回生，保留了原生语音和米家控制。
  <i>DeepSeek on the Xiaoai touchscreen speaker — an old device revived for the AI era, with native voice and Mijia control intact.</i>
- **[vid2note](https://github.com/Goldloli/vid2note)** — 把视频转成 Markdown 笔记和思维导图的工具。
  <i>Turns videos into Markdown notes and mind maps.</i>
- **[ai-sdd-bootstrap](https://github.com/Goldloli/ai-sdd-bootstrap)** — 给 AI 辅助开发用的分阶段脚手架，以前有用，现在模型能力强了没啥用。
  <i>Staged scaffolding for AI-assisted development — useful once, less needed as models got stronger.</i>

## 开源贡献 · Contributing

- **[Dailin521/codex-provider-sync](https://github.com/Dailin521/codex-provider-sync)** [![GitHub stars](https://img.shields.io/github/stars/Dailin521/codex-provider-sync?style=flat&color=gold)](https://github.com/Dailin521/codex-provider-sync) — 新增 macOS Avalonia 桌面端 GUI：在 Codex 里切换模型接入不再丢失会话记录——我的第一个 PR。 *macOS Avalonia desktop GUI, so switching model providers in Codex no longer loses your chat history — my first PR.*
- **[collabora/WhisperLive](https://github.com/collabora/WhisperLive)** [![GitHub stars](https://img.shields.io/github/stars/collabora/WhisperLive?style=flat&color=gold)](https://github.com/collabora/WhisperLive) — 实时音频流水的会话内重置：reset 标志与在途转写的竞态、锁内帧缓冲换入、TensorRT 后端对齐（三轮维护者 review 修出真实死锁）。 *Race-free in-session transcript reset for live streaming — buffered frame swap under lock, ack propagation, and TensorRT backend parity.*
- **[kornia/kornia](https://github.com/kornia/kornia)** [![GitHub stars](https://img.shields.io/github/stars/kornia/kornia?style=flat&color=gold)](https://github.com/kornia/kornia) — LightGlue 匹配的张量维度修复：(1, N, D) 描述子不再被早退条件误判而静默返回 0 匹配。 *LightGlue matcher dimension fix — (1, N, D) descriptors no longer hit the early-exit check and silently return zero matches.*
- **[microsoft/PyRIT](https://github.com/microsoft/PyRIT)** [![GitHub stars](https://img.shields.io/github/stars/microsoft/PyRIT?style=flat&color=gold)](https://github.com/microsoft/PyRIT) — Converter 身份哈希纳入有序参数，消除同参数量转换器的静默注册冲突。 *Converter identity hashing now includes ordered parameters, fixing silent registration collisions between same-arity converters.*
- **[version-fox/vfox](https://github.com/version-fox/vfox)** [![GitHub stars](https://img.shields.io/github/stars/version-fox/vfox?style=flat&color=gold)](https://github.com/version-fox/vfox) — 五条下载路径统一加固：任何非 200 状态即失败并报状态、URL 凭证脱敏、插件文件名 Windows 反斜杠安全。 *Hardened five download paths to fail on any non-200 status with the reason, redacted URL credentials, and Windows-safe plugin file names.*
- **[DefectDojo/django-DefectDojo](https://github.com/DefectDojo/django-DefectDojo)** [![GitHub stars](https://img.shields.io/github/stars/DefectDojo/django-DefectDojo?style=flat&color=gold)](https://github.com/DefectDojo/django-DefectDojo) — Qualys 扫描解析器健壮性：缺词条 QID 的 finding 跳过并告警，不再让整份报告导入崩溃。 *Qualys parser resilience — findings whose QID has no glossary entry are skipped with a warning instead of crashing the whole import.*
- **[kizuna-ai-lab/sokuji](https://github.com/kizuna-ai-lab/sokuji)** [![GitHub stars](https://img.shields.io/github/stars/kizuna-ai-lab/sokuji?style=flat&color=gold)](https://github.com/kizuna-ai-lab/sokuji) — 模型导入支持 hf-mirror.com：本机实测 CORS/防盗链链路后落地，curl/wget 命令按 URL 逐条推导镜像改写。 *hf-mirror.com as a model-import source, grounded in on-machine CORS/hotlink measurements, with per-URL mirror rewriting for curl and wget.*
- **[fishjar/kiss-translator](https://github.com/fishjar/kiss-translator)** [![GitHub stars](https://img.shields.io/github/stars/fishjar/kiss-translator?style=flat&color=gold)](https://github.com/fishjar/kiss-translator) — 划词翻译悬停延时：正确的事件语义（relatedTarget 感知的离开检测）+ 计时器生命周期管理，七语界面。 *Hover delay for selection translation with relatedTarget-aware leave detection, clean timer lifecycle, and i18n in seven languages.*
- **[nextai-translator/nextai-translator](https://github.com/nextai-translator/nextai-translator)** [![GitHub stars](https://img.shields.io/github/stars/nextai-translator/nextai-translator?style=flat&color=gold)](https://github.com/nextai-translator/nextai-translator) — 新版 Claude 模型兼容层：拒收 temperature / thinking budget 的启动 400 修复。 *Compatibility fix for current Claude models that reject temperature and thinking budgets.*
- **[docmd-io/docmd](https://github.com/docmd-io/docmd)** [![GitHub stars](https://img.shields.io/github/stars/docmd-io/docmd?style=flat&color=gold)](https://github.com/docmd-io/docmd) — 搜索索引从 /vX.Y.Z/ 版本式 base 路径加载：补上源码注释声称但缺失的绝对 site root 分支。 *Search index loading from versioned base paths like /vX.Y.Z/, via the build-injected absolute site root the code claimed but never used.*
- **[progit/progit2-zh](https://github.com/progit/progit2-zh)** [![GitHub stars](https://img.shields.io/github/stars/progit/progit2-zh?style=flat&color=gold)](https://github.com/progit/progit2-zh) — 《Pro Git》中文版全书 24 处「派生」统一为「分叉」，逐条对照英文原版并写进译者术语表。 *Unified the translation of "fork" from 派生 to 分叉 across 24 occurrences — each verified against the English source — plus a glossary entry.*
<details>
<summary>📊 全部已合并仓库 · All merged repos</summary>

<!-- contributions:start -->
**28** 个已合并 PR · **28** 个上游项目 · 合计 **283.2k** stars

<table>
  <tr><th align="left">项目</th><th align="right">Stars</th><th align="left">项目</th><th align="right">Stars</th><th align="left">项目</th><th align="right">Stars</th></tr>
  <tr><td><a href="https://github.com/career-ops-hq/career-ops">career-ops-hq/career-ops</a></td><td align="right">80.3k</td><td><a href="https://github.com/doocs/leetcode">doocs/leetcode</a></td><td align="right">36.8k</td><td><a href="https://github.com/docsifyjs/docsify">docsifyjs/docsify</a></td><td align="right">31.6k</td></tr>
  <tr><td><a href="https://github.com/nextai-translator/nextai-translator">nextai-translator/nextai-translator</a></td><td align="right">25k</td><td><a href="https://github.com/fishjar/kiss-translator">fishjar/kiss-translator</a></td><td align="right">13.2k</td><td><a href="https://github.com/kornia/kornia">kornia/kornia</a></td><td align="right">12.3k</td></tr>
  <tr><td><a href="https://github.com/jason5ng32/MyIP">jason5ng32/MyIP</a></td><td align="right">12.3k</td><td><a href="https://github.com/Laravel-Lang/lang">Laravel-Lang/lang</a></td><td align="right">7.8k</td><td><a href="https://github.com/supercollider/supercollider">supercollider/supercollider</a></td><td align="right">6.8k</td></tr>
  <tr><td><a href="https://github.com/KaiserY/trpl-zh-cn">KaiserY/trpl-zh-cn</a></td><td align="right">5.7k</td><td><a href="https://github.com/dromara/carbon">dromara/carbon</a></td><td align="right">5.2k</td><td><a href="https://github.com/DefectDojo/django-DefectDojo">DefectDojo/django-DefectDojo</a></td><td align="right">5.2k</td></tr>
  <tr><td><a href="https://github.com/collabora/WhisperLive">collabora/WhisperLive</a></td><td align="right">4.3k</td><td><a href="https://github.com/introlab/rtabmap">introlab/rtabmap</a></td><td align="right">4.1k</td><td><a href="https://github.com/version-fox/vfox">version-fox/vfox</a></td><td align="right">4k</td></tr>
  <tr><td><a href="https://github.com/autokey/autokey">autokey/autokey</a></td><td align="right">3.9k</td><td><a href="https://github.com/Dailin521/codex-provider-sync">Dailin521/codex-provider-sync</a></td><td align="right">3.6k</td><td><a href="https://github.com/aws-powertools/powertools-lambda-python">aws-powertools/powertools-lambda-python</a></td><td align="right">3.3k</td></tr>
  <tr><td><a href="https://github.com/hybridsjs/hybrids">hybridsjs/hybrids</a></td><td align="right">3.2k</td><td><a href="https://github.com/docmd-io/docmd">docmd-io/docmd</a></td><td align="right">2.5k</td><td><a href="https://github.com/mdn/translated-content">mdn/translated-content</a></td><td align="right">2k</td></tr>
  <tr><td><a href="https://github.com/amd/gaia">amd/gaia</a></td><td align="right">1.6k</td><td><a href="https://github.com/progit/progit2-zh">progit/progit2-zh</a></td><td align="right">1.6k</td><td><a href="https://github.com/mxsm/rocketmq-rust">mxsm/rocketmq-rust</a></td><td align="right">1.5k</td></tr>
  <tr><td><a href="https://github.com/kizuna-ai-lab/sokuji">kizuna-ai-lab/sokuji</a></td><td align="right">1.5k</td><td><a href="https://github.com/pipe-cd/pipecd">pipe-cd/pipecd</a></td><td align="right">1.4k</td><td><a href="https://github.com/blixvip/NullMotion">blixvip/NullMotion</a></td><td align="right">1.3k</td></tr>
  <tr><td><a href="https://github.com/eugenioenko/ttt">eugenioenko/ttt</a></td><td align="right">1.1k</td><td></td><td></td><td></td><td></td></tr>
</table>
<!-- contributions:end -->

</details>

## 技术栈 · Tech Stack

`Go` · `Rust` · `Python` · `TypeScript` · `C# / Avalonia` · `Tauri` · `FastAPI` · `Docker` · `SQLite` · `MLX` · `CUDA`
