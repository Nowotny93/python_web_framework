from django.shortcuts import render


def landing_page(request):
    return render(request, 'pets/../../templates/landing_page.html')
