from django.shortcuts import render


def index(request):
    return render(request, 'index.html' )


def trial_recip_page(request):
    return render(request, 'trial_recip_page.html')