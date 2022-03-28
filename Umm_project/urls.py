"""Umm_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from recommend.views import router as recommend_router
from credit.apis.v1.credit_router import router as credit_router
from review.apis.v1.review_router import router as review_router

api = NinjaAPI()
api.add_router("recommend/", recommend_router)
api.add_router("credit/", credit_router)
api.add_router("review/", review_router)

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
    path('credit/', include('credit.urls')),
    path('review/', include('review.urls'))

]

