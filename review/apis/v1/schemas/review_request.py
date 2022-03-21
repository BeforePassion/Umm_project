from ninja import Schema


class request_CRUD(Schema):
    mentor_id: str
    credit : int

