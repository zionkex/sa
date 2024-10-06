from django.shortcuts import render

from .models import Team


def about(request):
    team = Team.objects.all()
    context = {'team': team}
    return render(request, 'pages/about.html', context=context)