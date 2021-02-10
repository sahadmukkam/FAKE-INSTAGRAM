from django.urls import path
from post import views
urlpatterns = [

    path("", views.home_view, name="home"),
    path("add/", views.add_post, name="add_post"),
    path("like/<post_id>/",views.like_toggle)
    ]


