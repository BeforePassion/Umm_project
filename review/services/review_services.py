from review.models import Review

def create_an_review(user_id : int) -> Review:

    return Review.objects.create(review_id=user_id)



