from bs4 import BeautifulSoup
import requeｓts
import time
#リスト作る
win_list = []

for i in range(1,71):
  time.sleep(1)
  url = f'https://www.itreview.jp/products/windows-10/reviews?page={i}'
  r=requests.get(url)
#文字化け少なくする
  r.encoding = r.apparent_encoding
#ページのHTMLを解析
  html_soup = BeautifulSoup(r.text, "html.parser")
  #レビュースター名
  rvw_span_list = html_soup.find_all(class_="search-text")
  for rvw_tag in rvw_span_list:
    rvw_name = rvw_tag.text.strip()
    win_list.append(rvw_name)
    print(rvw_name)