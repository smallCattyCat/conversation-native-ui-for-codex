# 面向 Codex 的对话原生 UI 设计套件

**把 Claude 的视觉细节，变成 Codex 可以执行的设计规范。**

暖中性色、清楚但克制的字号层级、衬线与无衬线的分工、细边框、轻阴影、限宽阅读列、单色线框图标和按需展开的工作区。本项目明确引用 Anthropic 的公开设计规范，将官方参数与自行适配的布局选择逐项区分。

**[在线演示站](https://smallcattycat.github.io/conversation-native-ui-for-codex/)** · [对话与写作](https://smallcattycat.github.io/conversation-native-ui-for-codex/examples/claude-inspired/) · [组件画廊](https://smallcattycat.github.io/conversation-native-ui-for-codex/examples/pattern-gallery/) · [证据工作台](https://smallcattycat.github.io/conversation-native-ui-for-codex/examples/evidence-workbench/)

视觉预设可以独立复用；证据卡、适用条件、授权状态是专业任务的可选组件，不要求所有页面都变成工程仪表盘。

## R2 包括什么

- **Claude UI 视觉对照指南**：颜色、字号、字体替代、圆角、边框、交互状态与来源。
- **可直接复用的 CSS**：明暗主题、语义变量和 `.cnui` 作用域，位于 Skill 内部。
- **交互组件资源**：`assets/patterns.css` 和 `assets/patterns.js`，提供卡片、横向比较和工作区模式。
- **通用对话示例**：任务切换、可编辑工作笔记、本地输入、主题切换。
- **新增组件画廊**：Inline Card 的四种状态、四个可比较选项的 Carousel、可编辑全屏工作区；编辑草稿不会在重新打开时被覆盖。
- **AGENTS.md**：Codex 进入本仓库时采用的原则与验证要求。
- **Agent Skill**：位于 .agents/skills/conversation-native-ui/，可以复制到其他项目。
- **三种界面模式**：判断卡、可比较对象集合、证据工作台。
- **判断数据契约**：区别计算、引用、推断和待核实信息，并表示适用条件及授权状态。
- **演示页面**：纯 HTML / CSS / JavaScript，无依赖、无需密钥，能直接运行。
- **测试和归因文档**：便于继续开发与对外发布。

## 立刻体验

打开 `examples/claude-inspired/index.html` 体验通用对话示例，`examples/pattern-gallery/index.html` 查看三类组件；专业任务示例在 `examples/evidence-workbench/index.html`。也可以在仓库根目录执行：

    python3 -m http.server 8000

浏览器访问 http://localhost:8000/examples/claude-inspired/。

示例演示的是专业任务的**交互设计**，其中数据均明确标注为构造样例，不应解释为真实 MATLAB 计算、PLC 控制输出或模型评测结论。

## 在你自己的 Codex 项目中复用

可以手动复制 `.agents/skills/conversation-native-ui/` 文件夹，或使用安全安装脚本（只安装到已有项目，默认拒绝覆盖）：

    python3 scripts/install_skill.py --target /path/to/project --dry-run
    python3 scripts/install_skill.py --target /path/to/project

如需更新已有版本，可使用 `--force`，会先备份旧版本。再对 Codex 说：

> 使用 $conversation-native-ui 的 Claude-inspired 视觉预设。先读取 references/claude-ui-design.md 与 assets/claude-inspired.css。保留暖中性色、阅读型排版、轻边框和克制控件，用我们的产品名称；按实际任务选择布局，不默认生成 KPI 仪表盘。只有涉及来源判断或外部行动时才增加证据与授权模块。

不需要把演示应用整体搬进目标项目。**先迁移视觉规则和样式变量，按需采用组件与数据契约。** 完整 [Claude UI 借鉴说明](docs/claude-ui-reference.md) 记录了每项细节的来源。

新增的 [组件实现契约](docs/component-contracts.md) 解释了复用接口、状态与真正 MCP App 的区别；[设计来源对照](docs/figma-crosswalk.md) 区分官方参数、独立适配与尚未获得的原始 Figma 节点信息。[基准测试](benchmarks/README.md) 提供 Codex 安装前后对照的三类任务和评分表，目前尚未运行真实 A/B 生成实验，不能宣称 Skill 已经证明提升了模型效果。

## GitHub Pages 公开演示准备

已添加独立首页以及自动构建脚本：

```bash
python3 scripts/build_site.py
python3 -m http.server 8000 --directory site-dist
```

浏览器打开 `http://localhost:8000/` 可查看站点首页和三个示例。**GitHub Pages 已正式上线**：[访问在线演示站](https://smallcattycat.github.io/conversation-native-ui-for-codex/)。部署工作流 [第 2 次运行成功](https://github.com/smallCattyCat/conversation-native-ui-for-codex/actions/runs/38452675497)，首页和三个示例已经通过实际浏览器验证。详情见 [发布说明](docs/publishing.md)。

## 与已有 frontend-agent-kit 的关系

本 Skill 提供明确的 **Claude-inspired 视觉方向与交互细则**。通用前端工具可以负责工程实现与检查，但不应把已选定的暖中性阅读界面重新解释成其他风格。证据与行动模式按任务启用。

## 来源与边界

视觉预设明确借鉴 Anthropic 的 MCP Apps for Claude 公开规范及品牌色资料；组件代码与页面组合独立实现。**没有打包原始 Figma 文件、Logo 或字体文件**。引用见 NOTICE.md。源码和原创文档使用 MIT 授权；第三方资源仍保留其原有权利。

参见 [设计哲学](docs/philosophy.md)、[交互模式](docs/patterns.md)、[质量清单](docs/quality-gates.md)。

