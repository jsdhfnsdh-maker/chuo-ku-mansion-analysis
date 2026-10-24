import pandas as pd

def clean(df):
    #生データを整えて、㎡単価と築年数の列を足したDataFrameを返す。
    df = df.copy()
    df["BuildingYear"] = pd.to_numeric(df["BuildingYear"].str.replace("年", ""), errors="coerce")
    df["UnitPriceM2"]=df["TradePrice"]/df["Area"] #㎡単価: TradePrice / Area（取引価格 ÷ 面積）
    df["TradeYear"] = pd.to_numeric(df["Period"].str[:4], errors="coerce")
    df["築年数"] = df["TradeYear"] - df["BuildingYear"]
    #df["築年数"]=df["Period"]-df["BuildingYear"]
    return df

def select_mansion(df):
    #中古マンションだけに絞る。
    return df[df["Type"] == "中古マンション等"]

if __name__ == "__main__":
    df = clean(pd.read_csv("raw_trades.csv"))
    mansion = select_mansion(df)

    print(len(mansion))
    print(mansion["UnitPriceM2"].describe())

    df.to_csv("clean_trades.csv", index=False, encoding="utf-8-sig")
    mansion.to_csv("clean_mansion.csv", index=False, encoding="utf-8-sig")
