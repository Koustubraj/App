from django.urls import path
from . import views

# 127.0.0.1:8000/

urlpatterns = [
    path("", views.index, name = 'index_page'), # 127.0.0.1:8000/
    path("greet/", views.greet, name = 'greet_page'), # 127.0.0.1:8000/greet/
    path("login/", views.login, name = 'login_page'), # 127.0.0.1:8000/login/
    path("login2/", views.login2, name = 'login2_page'), # 127.0.0.1:8000/login2/
]