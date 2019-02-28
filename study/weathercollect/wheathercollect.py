from bs4 import BeautifulSoup
import random
import requests
import socket
import time
import http.client
import csv


def geturl():
    city = {
        "海口": "101310101",
        "三亚": "101310201",
        "苏州": "101190401",
        "郑州": "101180101"
    }
    for k in city:
        print(k)
    city_name = input("请输入城市名称：")
    city_number = city[city_name]
    weather_url = "http://www.weather.com.cn/weather/%s.shtml" % city_number
    return weather_url


def getHtml(url, data=None):
    """
        模拟浏览器来获取网页的html代码

    """
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
    }
    # 随机获得一个超时时间
    timeout = random.choice(range(80, 180))
    while True:
        try:
            req = requests.get(url, headers=header, timeout=timeout)
            req.encoding = "utf-8"
            break
        except socket.timeout as e:
            print("3:", e)
            time.sleep(random.choice(random.choice(range(8, 15))))
        except socket.error as e:
            print("4:", e)
            time.sleep(random.choice(random.choice(range(20, 60))))
        except http.client.BadStatusLine as e:
            print("5:", e)
            time.sleep(random.choice(random.choice(range(30, 80))))
        except http.client.IncompleteRead as e:
            print("6:", e)
            time.sleep(random.choice(random.choice(range(5, 15))))
    return req.text


def getData(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")
    body = bs.body
    #print(body)
    data = body.find("div", {"id": "7d"})
    ul = data.find("ul")
    li = ul.find_all("li")
    '''
    业务处理
    '''
    for day in li:
        temp = []
        date = day.find("h1").string
        temp.append(date)
        inf = day.find_all("p")
        temp.append(inf[0].string)
        if inf[1].find("span") is None:
            temperature_high = None
        else:
            temperature_high = inf[1].find("span").string  # 最高气温
            temperature_high = temperature_high.replace("℃", "")
        temperature_lower = inf[1].find("i").string  # 找到最低温
        temperature_lower = temperature_lower.replace("℃", "")
        temp.append(temperature_high)
        temp.append(temperature_lower)
        final.append(temp)  # 将temp添加到final中
    return final


def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


if __name__ == "__main__":
    url = geturl()
    print("将要获取的网址为", url)
    html = getHtml(url)
    #print("网页内容为：" + html)
    result = getData(html)
    write_data(result, "weather.csv")
    for i in result:
        print(i)