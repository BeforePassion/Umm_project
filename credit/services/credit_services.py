
from credit.models import Credit


def credit_charge_service(mentor_id: str , credit : int) -> str:

    credit_target = Credit.objects.filter(mentor_id=mentor_id)
    credit_value = credit_target.values('credit').get()['credit']

    if credit_target:
        credit_target.update(credit=credit_value + credit)

        msg = {"msg": f"크레딧 증정이 완료되었습니다. 현재 크레딧 금액{credit_value}"}
        return msg

def credit_use_service(mentor_id: str , credit : int) -> str:

    credit_target = Credit.objects.filter(mentor_id=mentor_id)
    credit_value = credit_target.values('credit').get()['credit']

    if credit_target:
        credit_target.update(credit=credit_value - credit)

        msg = {"msg": f"요청하신 크레딧이 사용되었습니다. 현재 크레딧 금액{credit_value}"}
        return msg






# def charge_history(request, page: int):
#     data = PointHistory.objects.filter(user_id=request.user.id, usage=True)
#     data = list(data.values())
#     p = Paginator(data, 5)
#     total_page = p.num_pages
#     p_data = p.page(page)
#     p_data = p_data.object_list
#     t_page = {"total_page": total_page}
#     data = {"p": p_data, "t": t_page}
#
#     return JsonResponse(data, safe=False)
#
#
#
# def usage_history(request):
#     data = PointHistory.objects.filter(user_id=request.user.id, usage=False)
#     data = list(data.values())
#     return JsonResponse(data, safe=False)
