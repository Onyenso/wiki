from django.urls import path

from . import views

app_name="wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("random", views.random_page, name="random"),
    path("edit/<str:entry>", views.edit, name="edit")
]
