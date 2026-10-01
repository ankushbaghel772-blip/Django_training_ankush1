from django.urls import path
from Exam import views

urlpatterns = [
    path("testpaper/",views.testPaper),
    path("result/",views.result),
]