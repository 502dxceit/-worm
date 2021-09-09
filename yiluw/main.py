import requests
import pandas
import time
from lxml import etree


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


if __name__ == '__main__':
    a = main()

    a.requests()
