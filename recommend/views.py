
from ninja import Router

router = Router()


@router.post("")  # 이미 앞 url이 apis/recommend/ 인 경우에 이 def 작동하는거네
def create_recommendations(request):
    # request body 추출& 가공 ninja API router것들 작성
    datas = []
    # 추천 ai 모듈 작동 - 문제
    result = []

    # 필요시 result 가공
    presenter = []
    return "recommendations.html"
