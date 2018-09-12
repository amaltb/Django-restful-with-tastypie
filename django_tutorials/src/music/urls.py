from django.urls import re_path
from . import views

urlpatterns = [

    # /music/
    re_path(r'^?', views.index, name='index'),

    # /music/<album_id>
    re_path(r'P<album_id>([0-9]+)/?', views.detail, name='detail'),

    # /music/<album_id>/favourite/
    re_path(r'P<album_id>([0-9]+)/favourite/?', views.favourite, name='favourite')
]
