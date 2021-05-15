from selenium import webdriver
import requests
from lxml import etree
# def chrome_drive():
# note_name = input('请输入书名:')
note_name = '大主宰'
# driver = webdriver.Chrome()
# data = {
#     'searchkey': '大主宰'
# }
# response = requests.post(url='http://www.xbiquge.la/modules/article/waps.php',
#                          data=data)
# response.encoding='utf-8'
# print(response.text)
# exit(0)
url = 'http://www.xbiquge.la/'
# driver.get(url=url)

# driver.find_element_by_xpath('//*[@id="wd"]').send_keys(note_name)
# driver.find_element_by_xpath('//*[@id="sss"]').click()
# search_result_page = driver.page_source
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Cookie': '_abcde_qweasd=0; bdshare_firstime=1619762655741; UM_distinctid=1792171b4e96f-0ec83424c7f6cf-d7e1739-1bcab9-1792171b4eac9e; CNZZDATA1253551727=1278126802-1619760676-%7C1619760676; cscpvrich9192_fidx=1; cscpvcouplet9193_fidx=1; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1619762656,1619762974,1620262109,1620610509; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1620610509'
}
data = {
    'searchkey': note_name
}
search_result_page = requests.post(url='http://www.xbiquge.la/modules/article/waps.php', data=data, headers=headers)
search_result_page.encoding='utf-8'
print(search_result_page.text)
search_result_page_tree = etree.HTML(search_result_page.text)
note_list_tr = search_result_page_tree.xpath('//*[@id="checkform"]/table//tr')
print(note_list_tr)
element = note_list_tr[1]
note_list_url = element.xpath('./td//a/@href')[0]
note_list_title = element.xpath('./td//a/text()')[0]
note_list_author = element.xpath('./td[3]/text()')[0]
# print(note_list_url, note_list_title, note_list_author)

# user_agent = driver.execute_script("return navigator.userAgent")

# print(headers)
response = requests.get(url=note_list_url, headers=headers)
response.encoding = 'utf-8'
# print(response.text)
menu_page = response.text
menu_page_tree = etree.HTML(menu_page)
note_url_dl = menu_page_tree.xpath('//*[@id="list"]/dl')
for element in note_url_dl:
    note_url = element.xpath('./dd/a/@href')
    # note_title_list = element.xpath('./dd/a/text()')
    # dic_note = enumerate(note_title_list)
    # print(dict(dic_note))
    # num = list(dic_note.keys())[list(dic_note.values()).index("第九十章 玩战术（求保底月票）")]
    # print(num)
    # print(note_url[-1])
    for url in note_url[:10]:
        url = 'http://www.xbiquge.la'+url
        print(url)
        response_note = requests.get(url=url, headers=headers)
        # print()
        response_note.encoding = 'utf-8'
        # print(response_note.text)
        # print(response.encoding)
        # response.encoding = response.apparent_encoding
        # print(response.encoding)
        # print(response_note.text)
        note_tree = etree.HTML(response_note.text)
        notes = note_tree.xpath('//*[@id="content"]/text()')
        # print(title)
        title = note_tree.xpath('//div[@class="bookname"]/h1/text()')[0]
        print(title)
        # driver.get(url)
        note_title = note_list_title + '.txt'
        with open(note_title,'a+', encoding='utf-8') as f:
            f.write(title + '\n')
            for i in notes:
                note = i.replace(u'\xa0', '')
                f.write(' ' + note + '\n')

# response = requests.get(url='http://www.xbiquge.la/0/8/7011298.html', headers = headers)
# if response.status_code == 404:
#     print('ok')

# print(note_list_tr)
# print(search_result_page_tree)
# print(search_result_page)
