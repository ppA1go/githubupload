import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

url = "https://www.irasutoya.com/search/label/%E5%BC%95%E8%B6%8A%E3%81%97"

html = requests.get(url)
soup=BeautifulSoup(html.content,"html.parser")

out_folder = Path("download3")
out_folder.mkdir(exist_ok=True)
cnt=0
#모든 img태그를 검색해 링크를 구한다
for element in soup.find_all("img"):
    src=element.get('src')
    # print(src)
    # 절대url을 만들어 이미지 데이터를 구한가
    image_url = urllib.parse.urljoin(url, src)
    imgdata = requests.get(image_url)
    # print(imgdata)

    # url에서 마지막에있는 파일명을 추출하고 저장 폴더명과 연결
    filename = image_url.split("/")[-1]
    outpath = out_folder.joinpath(filename)

    str1="download3//"+str(cnt)+".jpg"
    cnt+=1
    # 이미지 데이터를 파일에 저장
    with open(str1, mode="wb") as f:
        f.write(imgdata.content)

    time.sleep(1)