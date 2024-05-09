from flask import Flask,render_template,request

app = Flask(__name__)
import requests
from bs4 import BeautifulSoup
import time
import urllib
#엑셀쓰기위한 준비
from  openpyxl import Workbook
write_wb = Workbook()
write_ws = write_wb.active
import re

from selenium import webdriver
@app.route('/')
def hello_wolrd():
    return render_template("index.html")
@app.route("/result",methods=['post'])
def result():
    keyword=request.form['input1']
    page=request.form['input2']
    daum_list=[]
    for num in range(1,int(page)+1):
        url = "https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=" + keyword + "&p=" + str(num)
        req = requests.get(url)
        soup = BeautifulSoup(req.text,"html.parser")
        print(url)
        for i in soup.find_all("a",class_="link_major"):
            print(i.text)
            daum_list.append(i.text)
    for i in range(1,len(daum_list)+1):
        write_ws.cell(i,1,daum_list[i-1])#worksheet의 cell에 추가
    write_wb.save("static/result.xlsx")#workbook 저장

    return render_template('result.html',daum_list=daum_list)
@app.route('/naver_shopping',methods=['POST'])
def naver_search():
    search=request.form['input3']
    print(search)
    search_list=[]
    search_list_src=[]
    driver=webdriver.Chrome()
    #3초 기다려주기, 웹페이지 로딩까지
    driver.implicitly_wait(3)
    driver.get("https://search.shopping.naver.com/search/all?query=" + search)
    #스크롤 내리기
    dict1={}
    y=1000
    for timer in range(0,5):
        driver.execute_script("window.scrollTo(0, "+str(y)+")")
        y=y+1000
        time.sleep(1)
    soup = BeautifulSoup(driver.page_source,"html.parser")
    select = "#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx"
    cnt = 0
    result=[]
    list_in=[]
    for i in soup.select(select)[0].find_all("div",class_="product_item_MDtDF"):
        if i.text is not None:
            dict1['data'+str(cnt)]=[]
            for j in i.text.split(" "):
                if j.strip() != ':':#공백이 아닐 경우만 추가
                   list_in.append(j)
        result.append(list_in)
    driver.close()
    time.sleep(2)
    return render_template("shopping.html",
                           data=result  )
def naver_filter(x):
     return x not in ['https://news.naver.com/']
@app.route('/naver_image',methods=['POST'])
def img_update():
    img_results=[]
    url = "https://news.naver.com/"
    img_list=[]
    cnt=0
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    naver_list = ['https://news.naver.com/']
    # 모든 img태그를 검색해 링크를 구한다
    for element in soup.find_all("img"):
        src = element.get('src')
        # print(src)
        # 절대url을 만들어 이미지 데이터를 구한가
        image_url = urllib.parse.urljoin(url, src)
        print(cnt,image_url)
        if image_url in naver_list  :
            cnt+=1
            if cnt>10:break
        img_results.append(image_url)


        time.sleep(1)
    res=list(filter(naver_filter ,img_results))
    print(res)
    return render_template("naverimg.html",data=res)
if __name__=="__main__":
    app.run()
