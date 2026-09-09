from django.shortcuts import render
from .models import Experience


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