"""001 复指数与波 —— 亲眼看到 cos(x) = Re(e^(ix))

对应 W01 的卡片 C18。
目的不是"学会写 Python"，而是让你用眼睛确认一件事：
**复指数取实部，就是一个真实的波。**

运行方式（不需要激活虚拟环境）：
    cd D:\\Optics_Master\\sim
    .\\.venv\\Scripts\\python.exe 001-complex-exponential\\main.py

看完图之后，回答脚本最后打印的两个问题。
"""

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 中文字体（sim/matplotlibrc 里也设了，这里再设一遍，保证从任何目录运行都不出方框）
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ------------------------------------------------------------------
# 1. 自变量：一个完整的波周期
# ------------------------------------------------------------------
x = np.linspace(0.0, 2 * np.pi, 400)

# ------------------------------------------------------------------
# 2. 同一个波，两种写法
# ------------------------------------------------------------------
cos_direct = np.cos(x)                          # 直接写三角函数
re_exp = np.real(np.exp(1j * x))                # 复指数取实部

sin_direct = np.sin(x)                          # 直接写正弦
sin_shifted = np.real(np.exp(1j * (x - np.pi / 2)))   # 正弦 = 相位落后 π/2 的复指数

# ------------------------------------------------------------------
# 3. 先用数字说话
#    本项目的规矩：没有数字的讨论不算数。
# ------------------------------------------------------------------
d_cos = np.max(np.abs(cos_direct - re_exp))
d_sin_bad = np.max(np.abs(sin_direct - re_exp))
d_sin_ok = np.max(np.abs(sin_direct - sin_shifted))

print("=== 数值检查（最大值差）===")
print("cos(x)  vs Re(e^(ix))          :", d_cos)
print("sin(x)  vs Re(e^(ix))          :", d_sin_bad)
print("sin(x)  vs Re(e^(i(x-pi/2)))   :", d_sin_ok)
print()
print("前两个数告诉你：cos 完全重合，sin 差得很远（约 1.414）。")
print("第三个数是 1e-16 量级，那是浮点数的机器精度，等价于 0。")

# ------------------------------------------------------------------
# 4. 画图
# ------------------------------------------------------------------
fig, ax = plt.subplots(2, 1, figsize=(9, 6.5), sharex=True)

ax[0].plot(x, cos_direct, lw=5, alpha=0.30, color="black", label="cos(x)")
ax[0].plot(x, re_exp, lw=1.6, ls="--", color="crimson", label="Re(e^(ix))")
ax[0].set_title("上：两条线完全重合 —— 复指数的实部就是 cos(x)")
ax[0].set_ylabel("振幅")
ax[0].legend(loc="upper right")

ax[1].plot(x, sin_direct, lw=5, alpha=0.30, color="black", label="sin(x)")
ax[1].plot(x, re_exp, lw=1.6, ls="--", color="crimson", label="Re(e^(ix))")
ax[1].set_title("下：sin(x) 与 Re(e^(ix)) 并不重合 —— 它落后 π/2")
ax[1].set_ylabel("振幅")
ax[1].set_xlabel("相位 x（弧度）")
ax[1].legend(loc="upper right")
ax[1].set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
ax[1].set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])

ax[1].annotate("", xy=(np.pi / 2, 1.15), xytext=(0.0, 1.15),
               arrowprops=dict(arrowstyle="<->", color="steelblue", lw=1.5))
ax[1].text(np.pi / 4, 1.22, "相差 π/2", ha="center", color="steelblue")
ax[1].set_ylim(-1.4, 1.45)

fig.tight_layout()
outdir = Path(__file__).resolve().parent / "out"
outdir.mkdir(parents=True, exist_ok=True)
outfile = outdir / "complex-exponential.png"
fig.savefig(outfile, dpi=150, bbox_inches="tight")
print()
print("图已保存：", outfile)

# ------------------------------------------------------------------
# 5. 看图之后要回答的问题（这才是 C18 的内容）
# ------------------------------------------------------------------
print()
print("=" * 62)
print("看完图，回答这两个问题：")
print("  1. 上图两条线为什么能完全重合？")
print("  2. 下图两条线不重合，差在哪里？用「相位」这个词说一遍。")
print()
print("想清楚之后，把答案给我——或者直接对着空气说一遍也行。")
print("=" * 62)
