# 模块 7 · ABM 与涌现 —— 从异质 agent 到宏观规律

> "Agent-based models are to economics what statistical mechanics was to thermodynamics: a microfoundation for macro behavior."
> —— J. Doyne Farmer (paraphrased, Santa Fe Institute lecture)

模块 2–4 我们用统计工具刻画了**宏观 stylized facts**:重尾、波动率聚集、协方差谱。模块 5–6 我们看到这些事实在**机制层面**(临界现象、LOB)有部分解释。但还有一个层级没碰:**异质交易者之间的交互**。这模块用 agent-based models(ABM)把这一层补上,看看从简单的微观规则出发,宏观规律能否自然涌现。

读完本模块后,你应该能:

1. 描述 ABM 在科学方法论上的位置(和 DSGE、自顶向下的均衡模型对比)
2. 写出 Minority Game 的基本规则,解释为什么它的"集合行为"在某个参数区间产生重尾
3. 解释 heterogeneous agents(基本面派 vs 趋势派)模型如何**同时**给出重尾、波动率聚集、bubble-and-crash
4. 用 Python 跑一个简单 ABM,看几个 stylized facts 是否自发涌现

---

## 7.1 ABM 在科学方法论上的位置

主流经济学的核心是 **DSGE(Dynamic Stochastic General Equilibrium)** 这一脉:**代表性 agent**、理性预期、市场出清的方程系统。批评点很多,核心一条:**代表性 agent = 没有交互**,但市场是异质交易者交互的产物。

ABM 是反方向的:**从异质 agent 的局部规则出发,涌现出宏观行为**。这和统计物理的步骤完全一样——从分子的微观相互作用,涌现出温度、压强、相变。

| 维度 | DSGE | ABM |
|---|---|---|
| Agent | 代表性(homogeneous) | 异质(heterogeneous) |
| 预期 | 理性(rational expectations) | 适应性(adaptive) / 学习 |
| 均衡 | 闭式不动点 | 涌现的动态(可能多稳态) |
| 验证 | 内部一致性 + 部分实证 | stylized facts 复现度 |
| 数学 | 优化 + 动态规划 | 模拟 + 统计 |

**ABM 不是"DSGE 的替代",更准确说是 DSGE 假设的检验台**。在某个 ABM 里,如果你强迫所有 agent 同质 + 理性,你应该回到 DSGE 预测;如果你放松到异质,会涌现出 DSGE 抓不到的现象(重尾、危机、多稳态)。

ABM 的几个标准批评(中肯的):

1. **参数太多,容易过拟合**——同样的 stylized facts,不同 ABM 都能复现,等于没证伪
2. **校准困难**——agent 数量、规则参数、初始条件,组合空间巨大
3. **机制 vs 拟合**——拟合好不等于机制对

模块 8 会回到这些批评,讨论"宏观本构关系"作为 ABM 简化的方向。

---

## 7.2 Minority Game:最小的 ABM

Challet–Zhang(1997)的 **Minority Game (MG)** 是 ABM 历史上最简洁的模型。规则:

- $N$ 个 agent(奇数),每轮选 $\pm 1$
- **赢的是少数派**(因此叫 minority)。如果整体多数选 $+1$,选 $-1$ 的赢
- 每个 agent 有 $s$ 个**策略**(从过去 $m$ 步信息映射到当前选择的函数表),每轮用得分最高的那个

这个模型的天才之处:**没有信息,没有理性,只有简单规则**,却涌现出价格序列的 stylized facts。

### 7.2.1 MG 的关键现象

定义**控制参数** $\alpha = 2^m / N$($m$ 是记忆长度,$N$ 是 agent 数)。系统行为有三个区间:

- **$\alpha \gg 1$**:agent 多过策略空间,行为接近随机——市场无效率反而最强(可预测性最高)
- **$\alpha \approx \alpha_c$**(典型 $\alpha_c \approx 0.3$):**临界相变**。涨落 $\sigma^2(\alpha)/N$ 有极小值,系统对参数最敏感
- **$\alpha \ll 1$**:agent 太多,策略相互抵消,涨落大,但价格相对可预测性低

在临界点附近,价格序列**自发产生重尾、波动率聚集** —— 而这正是我们在 S&P 500 上看到的!

**这是 econophysics 一个标志性论证**:复杂的 stylized facts 不需要"复杂"的微观假设,简单的**异质 + 适应**就够。

---

## 7.3 Heterogeneous Agents:基本面派 vs 趋势派

更接近现实的 ABM 通常包含两类 agent:

- **Fundamentalists**:相信存在一个"基本面价格"$p^*$,当 $p_t < p^*$ 时买入,$p_t > p^*$ 时卖出。这是稳定力量。
- **Chartists / Trend-followers**:相信"趋势会延续",过去几天涨过则买,跌过则卖。这是放大力量。

