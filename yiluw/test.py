import requests
from lxml import etree

# response = requests.get(url="http://yl.oneroadedu.com/m")
# # tid max =85 http://yl.oneroadedu.com/m/news.php?tid=85&page=1
# print(response)
# with open("out.html", "w", encoding="utf-8") as out:
#     out.write(response.text)
#
# HTML = etree.HTML(response.text)
# # inytms box-pad
# print(HTML.xpath)
# res = HTML.xpath('//ul//li//a//text()')
# print(res)
# print(HTML.xpath('//ul//li//a//@href'))
# # print(HTML.xpath('//div[@class ="inytms box-pad"]//li//a/@href')) # <a href>

import random
print(random.random()+1)
