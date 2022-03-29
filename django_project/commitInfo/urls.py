from django.urls import path
from commitInfo import views

urlpatterns = [
    path("home/", views.home, name="home"),
    #path("test-url/", views.test_url, name="test-url"),
    path("commitinfo/", views.check_db, name="commitInfo"),
    path("test/", views.check_db, name="checkdb"),
    #path("test/<name>", views.hello_there, name="test")
]