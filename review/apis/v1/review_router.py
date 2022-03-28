from typing import Any

from django.http import HttpRequest
from ninja import Router
from review.apis.v1.schemas import request_review, response_CRUD,request_page
from review.services.review_services import review_add_service,review_inquire_service


router = Router()

@router.post("/add", response=response_CRUD)
def review_add(request: HttpRequest, review_request : request_review) -> set[str]:
    msg = review_add_service(request,review_request.satisfaction,review_request.interest,review_request.review_content)
    return msg

@router.get("/inquire", response=response_CRUD)
def review_inquire(request: HttpRequest, page : request_page) -> dict[str,Any]:
    msg = review_inquire_service(request,page)
    return msg

