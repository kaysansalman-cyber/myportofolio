from django.shortcuts import redirect, render
from .models import Experience, Project
from .forms import ProjectForm, ExperienceForm

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

def delete_project(request, id):
    project = Project.objects.get(id=id)

    if request.method == "POST":
        project.delete()
        return redirect("main:show_projects")

    context = {"project": project}
    return render(request, "delete_project.html", context)

def edit_project(request, id):
    project = Project.objects.get(id=id)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect("main:show_projects")
    else:
        form = ProjectForm(instance=project)

    context = {
        "form": form,
        "project": project,
    }

    return render(request, "edit_project.html", context)
def create_experience(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("main:show_experience")

    else:
        form = ExperienceForm()

    context = {
        "form": form
    }

    return render(request, "create_experience.html", context)

def edit_experience(request, id):
    experience = Experience.objects.get(id=id)

    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)

        if form.is_valid():
            form.save()
            return redirect("main:show_experience")
    else:
        form = ExperienceForm(instance=experience)

    context = {
        "form": form,
        "experience": experience,
    }

    return render(request, "edit_experience.html", context)

def delete_experience(request, id):
    experience = Experience.objects.get(id=id)

    if request.method == "POST":
        experience.delete()
        return redirect("main:show_experience")

    context = {
        "experience": experience
    }

    return render(request, "delete_experience.html", context)

