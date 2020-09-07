from bs4 import BeautifulSoup
import requests
import time

# 爬取104職缺
keyword = input("關鍵字(例：職稱、公司名、技能專長...) : ")
for page in range(1, 11):  # 爬取1-10頁
     # 用 requests 的 get 方法把網頁抓下來
    response = requests.get(
            "https://www.104.com.tw/jobs/search/?keyword="+keyword+"&order=1&page=" + str(page) + "&jobsource=2018indexpoc&ro=0")
    # 指定 lxml 作為解析器
    soup = BeautifulSoup(response.content, "lxml")
    blocks = soup.find_all("div", {"class": "b-block__left"})  # 職缺區塊
    for block in blocks:
        job = block.find("a", {"class": "js-job-link"})  # 職缺名稱
        if job is None:
            continue
        company = block.find_all("li")[1]  # 公司名稱
        salary = block.find("span", {"class": "b-tag--default"})  # 待遇

        print((job.getText(),) + (company.getText().strip(),) + (salary.getText(),))