经典模型(Lux 1995, Brock & Hommes 1998)用一个**切换机制**——agent 根据近期收益在两类之间切换。结果:

- 当趋势派占优,价格被推离基本面 → bubble
- 偏离够大时基本面派回归吸引力大,趋势派**集体切换** → crash
- 这个切换是**非线性**的,产生**多稳态**和**波动率聚集**

**关键洞察**:重尾、波动率聚集、bubble-and-crash **同时涌现**,不需要外部冲击。这比单独建模一个 stylized fact 强得多。

Bouchaud 等人后来发展出 "**herding + reference price**" 的连续版本,在订单簿层面复现 square-root impact + 长程相关——把模块 6 的微观结构和模块 7 的 ABM 缝起来。

---

## 7.4 ABM 对主流范式的真正挑战

ABM 真正动摇主流经济学的不是"DSGE 错了",而是:

1. **市场可以长期偏离均衡**——非线性反馈下"基本面价格"不一定收敛
2. **危机不需要外部冲击**——内生的羊群切换就够。2008 不一定是"次贷的外生冲击",可能只是某个均衡不稳定性的实现
3. **代表性 agent 假设系统性低估尾部风险**——同质性消灭了集体切换这个机制,VaR 计算反而比 ABM 低
4. **政策影响通过"agent 类型分布"传导**,而不是通过"代表性 agent 的优化"——央行 forward guidance 在 ABM 框架下可以引起 agent 分布漂移

后两点是 2008 后被各大央行(尤其英格兰银行)严肃看的方向。Andy Haldane 2012 年那篇讲话直接呼吁把 ABM 纳入金融稳定监测。

---

## 7.5 实战:Python Lab —— 一个简版异质 agent 模型

下面这段代码实现 Lux-Marchesi 风格的 minimal heterogeneous agent 模型:基本面派 + 趋势派,带切换。

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
T = 5000
N = 500
p_star = 100.0     # 基本面价格
p = np.zeros(T); p[0] = p_star

# 每个 agent 的"派系":1 = fundamentalist, 0 = chartist
fund_frac = np.zeros(T); fund_frac[0] = 0.5

# 参数
alpha_f = 0.02     # 基本面派强度
alpha_c = 0.10     # 趋势派强度
gamma = 5.0        # 切换敏感度
sigma_noise = 0.005

for t in range(1, T):
    # 当前需求
    n_fund = N * fund_frac[t-1]
    n_chart = N - n_fund
    demand_fund = alpha_f * (p_star - p[t-1]) * n_fund
    if t > 5:
        trend = np.mean(np.log(p[t-5:t]) - np.log(p[t-6:t-1]))
    else:
        trend = 0.0
    demand_chart = alpha_c * trend * n_chart
    excess = demand_fund + demand_chart
    p[t] = p[t-1] * np.exp(excess / N + sigma_noise * np.random.randn())

    # 切换:基本面派近期表现(避免追高)
    fitness_f = -np.log(max(p[t]/p_star, p_star/p[t]))  # 远离基本面价时,fund 的"对"
    fitness_c = trend * np.sign(excess)                  # chart 跟上趋势时正
    # softmax 切换
    z_f = np.exp(gamma * fitness_f)
    z_c = np.exp(gamma * fitness_c)
    fund_frac[t] = z_f / (z_f + z_c)

r = np.diff(np.log(p))

fig, axes = plt.subplots(2, 2, figsize=(13, 10))
axes[0,0].plot(p); axes[0,0].axhline(p_star, color="r", ls="--")
axes[0,0].set_title("Price path")

axes[0,1].plot(fund_frac); axes[0,1].set_title("Fundamentalist fraction")
axes[0,1].set_ylim(0, 1)

axes[1,0].hist(r, bins=80, density=True); axes[1,0].set_yscale("log")
axes[1,0].set_title("Return distribution (log)")

from statsmodels.tsa.stattools import acf
lags = np.arange(1, 200)
axes[1,1].loglog(lags, np.maximum(acf(np.abs(r), nlags=200, fft=True)[1:], 1e-4), "k.")
axes[1,1].set_title(r"ACF of $|r|$")

