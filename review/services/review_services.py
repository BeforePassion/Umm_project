from typing import Type, Set, Any

from django.core.paginator import Paginator, Page

from review.models import Review


def review_add_service(request,satisfaction: int, interest: str, review_content: str) -> set[str]:
    Review.objects.create(user_id=request.user.id,interest=interest,satisfaction=satisfaction,review_content=review_content)
    msg = {'입력하신 리뷰가 작성되었습니다.'}
    return msg

def review_inquire_service(request, page) -> dict[str,Any]:
    data = Review.objects.filter(review_id=request.user.id)
    data = list(data.values())
    p = Paginator(data, 5)
    total_page = p.num_pages
    p_data: Page = p.page(page)
    p_data: Page = p_data.object_list
    t_page = {"total_page": total_page}
    msg: dict[str, Any] = {"p": p_data, "t": t_page}
    return msg


