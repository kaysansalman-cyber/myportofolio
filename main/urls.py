from django.urls import path
from .views import (
    show_main,
    show_experience,
    create_experience,
    edit_experience,
    show_projects,
    create_project,
    delete_project,
    edit_project,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),

    path("experience/", show_experience, name="show_experience"),
    path(
        "experience/create/",
        create_experience,
        name="create_experience"
    ),
    path(
        "experience/edit/<uuid:id>/",
        edit_experience,
        name="edit_experience"
    ),

    path("projects/", show_projects, name="show_projects"),
    path("projects/create/", create_project, name="create_project"),
    path("projects/delete/<uuid:id>/", delete_project, name="delete_project"),
    path("projects/edit/<uuid:id>/", edit_project, name="edit_project"),
]