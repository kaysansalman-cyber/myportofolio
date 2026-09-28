import json

from django.shortcuts import redirect, render
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login, logout

from .models import Experience, Project
from .forms import ProjectForm, ExperienceForm, RegisterForm,  AuthenticationForm

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

def experience_json(request):
    data = serializers.serialize(
        "json",
        Experience.objects.all()
    )

    return HttpResponse(
        data,
        content_type="application/json"
    )

def experience_json_deserialized(request):
    data = serializers.serialize(
        "json",
        Experience.objects.all()
    )

    experiences = json.loads(data)

    context = {
        "experiences": experiences
    }

    return render(
        request,
        "experience_json.html",
        context
    )

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

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:show_main")
    else:
        form = RegisterForm()

    context = {
        "form": form
    }

    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("main:show_main")
    else:
        form = AuthenticationForm()

    context = {
        "form": form
    }

    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("main:show_main")