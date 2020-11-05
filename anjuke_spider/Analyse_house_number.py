import matplotlib.pyplot as plt
import csv


def main():
    with open("house_inf.csv", "r", encoding="utf-8") as house_number_file:
        reader = csv.reader(house_number_file)
        headers_row = next(reader)
        location_list = []
        for row in reader:  # 遍历获取CSV文件中的第一列
            location_list.append(row[1])
        # print(location_list)
        """统计广州各区楼盘的数量"""
        locate_zengceng_counts = 0
        locate_huangpu_counts = 0
        locate_nansha_counts = 0
        locate_panyu_counts = 0
        locate_huadu_counts = 0
        locate_tianhe_counts = 0
        locate_baiyun_counts = 0
        locate_haizhu_counts = 0
        locate_conghua_counts = 0
        locate_liwan_counts = 0
        locate_yuexiu_counts = 0
        for list_1 in location_list:
            if '增城' in list_1:
                locate_zengceng_counts += 1
            elif '黄埔' in list_1:
                locate_huangpu_counts += 1
            elif '南沙' in list_1:
                locate_nansha_counts += 1
            elif '番禺' in list_1:
                locate_panyu_counts += 1
            elif '花都' in list_1:
                locate_huadu_counts += 1
            elif '天河' in list_1:
                locate_tianhe_counts += 1
            elif '白云' in list_1:
                locate_baiyun_counts += 1
            elif '海珠' in list_1:
                locate_haizhu_counts += 1
            elif '从化' in list_1:
                locate_conghua_counts += 1
            elif '荔湾' in list_1:
                locate_liwan_counts += 1
            else:
                locate_yuexiu_counts += 1
        area_house_counts = []
        area_house_counts.append(locate_zengceng_counts)
        area_house_counts.append(locate_huangpu_counts)
        area_house_counts.append(locate_nansha_counts)
        area_house_counts.append(locate_panyu_counts)
        area_house_counts.append(locate_huadu_counts)
        area_house_counts.append(locate_tianhe_counts)
        area_house_counts.append(locate_baiyun_counts)
        area_house_counts.append(locate_haizhu_counts)
        area_house_counts.append(locate_conghua_counts)
        area_house_counts.append(locate_liwan_counts)
        area_house_counts.append(locate_yuexiu_counts)
        # print(area_house_counts)

        """广州各区域新房数量柱状图"""
        # 创建画布中的X轴数据内容
        area_list = ["增城", "黄埔", "南沙", "番禺", "花都", "天河", "白云", "海珠", "从化", "荔湾", "越秀"]

        x = area_list
        y = area_house_counts
        # 设置正常显示字符
        plt.rcParams['font.sans-serif'] = 'SimHei'
        plt.rcParams['axes.unicode_minus'] = False

        plt.figure(figsize=(25, 10), dpi=100)  # 设置画布大小
        plt.bar(x, y, label="各区域房源数量")
        plt.legend()

        # 旋转x轴标签
        plt.xticks(rotation=0)
        # 调整字体大小
        plt.tick_params(axis='x', labelsize=8)
        plt.title("广州各区域新房源数量")
        plt.xlabel("地区名称")
        plt.ylabel("房源数量")

        # 让数据在柱形顶端显示出来
        index = 0
        for i in range(0, len(area_list)):
            plt.text(area_list[index], area_house_counts[index], area_house_counts[index], color='r')
            index += 1
        plt.show()


if __name__ == '__main__':
    main()
