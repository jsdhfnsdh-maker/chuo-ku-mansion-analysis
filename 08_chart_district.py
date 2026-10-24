#地区別の㎡単価を、グラフにする
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Meiryo"

df = pd.read_csv("clean_mansion.csv")

# 1. 地区ごとの件数と中央値を出す(my_clean.py と同じ)
by_district = df.groupby("DistrictName")["UnitPriceM2"].agg(["count", "median"])

# 2. 件数が10以上の地区に絞る
big = by_district[by_district["count"] >= 10]

# 3. ㎡単価を「万円」にして、安い順に並べる
data = (big["median"] / 10000).sort_values()

# 4. 横棒グラフにして保存する
ax = data.plot(kind="barh")
ax.set_xlabel("㎡単価の中央値(万円)")
ax.set_ylabel("")
plt.tight_layout()
plt.savefig("district_price.png", dpi=150)
