import requests, time, schedule, datetime, base64
from flask import render_template
from flask import abort
from bs4 import BeautifulSoup


"""
token	string-	API 키값
s_date	stringyyyy-mm-dd	뉴스 송고일자 기준 검색범위 시작일.
e_date	stringyyyy-mm-dd	뉴스 송고일자 기준 검색범위 종료일.
keyword	string-	검색할 제목 키워드
page	int-	검색할 페이지 번호
limit	int-	페이지당 컨텐츠 갯수 (제한: 100)

"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'




def sanitize_html(title,id,pubdate,byline):
    get = [title,id,pubdate,byline]
    results =[]
    for i in get:
        i = BeautifulSoup(i, 'html5lib').get_text()
        results.append(i)
    return results




@app.route("/view/<idx>", methods=["GET"])
def newdetail(idx):
    key = "$2y$10$e/UnipeSQDzMTICFfZNXMO6X2qa36Wmx0b/b2O/HVwxToTkvt89Ym"
    url = "https://www.cryptohub.or.kr/api/v1/news"
    data = {"token": key,
            "s_date": "2021-08-20",
            "e_date": "2021-08-20",
            "keyword": "비트코인"}
    res = requests.post(url, data)
    if res.status_code == 200:
        results = res.json()["data"]
        wow = []
        if idx in results['id']:
            for i in res.json()["data"]:
                title = i['title']
                id = i['id']
                pubdate = i['pubdate']
                byline = i['byline']

                title1,id1,pubdate1,byline1 = sanitize_html(title,str(id),pubdate,byline)
                wow.append({title1, id1, pubdate, byline1})

    return wow

@app.route("/list", methods=["GET"])
def newlist():
    key = "$2y$10$e/UnipeSQDzMTICFfZNXMO6X2qa36Wmx0b/b2O/HVwxToTkvt89Ym"
    url = "https://www.cryptohub.or.kr/api/v1/news"
    data = {"token": key,
            "s_date": "2021-08-20",
            "e_date": "2021-08-20",
            "keyword": "비트코인"}
    res = requests.post(url, data)
    if res.status_code == 200:
        results = res.json()["data"]
        wow = []
        newwow = []
        for i in res.json()["data"]:
            title = i['title']
            id = i['id']
            pubdate = i['pubdate']
            byline = i['byline']

            title1, id1, pubdate1, byline1 = sanitize_html(title, str(id), pubdate, byline)
            if wow is not newwow:
                wow.append({title1, id1, pubdate, byline1})
    print(wow)
    return render_template("news.html", wow=wow)


            # id = res.json()["data"][i]['id']
            # a_list.append({'title':title, "id":id})
    #     return render_template("news.html", results=a_list)
    # else:
    #     # print(res.text)
    #     print("error")
    #     return abort(404)


if __name__ == "__main__":
    app.run(debug=True, port=9000)











# schedule.every(1).minute.do(newpost)
#
#
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# start =  str((datetime.datetime.today().strftime("%Y-%m-%d")))
# key = "$2y$10$e/UnipeSQDzMTICFfZNXMO6X2qa36Wmx0b/b2O/HVwxToTkvt89Ym"
#
# url ="https://www.cryptohub.or.kr/api/v1/news"
# data = {"token":key,
#         "s_date":"2021-08-19",
#         "e_date":"2021-09-20",
#         "keyword":"비트코인"}
# res = requests.post(url,data)
# now = int(datetime.datetime.today().strftime("%M"))"%Y-%m-%d %H:%M"