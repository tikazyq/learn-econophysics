# 模块 1 · 学科诞生 —— 物理学家为何进入金融

> "I have endeavoured to give a precise idea of the laws of chance which govern speculation."
> —— Louis Bachelier, *Théorie de la spéculation* (1900)

---

1900 年 3 月 29 日,巴黎大学理学院的答辩厅。委员会三人:Paul Appell 主席,Joseph Boussinesq,Henri Poincaré 任审稿人。被答辩的论文叫 *Théorie de la spéculation*,作者 Louis Bachelier,二十九岁。论文要解决的问题——巴黎证券交易所里的政府债券价格随时间如何波动——以及它给出的答案——价格变化是连续的、独立的、其概率分布满足一个抛物型偏微分方程——对委员会来说是陌生的。Poincaré 在审稿意见里给的评语是友好但克制的:作者表现出"非常独到且非常精确的分析头脑",但"主题与我们常出给候选人的题目相去较远"。

那个抛物型方程的解,是后来 Einstein 1905 年在他关于花粉颗粒的论文里独立写出的同一个东西。Bachelier 比 Einstein 早了五年。论文给的等级是 *mention honorable*——通过,但远不及 *très honorable*。在当时的法国学术系统里,这两个等级之间的差距,直接决定你能否进巴黎的高校。Bachelier 没能进。他此后大半辈子在外省做副教授,1946 年去世于贝桑松。直到他去世后将近十年,Jimmy Savage——芝加哥大学的统计学家——才在某个图书馆的角落里偶然翻到 Bachelier 的论文。Savage 给他认识的几位经济学家寄了明信片,大意是:你们应该知道还有这么个人。其中一张到了 MIT 的 Paul Samuelson 手上。

Samuelson 读完之后,1965 年发表了 *Rational Theory of Warrant Pricing*,把 Bachelier 的算术布朗运动改写成几何布朗运动——这是个不大的技术调整,但它让模型适配于"价格不会跌穿 0"这件事。八年后,Samuelson 的两位学生兼合作者 Fischer Black 和 Myron Scholes、再加上 Robert Merton,把这个框架推到了它的逻辑终点:**Black–Scholes 期权定价公式**。这条线从此再没断过。今天全世界衍生品市场每天数十万亿美元的名义未平仓量,定价基础是 Bachelier 1900 年那个被 Poincaré 评为"主题相去较远"的方程。

把这件事说穿的话:**金融学最核心的数学结构,从一开始就是物理学的语言**。Brownian motion、扩散方程、随机微积分,这些工具不是经济学家发明给金融用的——它们是物理学家发明出来描述布朗颗粒、热传导、量子涨落的,然后在某个不被任何人注意的午后,被一个数学水平很高、运气不太好的法国青年率先拿来描述股价。物理学家进入金融,某种意义上不是"入侵",是回到一个本来就由物理工具搭起来的房子。

---

Bachelier 论文里有一个细节,Samuelson 在 1960 年代重读时也注意到了,但没多说——Bachelier 假设价格变化服从正态分布。这是 1900 年的合理选择:抛物型扩散方程的解是高斯,Bachelier 给的是数学闭包最干净的版本。从他到 Samuelson 再到 Black–Scholes,这个假设一路保留下来。Black–Scholes 1973 年的公式,**前提是对数收益率服从正态分布**。

但 1962 年,在 IBM Watson Research Center 的一栋办公楼里,一件不寻常的事发生了。哈佛经济学家 Hendrik Houthakker 来访问,带着一个箱子——里面是当时已知最长的连续日价格数据,纽约棉花交易所大约百年的日报价。他把箱子交给 IBM 的一位数学家,理由是这位数学家正在做一种听起来很怪的东西,叫"分形"。这位数学家叫 Benoît Mandelbrot。

Mandelbrot 把棉花数据画出来,做的第一件事是直方图叠正态分布。他后来回忆,那一刻他几乎是立刻看出来:**这不是正态**。极端日变动出现的频率比正态分布预测的高得多——不是"高一点",是高出几个数量级。如果你假定收益率服从 $\mathcal{N}(\mu, \sigma^2)$,一个 6σ 事件大约每 50 万年来一次;Mandelbrot 在棉花数据里,这种事件每隔几年就出现。

1963 年,他在 *Journal of Business* 36(4) 发表了 *The Variation of Certain Speculative Prices*,提出用 **Lévy 稳定分布(Lévy stable distribution)** 来描述收益率——一类允许"重尾"的分布家族,Cauchy 分布是其中最有名的特例。Lévy stable 的核心特征是**方差无穷**:你不能算"年化波动率"这种东西,因为样本方差不收敛。

