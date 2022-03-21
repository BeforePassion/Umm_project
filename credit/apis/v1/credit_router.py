from django.http import HttpRequest
from ninja import Router
from credit.apis.v1.schemas import request_CRUD, response_CRUD
from credit.services.credit_services import credit_charge_service,credit_use_service


router = Router()

@router.post("/charge", response=response_CRUD)
def credit_charge(request: HttpRequest, credit_charge_request : request_CRUD) -> str:
    msg = credit_charge_service(credit_charge_request.mentor_id , credit_charge_request.credit)
    return msg

@router.post("/use", response=response_CRUD)
def credit_use(request: HttpRequest, credit_charge_request : request_CRUD) -> str:
    msg = credit_use_service(credit_charge_request.mentor_id , credit_charge_request.credit)
    return msg