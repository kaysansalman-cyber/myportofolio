from django.test import TestCase

from django.test import TestCase
from django.urls import reverse

from .models import Project


class ProjectPageTest(TestCase):

    def test_projects_url_and_template(self):
        response = self.client.get(reverse("main:show_projects"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects.html")

    def test_project_data_appears_on_page(self):
        Project.objects.create(
            title="Test Project",
            description="This is a test project.",
            project_type="web",
            technologies="Django, Python",
            github_url="https://github.com/test/project"
        )

        response = self.client.get(reverse("main:show_projects"))

        self.assertContains(response, "Test Project")
        self.assertContains(response, "This is a test project.")
        self.assertContains(response, "Django, Python")

    def test_empty_projects_page_shows_empty_message(self):
        response = self.client.get(reverse("main:show_projects"))

        self.assertContains(
            response,
            "Belum ada project yang tersedia."
        )
