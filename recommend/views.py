from bs4 import BeautifulSoup
from ninja import Router
import requests
router = Router()


def make_url_list(page_num, language):
    url_list = []

    for i in range(1, page_num + 1):
        url = f'https://www.udemy.com/courses/search/?src=ukw&q={language}'

        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

        lecture = requests.get(url, headers=headers)

        soup = BeautifulSoup(lecture.content, 'html.parser')

        lecture_list = soup.select('u124-popper-trigger--243 > div.course-card--main-content--2XqiY.course-card--has-price-text--1c0ze > h3 > a')
        lecture_list.extend(soup.select('u124-popper-trigger--243 > div.course-card--main-content--2XqiY.course-card--has-price-text--1c0ze > h3 > a'))
        print(lecture_list)
    for line in lecture_list:
        url_list.append(line.a.get('href'))
    return url_list


@router.post("")  # 이미 앞 url이 api/recommend/ 인 경우에 이 def 작동
def create_recommendations(request):

    url_list = make_url_list(1, 'python')

    print(url_list)
    # request body 추출& 가공 ninja API router것들 작성
    datas = []
    # 추천 ai 모듈 작동 - 문제
    result = []

    # 필요시 result 가공
    presenter = []

    return "recommendations.html"  # html 파일 열면서 ai 모듈 돌려서 나온 결과값들 함께 출력
