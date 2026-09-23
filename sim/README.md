# 仿真与计算

光学是"能算"的学科。这里的仿真不是为了好看，而是为了：

1. **在买器材之前**验证一个实验方案是否可行。
2. **在实验结果异常时**判断是理论错了还是装置错了。
3. **在实验之后**把数据纳入统一模型。

## 环境

> **状态：已建好（2026-09-23）。** 下面是重建步骤，不是待办。

```powershell
cd D:\Optics_Master\sim
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**已装版本**（Python 3.14.6 / venv）：

| 包 | 版本 |
| --- | --- |
| numpy | 2.5.3 |
| matplotlib | 3.11.2 |
| scipy | 1.18.1 |
| pandas | 3.0.6 |

**两个实测踩过的坑**

1. **不要用清华镜像装。** 2026-09 实测 `pypi.tuna.tsinghua.edu.cn` 上还没有
   Python 3.14 的 wheel，会报 `No matching distribution found`；
   用 PyPI 官方源（默认）就能直接下到 cp314 的 wheel。
2. **不要用 `Activate.ps1`。** PowerShell 的脚本执行策略会拦它，
   直接用 `.\.venv\Scripts\python.exe` 调用更省事，也避免污染当前会话。

**中文标注已经配好**：`sim/matplotlibrc` 里设了 `Microsoft YaHei` 与
`axes.unicode_minus: False`，从本目录运行脚本时图上可以直接写中文，不会出方框。
（`axes.unicode_minus` 那条是关键：默认的 Unicode 减号会让中文标签里的负号变成方框。）

## 库的选择（按需装，不要一次全装）

| 库 | 用途 | 何时用 |
| --- | --- | --- |
| `numpy` `scipy` `matplotlib` | 一切的基础 | 立刻 |
| `pandas` | 数据处理 | 立刻 |
| `jupyterlab` | 交互式探索 | 立刻 |
| `rayoptics` `prysm` | 几何光学追迹、系统分析 | S1 |
| `lightpipes` `diffractio` | 物理光学/衍射传播 | S2 |
| `poppy` | 成像系统物理光学传播（天文级） | S2 |
| `tmm` | 薄膜传输矩阵 | S3 |
| `scikit-image` | 图像处理（条纹、散斑分析） | S2 起 |
| `hcipy` `aotools` | 自适应光学、波前传感 | S6 |
| `meep` `gdstk` | FDTD、微纳光子学、版图 | S6 |
| `torch` / `jax` | 逆设计、自动微分光学 | S6 |

## 目录约定

```text
sim/
├─ README.md
├─ lib/              # 自己写的可复用模块（如 fresnel.py, tmm.py, fit.py）
├─ 001-ray-tracer/   # 每个仿真一个文件夹
│   ├─ README.md     # 目的、模型、假设、结论
│   ├─ main.py       # 或 notebook.ipynb
│   └─ out/          # 图与数据（可 gitignore）
└─ 002-fresnel/
```

**每个仿真必须写清假设。** 一个没有假设说明的仿真结果毫无价值。

## 写一个合格仿真脚本的检查清单

- [ ] 模型假设写清楚（标量/矢量、近轴/非近轴、相干/非相干）
- [ ] 单位统一（建议全部用 SI 或全部用 mm/mrad）
- [ ] 有解析解对照的，一定做对照
- [ ] 有网格/步长收敛性检查（把步长减半，结果是否稳定）
- [ ] 图有轴标签和单位
- [ ] 结论能一句话说清

## `lib/` 里最终应该攒下来的东西

这是本项目最有长期价值的资产之一。建议逐步积累：

- 光线追迹内核（球面、非球面、平面）
- 菲涅尔/夫琅禾费/角谱衍射传播
- 传输矩阵法薄膜计算器
- 高斯光束 ABCD 传播
- 常用拟合与误差传递工具
- 实验数据读取与标定工具（相机响应、功率计、光谱仪）
