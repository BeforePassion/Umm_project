from django.test import TestCase

# Create your tests here.
from recommend.models import Lecture, Recommend
from user.models import UserModel


class RecommendModelTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create(
            email="test1@test.com",
            username="test1",
            password="test1",
            user_type="Mentor",
            experience="3"
        )
        Lecture.objects.create(
            name="test_lecture"
        )

    def test_recommend_model(self):
        user = UserModel.objects.all()

        # assertEqual
        assert len(user) == 1  # 유저 조회 결과가 1개인지
        assert isinstance(user[0], UserModel)  # 조회 결과에 UserModel이 제대로 존재하는지

        lecture = Lecture.objects.all()
        Recommend.objects.create(
            user=user[0],
            lecture=lecture[0]
        )

        recommend = Recommend.objects.all()

        assert isinstance(recommend[0], Recommend)
        assert recommend[0].user_id == 1  # Recommend에 들어간 유저가 처음 생성 해놓은 유저가 맞는지


class RecommendViewTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_recommend_view(self):
        # 만든 api가 제대로 routing 되었는지 확인
        res = self.client.post("/api/recommend/")

        assert res.status_code == 200  # 200: 성공

    def test_wrong_view(self):
        # 잘못된 api(url)로 연결할 경우
        res = self.client.post("api/recommend/")

        assert res.status_code == 404  # 404: not found

