# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import  re
import  requests
from pprint import pprint
import openpyxl

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
}
response = requests.get('https://book.douban.com/latest?icn=index-latestbook-all', headers = headers)
response.raise_for_status()
html = response.text
print(html)

book_name = re.findall('<a href="https://book.douban.com/subject/.*?">(.*?)</a>', html)
book_sub_url = re.findall('<a class="cover" href="(.*?)">', html)
book_img_url = re.findall('<img src="(.*?)"/>', html)
#book_comment = re.findall('<span class="font-small color-lightgray">(.*?)</span>', html, re.S)

book_author = re.findall('<p class="color-gray">(.*?)</p>', html, re.S)
#book_publish
#book_detail
pprint(book_author)

wb = openpyxl.Workbook()
w_sheet = wb.active
w_sheet.title = 'douban new book'
w_sheet['A1'] = '书名'
w_sheet['B1'] = '作者 出版社 时间'
w_sheet['C1'] = '书本地址'
w_sheet['D1'] = '缩略图地址'


#calculation the count of the list
list_count = len(book_name)
for count in range(1, list_count):
    w_sheet['A' + str(count+1)].value = book_name[count]
    w_sheet['B' + str(count+1)].value = book_author[count]
    w_sheet['C' + str(count+1)].value = book_sub_url[count]
    w_sheet['D' + str(count+1)].value = book_img_url[count]

print(book_name[1])





wb.save('test.xlsx')



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
