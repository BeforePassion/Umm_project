from typing import Dict, Any
from datetime import timedelta, datetime
from django.core.paginator import Paginator, Page
from credit.models import Credit
from user.models import UserModel
from django.db.models import Sum
from review.models import Review
import re

def credit_inquire_service(request) -> dict[str, int]:
    credit = request.user.credit
    msg: dict[str, int] = {'my_credit': credit}
    return msg

def credit_charge_service(request) -> dict[str]:
    id = request.user.id
    credit = (Review.objects.filter(user_id=id).order_by("-review_date")[0].satisfaction)*100
    c = request.user.credit
    today_date=datetime.today().date()
    start_week = datetime(today_date.year, today_date.month, today_date.day)


    end_week = start_week + timedelta(7) - timedelta(seconds=1)
    # 유저가 한 주간 얻은 크레딧들의 총합
    own_week_credit = Credit.objects.filter(mentor_id=request.user.id,credit_type=1,credit_date__range=[start_week, end_week]).aggregate(Sum('credit'))['credit__sum']

    if own_week_credit == None:
        own_week_credit = 0
    # 한 주간 얻을 수 있는 크레딧의 한도
    week_limit_credit = 1000
    # 충전성공시 얻게되는 이번주 크레딧 충전량
    week_credit = credit+own_week_credit


    # 한 주간 얻을 수 있는 크레딧
    excess_credit = week_credit - week_limit_credit
    if week_credit <= week_limit_credit:
        Credit.objects.create(mentor_id=request.user.id,credit=int(credit), credit_type=True)
        UserModel.objects.filter(id=request.user.id).update(credit=c + int(credit))
        credit_value = UserModel.objects.get(id=request.user.id).credit
        msg: dict[str] = {"msg": f"크레딧 증정이 완료되었습니다. 현재 크레딧 금액{credit_value}"}
    else:
        msg: dict[str] = {"msg": f"주간 충전 크레딧 한도를 {excess_credit}만큼 초과합니다. 현재 주간 충전 크레딧 한도는 {week_limit_credit}입니다."}
    return msg

def credit_use_service(request, credit: int) -> dict[str]:
    c = request.user.credit

    if credit > c:
        msg: dict[str] = {"msg": f"현재 잔액{c}보다 사용하려는 금액이 {credit}만큼 큽니다."}
    else:
        UserModel.objects.filter(id=request.user.id).update(credit=c - int(credit))
        Credit.objects.create(mentor_id=request.user.id, credit=int(credit), credit_type=False)
        credit_value = UserModel.objects.get(id=request.user.id).credit
        msg: dict[str] = {"msg": f"크레딧이 정상적으로 사용되었습니다. 현재 크레딧 금액{credit_value}"}
    return msg

def charge_history_service(request, page: int) -> dict[str,Any] :
    data = Credit.objects.filter(mentor_id=request.user.id, credit_type=True)
    data = list(data.values())
    p = Paginator(data, 5)
    total_page = p.num_pages
    p_data = p.page(page)
    p_data = p_data.object_list
    t_page = {"total_page": total_page}
    msg:dict[str,Any] = {"p": p_data, "t": t_page}
    return msg

def use_history_service(request, page : int) -> dict[str,Any]:

    data = Credit.objects.filter(mentor_id=request.user.id, credit_type=False)
    data = list(data.values())
    p = Paginator(data, 5)
    total_page = p.num_pages
    p_data = p.page(page)
    p_data = p_data.object_list
    t_page = {"total_page": total_page}
    msg:dict[str,Any] = {"p": p_data, "t": t_page}
    return msg


