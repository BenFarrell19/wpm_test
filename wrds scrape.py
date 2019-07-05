import requests, re

r = requests.get('https://cdn.livechatinc.com/gtt/app.3.8.min.js')
p = re.compile(r'e\.exports={words:\[(.*?)\]')
words = p.findall(r.text)
print(words)
w = open("wrds_list.txt", "w")
