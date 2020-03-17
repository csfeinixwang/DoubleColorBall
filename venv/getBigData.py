import requests
from lxml import etree
import csv
#查找抓取的网站的地址
url=""

def save_csv(path,Nowdate="2020-3-13-1"):
    import csv
    with open('no.1-%s.csv' % (Nowdate), 'w') as f:
        writer = csv.writer(f)
        # 将列表的每条数据依次写入csv文件， 并以逗号分隔
        writer.writerows(path)
        print("写入完成....")


def get_data(url = "http://datachart.500.com/ssq/history/newinc/history.php?start=00001&end=20010"):
    response=requests.get(url)
    response=response.text
    selector=etree.HTML(response)
    result=[]
    # for i in selector.xpath('//tr[@class="t_tr1"]'):
    #     datetime = i.xpath('td/text()')[0]
    #     red = i.xpath('td/text()')[1:7]
    #     blue = i.xpath('td/text()')[7]
    #     print(datetime, red, blue)

    for i in selector.xpath('//tr[@class="t_tr1"]'):
        period=i.xpath('td/text()')[0]
        # print(period)
        blue=i.xpath('td/text()')[1:7]
        red=i.xpath('td/text()')[7]
        result.append((period,blue,red))
        # print(result)
    return result

if __name__=='__main__':
    print('start')
    rets=get_data()
    save_csv(rets)
