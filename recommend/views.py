
from ninja import Router

router = Router()


@router.post("")  # 이미 앞 url이 api/recommend/ 인 경우에 이 def 작동
def create_recommendations(request):

    # request body 추출& 가공 ninja API router것들 작성
    datas = []
    # 추천 ai 모듈 작동 - 문제
    result = []

    # 필요시 result 가공
    presenter = []

    return "recommendations.html"  # html 파일 열면서 ai 모듈 돌려서 나온 결과값들 함께 출력
