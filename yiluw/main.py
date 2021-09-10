import requests
import pandas
import time
from lxml import etree
import random
import re

class main:

    def __init__(self):
        self.base_url = "http://yl.oneroadedu.com/m"
        self.head_dict = {
            "权威资讯": 85,
            "新业态新模式": 47,
            "新消费洞察": 48,
            "新技术前瞻": 49,
            "跨境电商": 52,
            "专家视野": 55,
            "政策动态": 57,
            "案例库": 58,
            "调研报告": 59,
            "数字化转型": 84

        }

    def url(self, tid, page):
        v_url = "http://yl.oneroadedu.com/m/news.php?tid=" + str(tid) + "&page=" + str(page)
        return v_url

    def requests(self):
        totel_count = 0
        for i in self.head_dict.keys():
            list_ = []
            for j in range(1, 100):
                print(totel_count)
                time.sleep(1)
                response = requests.get(self.url(self.head_dict[i], j))
                html = etree.HTML(response.text)
                data = html.xpath('//div[@class ="inytms box-pad"]//li//a//p//text()')
                list_ += data
                totel_count += 1
                if data.__len__() == 0:
                    break
            pandas.DataFrame(list_).to_csv(i + ".csv", encoding="utf_8_sig")

    def measure(self):
        length = 0
        for i in self.head_dict.keys():
            length += pandas.read_csv(i + ".csv").__len__()
        return length

    def requests2(self):
        # 获取并保存可以get到的文章id
        count = 0
        list_good = []
        for i in range(10000):
            time.sleep(random.random()+1)
            response = requests.get("http://yl.oneroadedu.com/m/news_show.php?id=" + str(i))
            html = etree.HTML(response.text)
            if html.xpath('//div') != []:
                count += 1
                list_good.append(i)
            print(i+1,count)
        print("总文章数{}".format(count))
        return list_good

    def abstract_sta(self):
        # 关键词，作者统计
        gs = pandas.read_csv("good_id.csv")["0"]
        abslist = []
        writerlist = []
        count = 0
        b = gs.__len__()
        for i in gs:
            time.sleep(random.uniform(0.02, 0.5))
            response = requests.get("http://yl.oneroadedu.com/m/news_show.php?id=" +str(i))
            html = etree.HTML(response.text)
            writer = html.xpath("//div[@class = 'pojde-til']//span//text()")
            writera = re.findall(r'：(.*)\\u', str(writer))[0]
            abs = html.xpath("//div[@class = 'pojde-gj']//span//text()")
            if "、" in writera:
                writerlist += writera.split("、")
            else:
                writerlist += [writera]
            # print(writerlist, abs)
            abslist += abs
            count +=1
            print("{}/{}".format(count,b))

        pandas.DataFrame(writerlist).to_csv("writer.csv", encoding="utf-8-sig")
        pandas.DataFrame(abslist).to_csv("abs.csv", encoding="utf-8-sig")



if __name__ == '__main__':
    a = main()

    # li = a.requests2()
    # print(a.measure())
    # pandas.DataFrame(li).to_csv("good_id.csv")
    a.abstract_sta()