这是经济物理学方法论上的真正起点:**用数据说话,而不是用方便性挑模型**。

主流经济学界的反应,事后看是一个范式选择的标本。Eugene Fama 在 1965 年的博士论文里完整承认了 Mandelbrot 的观察——收益率确实不是正态,极端事件确实更多。然后 Fama 接着用正态分布做了 Efficient Market Hypothesis 的核心推导。1973 年 Black–Scholes 也接着用正态。这条路线选择的不是"否认数据",而是"承认数据,但保留模型"。这种态度——**知道有问题,但模型继续用**——是后来三十年里物理学家越来越不满的根源。Bouchaud 2008 年那篇标题刺眼的 *Nature* 短文 *Economics Needs a Scientific Revolution*,核心抱怨就是这条:经济学有一套把异常吸收回模型框架内的强大机制,代价是核心假设永远不需要被真正修改。

物理学家受的训练相反。在物理里,**模型和数据冲突时,错的几乎肯定是模型**。这不是因为物理学家更严谨,而是因为物理研究的对象——电子、流体、晶格——不会因为你用了某个错的模型就配合你装得像是对的。市场可以。市场里有人在读 Black–Scholes,然后据此交易;Black–Scholes 因此变成自我实现的预言;直到某天它不再实现,所有人同时发现的瞬间——1987 年 10 月 19 日,后面会讲到。

---

到 1990 年代初,一系列在历史上独立的事件,把一大批训练有素的物理学家推到了金融数据的面前。冷战在 1989–1991 之间结束;苏联解体;美国国会在 1993 年取消了已经开工的超导超级对撞机 SSC 项目,德州沙漠里挖了二十几公里的隧道半途而废。这件事本身在物理史上是一道分水岭——它意味着一代理论物理 PhD 找不到学术岗位。同一时期,Renaissance Technologies 的 Jim Simons(1982 年从纽约州立大学石溪分校的几何学家位置上离职)已经在做量化交易,业绩开始引人注意;Wall Street 的衍生品台开始大规模招物理 PhD 做模型工作。Emanuel Derman 后来的 *My Life as a Quant* 是这一代人最有代表性的自述。

另一部分人没有去 Wall Street,而是留在学界,开始把统计物理的工具——相变、临界现象、scaling laws、随机矩阵理论、disordered systems——直接搬到金融数据上。这股力量集中在几个地方:**波士顿大学的 H. Eugene Stanley** 把他在生物物理学里发展的标度律工具搬过来,做出后来被反复引用的 inverse cubic law(模块 2 主线);**巴黎的 Jean-Philippe Bouchaud**,理论物理出身做 disordered systems,1990 年代末和 Marc Potters 一起创办 Capital Fund Management,这是少数公开发表学术论文的量化对冲基金,Bouchaud 至今仍在两端——CFM 的董事长 + 高等师范学院的物理学教授——都在产出;**Didier Sornette**,地球物理学家出身,在巴黎、UCLA、ETH Zürich 几个地方辗转,把临界现象和 log-periodic oscillations 用于金融崩盘预测,争议大但思路非常物理学家。"econophysics" 这个词的出现,通常归到 Stanley 1995 年在 Kolkata 召开的 Statphys-Kolkata II 会议上。

1999 年是这个学科的拐点。Rosario Mantegna 和 Stanley 合著的 *An Introduction to Econophysics* 出版,这是这门学科的第一本教科书,标志学科形态固定下来。同年,Laloux、Cizeau、Bouchaud、Potters 在 *Physical Review Letters* 83, 1467 发表了那篇用 Marchenko–Pastur 分布解读 S&P 500 协方差谱的工作——把核物理学里 Wigner 和 Dyson 在 1950–60 年代发展的随机矩阵工具,用到了一个组合经理每天都在用但谁也没真正理解的样本协方差矩阵上(模块 4 主线)。同年 Gopikrishnan、Plerou、Stanley 等人发表 *Scaling of the Distribution of Fluctuations of Financial Market Indices* —— inverse cubic law 的奠基性经验论文。专属期刊 *Quantitative Finance* 在 2001 年创刊。从那以后,这个领域有了固定的会议、固定的引用脉络、固定的方法论清单。

|  | 主流金融经济学 | 经济物理学 |
|---|---|---|
| 出发点 | 公理(理性人、无套利、市场出清) | 数据(实证规律) |
| 模型角色 | 描述理性的均衡 | 描述涌现的统计规律 |
| 偏好的数学 | 优化、动态规划、Itô 微积分 | 统计物理、随机过程、复杂系统 |
| 对"异常"的态度 | 模型修补(加跳跃项、改测度) | 异常可能是核心,不是噪声 |
| 验证标准 | 内部一致性 + 部分实证 | 经验拟合 + 出样本预测 |

