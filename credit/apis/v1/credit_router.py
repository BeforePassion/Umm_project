from typing import Any

from django.http import HttpRequest, JsonResponse
from ninja import Router
from credit.apis.v1.schemas import request_CRUD, response_CRUD, request_page,request_use
from credit.services import credit_inquire_service,credit_charge_service,credit_use_service,charge_history_service,use_history_service

router = Router()


@router.get("/inquire")
def credit_inquire(request: HttpRequest) -> dict[str, int]:
    msg = credit_inquire_service(request)
    return msg

@router.post("/charge", response=response_CRUD)
def credit_charge(request: HttpRequest) -> dict[str]:

    msg = credit_charge_service(request)
    return msg


@router.post("/use", response=response_CRUD)
def credit_use(request: HttpRequest, credit: request_use) -> dict[str]:
    msg = credit_use_service(request, credit.credit)
    return msg

@router.post("/charge/history")
def credit_charge_history(request: HttpRequest, page: request_page) -> dict[str, Any]:
    msg = charge_history_service(request,page.page)
    return msg

@router.post("/use/history")
def credit_use_history(request: HttpRequest, page: request_page) -> dict[str, Any]:
    msg = use_history_service(request,page.page)
    return msg