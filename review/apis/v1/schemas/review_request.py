from ninja import Schema


class request_review(Schema):
    mentor_id: str
    satisfaction: int
    interest: str
    review_content: str

class request_page(Schema):
    page : int