这张表不是两个阵营的正面冲突,而是两种学科传统的内在偏好。物理学家不是不会做无套利和均衡——只是当数据说"看,这里有个稳定的非高斯结构",他们的本能是去读这个结构是什么,而不是先把它包进一个保留高斯的更复杂模型里。

---

经济物理学和主流金融经济学的分歧,**不是数学水平的问题,而是当数据和模型冲突时该听谁的**。这条分歧的代价,可以通过三个公开的案例文件来读。

**1987 年 10 月 19 日,Black Monday**。S&P 500 当天下跌 22.6%,Dow 跌 22.6%——这是美国市场历史上单日最大跌幅。在 Black–Scholes 框架的高斯假设下,这是一个 5σ × 5 量级的事件,概率大约 $10^{-160}$——比宇宙年龄乘以普朗克时间的倒数还小。换句话说,在那个模型里,Black Monday 物理上不该发生过。当天 Didier Sornette 在 UCLA,他后来回忆,那个早晨他立刻识别出了模式——这和他在异质性材料断裂过程中看到的临界行为有同样的形态。但整个金融工业的反应不是这个。它的反应是引入**隐含波动率 smile**——为每一个执行价格和到期日,在 Black–Scholes 公式里反推出一个不同的 $\sigma$,然后做一张表。这是模型在不动框架的前提下吸收异常的标本操作:Gaussian 假设保留,异常被推到一个"每点都有自己的 $\sigma$"的辅助构造里。这条路一直走到今天的 rough Bergomi 和 SABR——技术越来越复杂,底层假设始终没改。

**1998 年 9 月,Long-Term Capital Management**。基金的董事会上有两位 Nobel 经济学奖得主——Robert Merton 和 Myron Scholes,Black–Scholes 公式的两位作者。LTCM 的核心策略是收敛交易:找到价格之间应该收敛但因为流动性原因暂时偏离的对儿,做空高的、做多低的,等收敛。模型的前提是连续价格路径、稳定的相关结构、不会断裂的流动性——也就是 Black–Scholes 框架的所有底层假设。1998 年 8 月俄罗斯主权债违约,LTCM 在四十天里损失约 46 亿美元,纽约联储紧急召集 14 家投行做出 36 亿美元的救助以避免系统性传染。学界从这件事吸收的标准教训是"相关性可以瞬间切换"。物理学家这边吸收的更深的教训是:Gaussian 假设、连续路径假设、可分散性假设——三个底层在同一周里同时失效。这不是"模型边缘失灵",这是框架在它声称工作的核心区域失灵。

**2008 年,Gaussian copula**。2000 年,摩根大通的 David Li 在 *Journal of Fixed Income* 发表 *On Default Correlation: A Copula Function Approach*。这篇论文把高斯 copula 用作 CDO(担保债务凭证)tranche 定价的关联结构。整个结构化信用工业在接下来八年里采纳了这个公式。它的关键假设是:不同贷款的违约时间之间的依赖结构是高斯的——也就是说,联合的尾部行为继承了多元正态分布的对角衰减。2008 年危机里,违约事件以高斯 copula 几乎不允许的强度同时发生。被评为 AAA 的整个 tranche 都违约了。这不是模型校准错了,是模型的关联结构形式本身没法表征系统性危机里的依赖。

这三个案例放在一起,正好覆盖经济物理学常被引用的三条批评——而且每条批评在这些案例里各有它的中肯和它的不中肯之处:**(1) 经验规律拟合得好,但没有清晰的微观机制**——是,直到模块 6 latent liquidity 和模块 8 反应-扩散 PDE 出现之前,inverse cubic law 这样的事实确实只有标度律没有机制;但同样的批评对 Black–Scholes 也成立,它的"机制"是无套利,无套利在 1987、1998、2008 里都没救场。**(2) 忽略制度因素**——是,纯统计物理工具不直接看监管和央行政策;但 LTCM 救助和 2008 后的 Basel III 都说明制度因素是反应而非外生输入,模块 5(EWS 进入金融稳定监测)、模块 7(Haldane、ABM 进入英格兰银行)反过来给出制度内生化的尝试。**(3) "物理学只有粒子和流体两个寄存器,市场不是这两个,所以物理工具不适用"** ——这条是最常见也最浅的一条。当代物理学有第三个寄存器:**self-referential / observation-coupled / active 系统**——量子测量、active matter physics(鸟群、细菌悬液、上皮组织)、Friston 的自由能原理(大脑作为预测过程的物理化)。市场参与者会学习、会反读模型,不是对物理学的反驳,而是物理学这一分支的定义性特征。这件事是这本书的论证骨架,模块 8 §8.1 把它完整写出。

