from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .utils.data import monthly_challenges

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {'months': months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if 1 <= month <= len(months):
        redirect_month = months[month-1]
        # Use reverse instead of hardcoding the URL ;)
        # /challenges/<str:month>
        redirect_path = reverse('month-challenge', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        raise Http404()


def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]['challenge']
        description = monthly_challenges[month]['description']
        return render(request, 'challenges/challenge.html', {
            'month': month,
            'challenge': challenge,
            'description': description,
        })
    except:
        raise Http404()
