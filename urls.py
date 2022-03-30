from unicodedata import name
from django.urls import path
from . import views

#URL conf에 이름 공간 추가
app_name = "polls"
#polls:path 형식으로 url을 구분할 수 있다.

#url 패턴과 view 함수 매칭
urlpatterns = [
    path('', views.index, name="index"),    # '' = /polls/
    path("<int:question_id>/", views.detail, name="detail"),
    # 예) /polls/5/
    path("<int:question_id>/result/", views.result, name="result"),
    # 예) /polls/5/result/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # 예) /polls/5/vote/
]