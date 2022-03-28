from ninja import Schema

class request_CRUD(Schema):
    mentor_id: str
    credit : int

class request_page(Schema):
    page : int

class request_use(Schema):
    credit : int