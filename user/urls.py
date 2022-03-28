from django.urls import path
from .views import VerificationView

from . import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>', views.VerificationView.as_view(), name='activate'),
    path('', views.startpage, name='startpage'),
]
