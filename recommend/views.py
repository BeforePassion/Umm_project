from bs4 import BeautifulSoup
from ninja import Router
import requests
router = Router()


def make_urllist(page_num, language):
    urllist = []

    for i in range(1, page_num + 1):
        url = f'https://www.udemy.com/courses/search/?src=ukw&q={language}'

        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

        news = requests.get(url, headers=headers)

        soup = BeautifulSoup(news.content, 'html.parser')

        news_list = soup.select('u124-popper-trigger--243 > div.course-card--main-content--2XqiY.course-card--has-price-text--1c0ze > h3 > a')
        news_list.extend(soup.select('u124-popper-trigger--243 > div.course-card--main-content--2XqiY.course-card--has-price-text--1c0ze > h3 > a'))
        print(news_list)
    for line in news_list:
        urllist.append(line.a.get('href'))
    return urllist


@router.post("")  # 이미 앞 url이 api/recommend/ 인 경우에 이 def 작동
def create_recommendations(request):

    urllist = make_urllist(1, 101, 20220319)

    print(urllist)
    # request body 추출& 가공 ninja API router것들 작성
    datas = []
    # 추천 ai 모듈 작동 - 문제
    result = []

    # 필요시 result 가공
    presenter = []

    return "recommendations.html"  # html 파일 열면서 ai 모듈 돌려서 나온 결과값들 함께 출력
