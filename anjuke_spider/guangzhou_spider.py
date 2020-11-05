import lxml.html
import urllib.request


def main():
    guangzhou_url = "https://gz.fang.anjuke.com/loupan/all/"
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }
    request_guangzhou = urllib.request.Request(guangzhou_url, headers=headers)
    guangzhou_response = urllib.request.urlopen(request_guangzhou)
    html_content = guangzhou_response.read().decode("utf-8")
    metree = lxml.html.etree
    parser = metree.HTML(html_content)
    # 获取广州所有区的地址
    area_url_list = parser.xpath("//div[@class='item-bd']/div[@class='item-list area-bd']/div[@class='filter']/a")
    # print(len(area_url_list))
    area_list = []
    area_page_list = []
    for list_1 in area_url_list:  # 遍历
        # area_name = list.xpath("./text()")  # 获取每个区的名字
        area_url = list_1.xpath("./@href")  # 获取每个区的链接
        area_url_str = ''.join(area_url)
        # 判断并去除标签中的‘广州周边’字段，剩下各个区地址
        if area_url_str != 'https://gz.fang.anjuke.com/loupan/guangzhouzhoubian/':
            area_list.append(area_url_str)
        else:
            continue
        # print(area_name, area_url_str)
    # print(area_list)
    for every_area_url in area_list:
        # 获取每个区拥有的页数
        request_area = urllib.request.Request(every_area_url, headers=headers)
        area_response = urllib.request.urlopen(request_area)
        area_content = area_response.read().decode("utf-8")
        metree = lxml.html.etree
        parser = metree.HTML(area_content)
        page_number = parser.xpath("//div[@class = 'pagination']/a[position() = last()-1]/text()")
        # print(page_number)
        page_number_str = ''.join(page_number)
        page_number_int = int(page_number_str)
        # print(page_number_str)
        for i in range(1, page_number_int+1):  # 遍历获取每个区所有页的地址
            area_page_url = every_area_url+'p'+str(i)+'/'
            # print(area_page_url)
            area_page_list.append(area_page_url)
    # print(area_page_list)
    all_house_list = []
    top_all_house_list = ["楼盘名", "楼盘地址", "所在地区", "房子户型", "房子面积", "房子价格"]
    all_house_list.append(top_all_house_list)
    for area_every_page_url in area_page_list:
        request_area_page = urllib.request.Request(area_every_page_url, headers=headers)
        area_page_response = urllib.request.urlopen(request_area_page)
        html_content = area_page_response.read().decode("utf-8")
        metree = lxml.html.etree
        parser = metree.HTML(html_content)
        # 获取一页下的所有楼盘信息
        area_page_all_div = parser.xpath("//div[@class='item-mod ']")
        # print(len(area_page_all_div))
        for i in area_page_all_div:
            house_list = []
            # 获取楼盘名
            house_name = i.xpath("./div[@class='infos']/a[@class='lp-name']/span[@class='items-name']/text()")
            house_name = ''.join(house_name)
            house_list.append(house_name)
            # 获取楼盘位置
            house_location = i.xpath("./div[@class='infos']/a[@class='address']/span[@class='list-map']/text()")
            house_location = house_location[0].replace('\xa0/\xa0', '').replace(',', '')
            house_location = ''.join(house_location)
            house_list.append(house_location)
            # 获取楼盘所在地区
            house_area_name = house_location[2:4]
            house_list.append(house_area_name)
            # 获取房子户型
            house_type = i.xpath(
                "./div[@class='infos']/a[@class='huxing']/span[position()>0][position()<last()]/text()")
            house_type = '/'.join(house_type)
            house_list.append(house_type)
            # 获取房子面积
            house_area = i.xpath("./div[@class='infos']/a[@class='huxing']/span[@class='building-area']/text()")
            house_area = ''.join(house_area)
            house_list.append(house_area)
            # 获取房子价格
            house_prices = i.xpath("./a[@class='favor-pos']/p[@class = 'price']/span/text()")
            house_prices = ''.join(house_prices)
            # house_price = house_prices.xpath('string(.)')
            # house_price = ''.join(str(s) for s in house_price)
            house_list.append(house_prices)
            # print(house_name, house_location, house_type, house_area)
            house_list = [el.replace('\xa0', ' ') for el in house_list]
            # print(house_list)
            all_house_list.append(house_list)
    print(all_house_list)
    print(len(all_house_list))
    """保存文件为CSV格式"""
    file = open("house_inf.csv", "w", encoding="utf-8")
    for j in all_house_list:
        a = ",".join(j)
        file.write(a + "\n")
    file.close()
    print("数据已导入成功！")


if __name__ == '__main__':
    main()