plt.tight_layout()
plt.show()
```

**你应该看到**:

- 价格在 $p^*$ 周围 oscillate,偶尔形成 bubble 然后被拉回
- 基本面派比例剧烈切换——成簇地变到 $> 0.8$ 或 $< 0.2$
- 收益率分布重尾(log 尺度下尾部不是抛物线)
- $|r|$ 的 ACF 有长平台——**波动率聚集**自发涌现

四个 stylized facts(bubble、切换、重尾、聚集)**从同一个最小模型涌现**——这是 ABM 最有说服力的演示。

---

## 7.6 常见误解

- **"ABM 拟合 stylized facts 等于解释了它们"**——不一定。能复现不等于机制对。需要进一步的鉴别性实证。
- **"agent 越复杂越好"**——错。最少的假设涌现最多的 fact,才是好 ABM。Minority Game 用极简规则就能复现重尾。
- **"ABM 完全没用,只是模拟玩具"**——20 年的发展使 ABM 在央行(BoE、ECB)、学术界(SFI)、部分对冲基金里有严肃应用。Haldane 2012 的讲话是分水岭。
- **"代表性 agent 就是错的"**——代表性 agent 在某些场景(长期平均行为)非常有用,错的是把它当万能。ABM 的论证是它**不够刻画危机**。
- **"ABM 不可证伪"**——只要你预先承诺哪些 stylized facts 算复现成功、复现度如何度量,就可以证伪。当代严肃的 ABM 文献都在这么做。

---

## 7.7 章末小结与延伸

### 本模块核心回顾

1. **ABM 是 DSGE 的镜像**:自下而上 vs 自上而下,异质 vs 代表性。两者互补,而非互斥。
2. **Minority Game** 用极简规则演示**异质 + 适应 → stylized facts**,临界参数 $\alpha_c$ 是又一个"近临界"信号。
3. **Heterogeneous agents(基本面 + 趋势)** 模型在简单切换机制下**同时**涌现重尾、聚集、bubble-and-crash。
4. **ABM 对主流的真正挑战**在于"长期偏离均衡"、"内生危机"、"代表性 agent 低估尾部"——这是 2008 后被央行严肃看的方向。
5. **未来方向**:ABM × 机器学习(用 RL 替换规则 agent)、ABM × LOB(模块 6 + 7)、ABM × policy stress test(英格兰银行)。

### 习题

#### 习题 7.1(简单)

为什么"少数派赢"是 Minority Game 的关键设计?和"多数派赢"(coordination game)对比一下,后者会出现什么?

#### 习题 7.2(中等)

Heterogeneous agents 模型里,如果趋势派强度 $\alpha_c \to 0$,系统的稳态行为是什么?如果 $\alpha_f \to 0$ 呢?哪一个极限对应"理性预期"的图像?

#### 习题 7.3(中等,需跑代码)

跑 7.5 节代码。然后:
(a) 把 `gamma`(切换敏感度)从 5 调到 50,$|r|$ 的 ACF 衰减率怎么变?
(b) 把基本面价格 $p^*$ 设成一个慢变化序列($p^*_t = 100 + 0.01t$),会涌现 trend-following 行为吗?

#### 习题 7.4(开放)

如果你是 BIS 的金融稳定研究员,想用 ABM 评估"取消利率下限"的政策。你会怎么校准 agent 类型分布?怎么衡量结果的 robustness?

#### 习题 7.5(挑战)

模块 5 的临界现象和模块 7 的 minority game 临界点($\alpha = \alpha_c$)是同一回事吗?(提示:都是统计物理意义上的二阶相变,标度律应该 universal。试着估出 minority game 的临界指数,和 Ising 比对。)

### 延伸阅读

**必读:**

- Farmer, J. D., & Foley, D. (2009). "The economy needs agent-based modelling." *Nature*, 460, 685.
- Hommes, C. H. (2006). "Heterogeneous agent models in economics and finance." *Handbook of Computational Economics*, 2.

**值得翻:**

- Challet, D., & Zhang, Y.-C. (1997). "Emergence of cooperation and organization in an evolutionary game." *Physica A*, 246. —— Minority Game 起点。
- Lux, T., & Marchesi, M. (1999). "Scaling and criticality in a stochastic multi-agent model." *Nature*, 397, 498.
- Haldane, A. (2012). "The dappled world." Bank of England speech. —— 政策影响立场鲜明。

**进阶:**

- Challet, D., Marsili, M., & Zhang, Y.-C. (2005). *Minority Games*. Oxford. —— MG 的完整数学处理。
- LeBaron, B. (2006). "Agent-based computational finance." *Handbook of Computational Economics*, 2.

---

### 下一模块预告

到这里 stylized facts、临界现象、微观结构、ABM 都讲过一遍。最后一模块要做一件雄心大但目前还在开放阶段的事:**把市场写成偏微分方程**——用流体力学的语言看价格、流动性、波动率作为"场"的演化。这是物理直觉的最远归宿,也是 econophysics 当前最活跃的开放方向之一。

---

> **本模块一句话总结**
>
> ABM 的论证不是"DSGE 错了",而是"异质 + 适应 + 局部交互在简单规则下就能涌现所有 stylized facts"——这件事在 Minority Game 和 heterogeneous agents 模型里都被反复验证,且对央行的金融稳定监测开始有真实政策影响。

---

## 📝 学习记录

| 项 | 内容 |
|---|---|
| 起始日期 | |
| 完成日期 | |
| 卡点 | |
| 关键收获 | |
| 配套代码仓库链接 | |
