from django.shortcuts import redirect, render
from .models import Experience, Project
from .forms import ProjectForm

def show_main(request):
    context = {
        'name': 'Kaysan',
        'npm': '2506540670',
        'study_program': 'Sistem Informasi',
        'bio': 'I am an Information Systems student at the Faculty of Computer Science, Universitas Indonesia, interested in software development, technology, and building useful digital experiences.',
    }

    return render(request, 'index.html', context)


def show_experience(request):
    experiences = Experience.objects.all()

    context = {
        'experiences': experiences
    }

    return render(request, 'experience.html', context)

def show_projects(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'projects.html', context)

def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("main:show_projects")

    else:
        form = ProjectForm()

    context = {
        "form": form
    }

    return render(request, "create_project.html", context)