# Econophysics 笔记 —— mdBook 项目

> 物理学家视角下的金融市场

这是一本写给有物理 / 应用数学 / 工程 / 计算机科学背景的自学者的经济物理学教材。它把金融市场当作"统计力学系统"来理解,从经验规律(重尾、波动率聚集、关联结构)走到机制(临界现象、订单簿、ABM),最终落到流体力学视角的开放方向。

---

## 🚀 部署到 Vercel(推荐路径)

最佳协作姿势:**改 .md → git push → Vercel 自动重新构建并部署**。

Vercel 端的接入步骤:

1. GitHub 建仓 → 把当前 repo push 上去
2. Vercel 控制台 New Project → 选这个 repo
3. Framework Preset 选 *Other*,其余字段留空(`vercel.json` 已经写好 build / output)
4. Deploy,首次构建约 30 秒

之后每次 `git push` 触发一次重新构建。

---

## 💻 本地预览

### 安装 mdBook

```bash
cargo install mdbook
```

或下载预编译二进制:<https://github.com/rust-lang/mdBook/releases>

### 启动本地服务

```bash
mdbook serve --open
```

浏览器自动打开 `http://localhost:3000`,支持:

- 左侧目录导航(全模块折叠/展开)
- 顶部搜索框(`s` 快捷键)
- 代码块语法高亮、复制按钮
- 浅色 / 深色主题切换
- MathJax 渲染数学公式
- 文件改动后自动重新构建并刷新浏览器

### 导出静态站点

```bash
mdbook build
```

输出在 `book/` 目录。

---

## 📂 目录结构

```
learn-econophysics/
├── README.md              # 本文件
├── book.toml              # mdBook 配置(启用 MathJax)
├── vercel.json            # Vercel 构建配置
├── .gitignore
├── .github/
│   └── workflows/
│       └── build.yml      # CI:mdbook build + lychee 链接检查
└── src/
    ├── SUMMARY.md         # mdBook 目录(入口)
    ├── introduction.md
    ├── module-01-birth-of-the-field.md
    ├── module-02-heavy-tails.md
    ├── module-03-stochastic-processes.md
    ├── module-04-correlation-rmt.md
    ├── module-05-critical-phenomena.md
    ├── module-06-microstructure-orderbook.md
    ├── module-07-agent-based-models.md
    └── module-08-fluid-dynamics-frontiers.md
```

---

## 📊 内容状态

| 模块 | 状态 |
|---|---|
| 引言 | ✅ 完整 |
| 模块 1 · 学科诞生 | ✅ 完整 |
| 模块 2 · 重尾分布 | 🚧 stub |
| 模块 3 · 随机过程 | 🚧 stub |
| 模块 4 · 关联结构与 RMT | 🚧 stub |
| 模块 5 · 临界现象 | 🚧 stub |
| 模块 6 · 微观结构与订单簿 | 🚧 stub |
| 模块 7 · ABM 与涌现 | 🚧 stub |
| 模块 8 · 流体力学视角与开放方向 | 🚧 stub |

---

## 🔄 CI / CD

GitHub Actions 工作流(`.github/workflows/build.yml`)在每次 push 和 PR 时:

1. **mdbook build** —— 验证整本书能构建
2. **lychee link check** —— 扫描所有 .md 中的链接

CI 通过后 Vercel 自动部署。

---

## 🛠 个性化

- **主题色**:`mdbook init --theme` 生成 `theme/` 目录,改 `theme/css/variables.css`
- **数学公式**:`book.toml` 里已启用 `mathjax-support = true`,行内用 `\\( ... \\)` 或 `$ ... $`,块级用 `\\[ ... \\]` 或 `$$ ... $$`
- **Mermaid 图**:安装 `mdbook-mermaid` 预处理器
- **配套 Python lab**:每个模块末尾的"实战"小节带 Python 代码,可单独跑或放进 `learn-econophysics-code/` 仓库

---

## 📝 推荐工作流

1. 每天学习前 `mdbook serve` 开本地预览
2. 学完一个模块后,在该模块末尾的"📝 学习记录"表格填日期 / 卡点 / 关键收获
3. 配套 Python 代码贴回学习记录里
4. 一周一次 `git push` 触发 Vercel 重建,顺便复盘本周进展
