import json
import requests

# 获取远程JSON
url = "https://jsd.268682.xyz/gh/Kemeow0815/friends@output/v2/data.json"
response = requests.get(url)
data = response.json()

# 转换格式并输出
for item in data["content"]:
    print(f"{item['title']},{item['url']}")

# 保存到 link.csv
with open("link.csv", "w", encoding="utf-8") as f:
    for item in data["content"]:
        f.write(f"{item['title']},{item['url']}\n")