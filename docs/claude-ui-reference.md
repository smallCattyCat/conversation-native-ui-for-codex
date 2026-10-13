# Claude UI 借鉴说明：从设计哲学到可见细节

核查日期：2026-10-13。完整来源及设计参数见 [随 Skill 分发的视觉指南](../.agents/skills/conversation-native-ui/references/claude-ui-design.md)。

## 这轮的定位调整

项目现在首先是一套 **Claude-inspired UI patterns for Codex**：让开发者能够得到熟悉的暖中性色、阅读节奏、轻量控件和克制的界面层级。证据卡、适用条件、人工确认等是专业任务的可选扩展，而不是每个页面必须携带的仪表盘结构。

## 我们具体借鉴什么

| 细节 | 本项目采用的方式 | 依据与边界 |
| --- | --- | --- |
| 暖中性底色 | 阅读背景 #FAF9F5，侧栏 #F5F4ED，前景白色 | 色值来自官方 MCP Apps 规范；区域分配是本项目选择 |
| 深色主题 | #141413 / #262624 / #30302E 三层底色 | 来自官方明暗主题变量；不是把浅色页面简单反色 |
| 字体层次 | 20 / 16 / 12px 的组件标题、正文、说明；14px 控件 | 从官方字号集合中选取，不把所有字号同时塞进页面 |
| 衬线与无衬线的分工 | 编辑性页面标题用系统衬线，操作界面用系统无衬线 | 为便携性做的替代；不是原版 Anthropic 字体 |
| 细边框与圆角 | 0.5px 分隔线，8px 控件，12px 卡片和输入区 | 使用官方 token 数值；控件边界与焦点框另行保证可见性 |
| 少量暖色点缀 | #D97757 只用于小面积装饰，不作为正文文字 | 来自 Anthropic 品牌色；不能等同于所有 Claude 按钮的颜色 |
| 阅读优先 | 限宽正文、无框助手段落、较轻的用户消息底色 | 本项目的独立页面组合，不声称是 Figma 节点测量 |
| 克制的交互 | 可见选项、明确焦点、卡片底部操作、按需展开工作笔记 | 借鉴官方交互原则；独立网页的输入区不应搬进 MCP 卡片 |

## 可以立即体验的页面

打开 [Claude-inspired conversation](../examples/claude-inspired/index.html)。这是一张完整独立网页，包括三种任务示例、亮／暗／系统主题、可编辑工作笔记和本地输入演示。页面不是截图，也不调用模型。

已有 [Evidence workbench](../examples/evidence-workbench/index.html) 保留为专业任务示例。两者共用视觉预设，避免每做一个页面就重新决定颜色和按钮样式。

R2 新增 [Pattern Gallery](../examples/pattern-gallery/index.html)，实际实现了单结果卡的四种状态、四选项横向 Carousel、可编辑的独立网页全屏工作区。交互样式与可选辅助 JS 位于 `.agents/skills/conversation-native-ui/assets/patterns.css`、`patterns.js`。这不是 MCP host fullscreen，而是 standalone browser dialog 示例。

不同来源的设计细节、尚未验证的 Figma 精确参数及宿主支持边界在 [来源逐项对照](figma-crosswalk.md) 中列出；实现接口在 [组件契约](component-contracts.md) 中列出。

## 复用方法

将 `.agents/skills/conversation-native-ui/` 整个目录复制到目标项目。在 Codex 中说明：

> 使用 conversation-native-ui 的 Claude-inspired 视觉预设。先读取 references/claude-ui-design.md 和 assets/claude-inspired.css；保留暖中性底色、字体层次、轻边框与阅读型布局；按本项目实际任务选择组件，不默认生成 KPI 仪表盘。只在有来源判断或外部行动时加入证据与授权信息。用自己的产品名称，并保留来源说明。

在已有设计系统中只迁移规则或做 token 映射，不覆盖项目的全局样式。`.cnui` 是本套件的样式作用域。

## 归因方式

README 中采用明确表述：本项目的视觉预设借鉴 Anthropic 公开的 MCP Apps for Claude 设计规范及品牌色资料，组件代码与页面组合独立实现。文档区分公开参数与本项目的适配选择。

这比只说“受到启发”更具体，也不把自己的留白数值、字体替代或页面布局冒充官方规范。原始 Figma 文件、Logo 和字体文件均未加入仓库。
