from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name = "create_entry"),
    path("new/", views.new_entry, name = "new_entry"),
    path("edit/<str:title>/", views.edit, name = "edit"),
    path("edited/", views.edited, name = "edited"),
    path("random", views.random_page, name = "random"),
    path("<str:title>/", views.name, name = "name")
]
