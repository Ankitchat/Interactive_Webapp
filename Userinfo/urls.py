from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        regex=r"^add/",
        view=views.UserInfodetail.as_view(),
        name="Add"),
    url(
        regex=r"^survey/",
        view=views.DisplayQuestion.as_view(),
        name="Survey"),
    url(
        regex=r"^confirm/",
        view=views.CreateCsv.as_view(),
        name="confirm"),

]
