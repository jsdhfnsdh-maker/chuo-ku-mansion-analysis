from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

rows = []

for page in range(1, 11):
    url = f"https://quotes.toscrape.com/page/{page}/"
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    for q in soup.select(".quote"):
        text = q.select_one(".text").get_text()
        author = q.select_one(".author").get_text()
        rows.append({"text": text, "author": author})
    time.sleep(1)

df = pd.DataFrame(rows)
df.to_csv("my_quotes2.csv", index=False, encoding="utf-8-sig") 