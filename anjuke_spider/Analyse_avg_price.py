import matplotlib.pyplot as plt
import pandas as pd


def main():
    file_name = "./house_inf.csv"
    price_data = pd.read_csv(file_name, encoding="utf-8")
    avg_price_list = []
    price_data.dropna()  # 去除空值

    data1 = price_data[~price_data['房子价格'].isin(['价格待定'])]  # 爬取的价格中有些为价格待定，所以需要去除这些信息，判断价格待定是否存在价格这一列中，再取反
    data1 = data1[(pd.to_numeric(data1['房子价格']) > 2000)]
    """取出每个区域信息，采用round函数保留两位小数"""
    d1 = data1[data1['所在地区'] == '增城']
    p1 = round(pd.to_numeric(d1['房子价格']).sum() / len(d1), 2)  # 计算价格均值
    avg_price_list.append(p1)  # 加入列表
    d2 = data1[data1['所在地区'] == '黄埔']
    p2 = round(pd.to_numeric(d2['房子价格']).sum() / len(d1), 2)
    avg_price_list.append(p2)
    d3 = data1[data1['所在地区'] == '南沙']
    p3 = round(pd.to_numeric(d3['房子价格']).sum() / len(d1), 2)
    avg_price_list.append(p3)
    d4 = data1[data1['所在地区'] == '番禺']
    p4 = round(pd.to_numeric(d4['房子价格']).sum() / len(d1), 2)
    avg_price_list.append(p4)
    d5 = data1[data1['所在地区'] == '花都']
    p5 = round(pd.to_numeric(d5['房子价格']).sum() / len(d1), 2)
    avg_price_list.append(p5)
    d6 = data1[data1['所在地区'] == '天河']
    p6 = round(pd.to_numeric(d6['房子价格']).sum() / len(d1), 2)
    avg_price_list.append(p6)
    d7 = data1[data1['所在地区'] == '白云']
    p7 = round(pd.to_numeric(d7['房子价格']).sum() / len(d1), 2)
    avg_price_list.append(p7)
    d8 = data1[data1['所在地区'] == '海珠']
    p8 = round(pd.to_numeric(d8['房子价格']).sum() / len(d1), 2)
    avg_price_list.append(p8)
    d9 = data1[data1['所在地区'] == '从化']
    p9 = round(pd.to_numeric(d9['房子价格']).sum() / len(d1), 2)
    avg_price_list.append(p9)
    d10 = data1[data1['所在地区'] == '荔湾']
    p10 = round(pd.to_numeric(d10['房子价格']).sum() / len(d1), 2)
    avg_price_list.append(p10)
    d11 = data1[data1['所在地区'] == '越秀']
    p11 = round(pd.to_numeric(d11['房子价格']).sum() / len(d1), 2)
    avg_price_list.append(p11)

    """广州各区域新房均价柱状图"""
    # 创建画布中的X轴数据内容
    area_list = ["增城", "黄埔", "南沙", "番禺", "花都", "天河", "白云", "海珠", "从化", "荔湾", "越秀"]

    x = area_list
    y = avg_price_list
    # 设置正常显示字符
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(25, 10), dpi=100)  # 设置画布大小
    plt.bar(x, y, label="各区域新房均价")
    plt.legend()

    # 旋转x轴标签
    plt.xticks(rotation=0)
    # 调整字体大小
    plt.tick_params(axis='x', labelsize=8)
    plt.title("广州各个区的新房均价")
    plt.xlabel("地区名称")
    plt.ylabel("价格（元/平方米）")

    # 让数据在柱形顶端显示出来
    index = 0
    for i in range(0, len(area_list)):
        plt.text(area_list[index], avg_price_list[index], avg_price_list[index], color='r')
        index += 1
    plt.show()


if __name__ == '__main__':
    main()
