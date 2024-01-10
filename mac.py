from bs4 import BeautifulSoup
import requeｓts
import time
#リスト作る
mac_list = []
for i in range(1,17):
    time.sleep(1)
    url = f'https://www.itreview.jp/products/macos/reviews?page={i}'
    r=requests.get(url)

#文字化け少なく（意味なし？）
    r.encoding = r.apparent_encoding
#HTMLを解析する
    html_soup = BeautifulSoup(r.text, "html.parser")
#レビュースター名
    rv_span_list = html_soup.find_all(class_="search-text")
    for rv_tag in rv_span_list:
        rv_name = rv_tag.text.strip()
        mac_list.append(rv_name)
        print(rv_name)