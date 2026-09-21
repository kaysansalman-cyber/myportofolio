from django.urls import path
from .views import (
    show_main,
    show_experience,
    experience_json,
    experience_json_deserialized,
    create_experience,
    edit_experience,
    delete_experience,
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
    "experience/json/",
    experience_json,
    name="experience_json"
    ),
    path(
    "experience/json/deserialized/",
    experience_json_deserialized,
    name="experience_json_deserialized"
    ),
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
    path(
    "experience/delete/<uuid:id>/",
    delete_experience,
    name="delete_experience"
    ),

    path("projects/", show_projects, name="show_projects"),
    path("projects/create/", create_project, name="create_project"),
    path("projects/delete/<uuid:id>/", delete_project, name="delete_project"),
    path("projects/edit/<uuid:id>/", edit_project, name="edit_project"),
]