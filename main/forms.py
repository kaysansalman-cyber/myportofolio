from django.forms import ModelForm, TextInput, Textarea, URLInput, Select

from main.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project

        fields = [
            "title",
            "description",
            "project_type",
            "technologies",
            "github_url",
        ]

        labels = {
            "title": "Nama Project",
            "description": "Deskripsi Project",
            "project_type": "Tipe Project",
            "technologies": "Teknologi yang Digunakan",
            "github_url": "URL GitHub",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Personal Portfolio",
                    "maxlength": 255,
                }
            ),

            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan project yang kamu kerjakan",
                    "rows": 5,
                }
            ),

            "project_type": Select(),

            "technologies": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),

            "github_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/username/project",
                }
            ),
        }