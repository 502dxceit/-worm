import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import pandas
import main
from collections import Counter


# df = pandas.read_csv("调研报告.csv")
# a = jieba.lcut(str(df['0']))


def word_cloud():
    main_class = main.main()
    a = []
    for i in main_class.head_dict.keys():
        df = pandas.read_csv(i + ".csv")
        a += jieba.lcut(str(df['0']))

    b = str(a)[1:-1].replace(",", '').replace('\'', '').replace('，', '').replace('n', '').replace('的', '').replace('关于',
                                                                                                                   '').replace(
        '报告', '')
    b = b.replace('如何', '').replace('与', '').replace('Length', '').replace('Name', '').replace('dtype', '').replace(
        'object', '').replace('Legth', '')

    print(b)
    print(b.__len__())
    wc = WordCloud(font_path="方正粗黑宋简体.ttf").generate(b)

    plt.imshow(wc)
    plt.axis('off')
    plt.show()


def anlysis(baoliu1=False):
    # baoliu1 保留为1的词？
    pop_list = ['0', ' ', '\n', '2', '，', '3', '"', '...', '【', '】', 'Name', ':', ',', 'Length', 'dtype', 'object',
                '：', '“', '”', '的', '号', '-', '223', '222', '1', '4']
    main_class = main.main()
    a = []
    for i in main_class.head_dict.keys():
        df = pandas.read_csv(i + ".csv")
        a += jieba.lcut(str(df['0']))
        print(i)
    arra = Counter(a)
    arr = {}
    for i, j in arra.items():
        if i not in pop_list:
            arr[i] = j
    if not baoliu1:
        arr2 = {}
        for i, j in arr.items():
            if arr[i] != 1:
                arr2[i] = j
        return arr2

    return arr


def abs_ayl():
    # 查一查abs里元素个数（关键词统计）
    df = pandas.read_csv("abs.csv")

    resa = []
    for i in df["0"]:
        resa.append(i)
    res = Counter(resa)
    wc = WordCloud(font_path="方正粗黑宋简体.ttf").generate(str(res).replace(",", ''))
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig("abs.png", dpi=3000)
    plt.show()

    print(res)


def writer():
    # Count writer
    df = pandas.read_csv("writer.csv")
    resa = []
    for i in df["0"]:
        resa.append(i)
    res = Counter(resa)
    print(res)


if __name__ == '__main__':
    # k = anlysis()
    # df = pandas.DataFrame(columns=["item", "count"], index=[])
    # df["item"] = k.keys()
    # df['count'] = k.values()
    # df2 = df.sort_values(by="count", ascending=False)
    # # print(df2)
    # df2 = df2.reset_index()
    # df3 = df2.loc[:30]
    # df4 = df2.loc[30:60]
    # print(df3)
    # df2.to_csv("count.csv", encoding="utf-8-sig")
    # # plt.plot(df3["item"], df3["count"])
    # #
    # # plt.show()
    # abs_ayl()
    writer()
