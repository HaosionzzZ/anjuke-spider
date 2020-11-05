import matplotlib
import matplotlib.pyplot as plt
import csv


def main():
    with open("house_inf.csv", "r", encoding="utf-8") as house_type_file:
        reader = csv.reader(house_type_file)
        type_list = []
        for row in reader:  # 遍历获取CSV文件中的第2列
            type_list.append(row[2])
        del type_list[0]
        # print(type_list)
        """统计广州新房各类型数量"""
        type_str = ''
        for type1 in type_list:
            type_str += type1+'/'
        # print(type_str)
        type_count_list = []
        one_count = type_str.count('1室')
        type_count_list.append(one_count)
        two_count = type_str.count('2室')
        type_count_list.append(two_count)
        three_count = type_str.count('3室')
        type_count_list.append(three_count)
        four_count = type_str.count('4室')
        type_count_list.append(four_count)
        five_count = type_str.count('5室')
        type_count_list.append(five_count)
        # print(type_count_list)

        """新房类型的饼状图"""
        plt.figure(figsize=(25, 10), dpi=100)
        matplotlib.rcParams['font.family'] = 'SimHei'
        matplotlib.rcParams['font.sans-serif'] = 'SimHei'
        labels = ["1室", "2室", "3室", "4室", "5室"]
        type_data = type_count_list
        explodes = [0, 0.1, 0.1, 0, 0]
        plt.axes(aspect=1)
        plt.pie(x=type_data, labels=labels, explode=explodes, autopct="%.1f%%", shadow=True)
        plt.title("广州新房类型占比图")
        plt.legend(loc="upper right")
        plt.show()


if __name__ == '__main__':
    main()