---

回到最开始的问题:物理学家为什么要进金融?

不是因为他们觉得自己比经济学家聪明,也不是因为他们想推翻 DSGE 或者无套利定理——绝大部分进场的物理学家对经济学并无敌意,很多人甚至专门去读经济学的核心文献,Bouchaud 引用 Keynes 比一般金融博士还熟。他们进场,是因为他们认领了一个对象。这个对象有一组特征——尾指数稳定在 3 附近、长程依赖、近临界标度、自激响应——而这一组特征,在物理学过去七十年的发展里,有现成的工具去测、去拟、去机制化。他们看到一枚指纹,认出了它的种属。

这本书要做的事,就是把这种"认出"的过程,完整地走一遍。

接下来七章,每章拆这枚指纹的一个剖面。模块 2 形式化"尾巴弯曲"本身——什么叫幂律尾,$\alpha \approx 3$ 是怎么估的,陷阱在哪里。模块 3 把时间维度加上,看波动率聚集如何与重尾共存。模块 4 进入多资产,用 Marchenko–Pastur 把样本协方差里的噪声和信号分开。模块 5 把"临界"从直觉变成可测量的诊断。模块 6 拉到微观,看 square-root impact 和限价单簿的机器。模块 7 自底向上用 ABM 重建这一切。模块 8 把所有线索缝进一个偏微分方程,并把整套工作放进物理学的第三个寄存器里。

读到第八章,你应该会发现:你看到的不是八件事,是同一件事的八个侧面。

---

## 习题

> 找一个你自己亲眼见过的"模型有问题但模型继续用"的例子。可以是金融的,也可以是任何工程或科学领域里你接触过的——某个 ML pipeline 里大家心照不宣的偏差,某个仿真里一个明显不成立的假设。把它和 1987 之后 Black–Scholes 在 smile 上的处理方式对比:哪里相似,哪里不同?如果你是那个领域的"经济学家",你会怎么辩护;如果你是那个领域的"物理学家",你会怎么质疑?

> 这一章里说"物理学家进场不是要推翻经济学"。如果你认同这一点,你怎么向一个经济学博士生解释 econophysics 作为一个独立学科的存在合理性——而不是只是"经济学的一个奇怪分支"或者"物理学家的玩票"?如果你不认同,你的反例是什么?

> Mandelbrot 在棉花数据上看到非高斯尾巴的时间是 1962,Fama 在 1965 年正式承认这件事但保留高斯,Black–Scholes 在 1973 用高斯。从 1962 到 1973 之间,有十一年时间可以重做底层假设。为什么没有发生?把答案写成两段:一段从社会学/学术机制的角度,一段从数学便利性的角度。

## 延伸阅读

**起点:**

- Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École Normale Supérieure. —— 翻一翻,看看 1900 年法国数学论文长什么样。
- Mandelbrot, B. (1963). "The variation of certain speculative prices." *Journal of Business*, 36(4), 394–419. —— 经济物理学的起点论文,值得通读。
- Bouchaud, J.-P. (2008). "Economics needs a scientific revolution." *Nature*, 455, 1181. —— 一页短文,立场鲜明。

**学科自述:**

- Mantegna, R. N., & Stanley, H. E. (1999). *An Introduction to Econophysics*. Cambridge University Press. —— 这门学科的第一本教科书。
- Sornette, D. (2014). "Physics and financial economics (1776–2014)." *Reports on Progress in Physics*, 77, 062001. —— 一份近 60 页的全景综述,从 Adam Smith 一路写到 21 世纪。
- Derman, E. (2004). *My Life as a Quant*. Wiley. —— 1990 年代物理学家集体进场的最有代表性的自述。

**背景:**

- Ball, P. (2004). *Critical Mass*. —— 科普读物,把统计物理和社会系统连起来的最佳入门。
- Bernstein, P. (1992). *Capital Ideas*. —— Bachelier–Samuelson–Black–Scholes 这条线的标准故事,从主流金融经济学一侧讲。

**为后续模块做准备:**

- Bouchaud, J.-P., & Potters, M. (2003). *Theory of Financial Risk and Derivative Pricing*. —— 模块 4、6 会反复用到。
- Sornette, D. (2003). *Why Stock Markets Crash*. —— 模块 5 主线。
