# from django.http import HttpResponse
from django.shortcuts import render
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import pandas as pd
# import numpy as np
import csv
import random
from collections import defaultdict
from itertools import chain

from ninja import Router

import requests
router = Router()


# 언어 선택을 여러개 해주었을때 전체 강의 리스트에서 해당 언어별 강의를 추천
# @router.get("")
# def make_recommend_courses_list(request):  # 강의.csv 만들기
#     if request.method == 'GET':  # 페이지 접근
#
#         # parts = []
#         img_list = []
#         title_list = []
#         url_list = []
#         language_type_list = []
#
#         # review_language = ReviewModel.objects.filter(mentee_id=pk)
#         # parts.append(review_language)  # 리뷰에서 선정된 언어들을 parts list에 추가해준다.
#
#         parts = ['python', 'data-analysis', 'javascript', 'html-css',
#                  'mobile-app', 'java', 'front-end', 'back-end',
#                  'game-dev', 'machine-learning', 'algorithm'
#                  ]
#
#         # 강의를 크롤링 해올 url 가져오기
#         for part in parts:
#             url = f'https://www.inflearn.com/courses?level=level-1%2Clevel-2&order=seq&skill={part}'
#             # url_list.append(url)
#
#             # img list by bs4
#             r = requests.get(url)
#             html_data = r.text
#             soup = BeautifulSoup(html_data, 'html.parser')
#             for item in soup.find_all('div', class_='card-image'):
#                 # print(item)
#                 if item.find('img'):
#                     # print('img',item.find('img')['src'])
#                     img_list.append(item.find('img')['src'])
#                 elif item.find('video'):
#                     # print('video', item.find('video').find('source')['src'])
#                     img_list.append(item.find('video').find('source')['src'])
#
#             # for selenium
#             options = Options()
#             options.add_argument("--headless")
#             assert options.headless  # Operating in headless mode > chrome(browser를 띄우지 않고 작업가능)
#             browser = Chrome(options=options)
#
#             browser.get(url)
#
#             for i in range(1, 25):
#                 # 제목 list by selenium
#                 courses = browser.find_elements(By.XPATH,
#                                                 f'/html/body/div[1]/main/section/div/div/div/main/div[3]/div/div[{i}]/div/a/div[2]/div[1]')
#                 for course in courses:
#                     # print(course.text)
#                     title_list.append(course.text)
#
#                 # 강의 url list by selenium
#                 course_links = browser.find_elements(By.XPATH,
#                                                      f'/html/body/div[1]/main/section/div/div/div/main/div[3]/div/div[{i}]/div/a')
#                 for course_link in course_links:
#                     href = course_link.get_attribute('href')
#                     url_list.append(href)
#
                # headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
                #
                # lecture = requests.get(url, headers=headers)
                #
                # soup = BeautifulSoup(lecture.content, 'html.parser')
                #
                # lecture_list = soup.select('u124-popper-trigger--243 > div.course-card--main-content--2XqiY.course-card--has-price-text--1c0ze > h3 > a')
                # lecture_list.extend(soup.select('u124-popper-trigger--243 > div.course-card--main-content--2XqiY.course-card--has-price-text--1c0ze > h3 > a'))
                # print(lecture_list)
#
#             data = {
#                 'img': img_list,
#                 'title': title_list,
#                 'url': url_list,
#                 'language_type': language_type_list
#             }
#
#         data_frame = pd.DataFrame(data, columns=['img', 'title', 'url', 'language_type'])
#
#         data_frame.to_csv('csv/' + f'courses_list' + '.csv', encoding="utf-8-sig")
#
#         browser.close()
#             # for line in lecture_list:
#             #     url_list.append(line.a.get('href'))
#         return HttpResponse('create model ~')


@router.get("")  # 이미 앞 url이 api/recommend/ 인 경우에 이 def 작동
def get_recommendations(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            # 멘티가 선택한 관심 언어 list
            selected = ['java', 'python', 'javascript']
            # review_language = ReviewModel.objects.filter(mentee_id=pk)  # review app이랑 콜라보 필요
            # selected.append(review_language)

            class Course:

                def __init__(
                        self,
                        id_,
                        img,
                        title,
                        url,
                        language_type,
                ):
                    self.id_ = id_
                    self.img = img
                    self.title = title
                    self.url = url
                    self.language_type = language_type

            with open('./courses_list.csv', mode='r') as csv_file:
                courses_list = csv.reader(csv_file)

                next(courses_list)

                courses_list = [Course(
                    id_=course[0],
                    img=course[1],
                    title=course[2],
                    url=course[3],
                    language_type=course[4],
                ) for course in courses_list]

            language_type_dict = defaultdict(list)
            for course in courses_list:
                language_type_dict[course.language_type].append(course)

            # 유저가 선택한 언어별 강의 리스트를 하나로 취합
            target = list(chain(*(language_type_dict[s] for s in selected)))

            # 취합한 리스트에서 랜덤으로 강의 추출
            recommended_course_1 = random.choice(target)
            recommended_course_2 = random.choice(target)
            recommended_course_3 = random.choice(target)

    return render(request, 'recommend/recommend.html', {'recommended_course_1': recommended_course_1,
                                                        'recommended_course_2': recommended_course_2,
                                                        'recommended_course_3': recommended_course_3
                                                        })



