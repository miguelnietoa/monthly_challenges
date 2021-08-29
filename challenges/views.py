from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Go to the gym!',
    'may': 'Eat no meat for the entire month!',
    'june': 'Walk for at least 20 minutes every day!',
    'july': 'Learn Django for at least 20 minutes every day!',
    'august': 'Go to the gym!',
    'september': 'Eat no meat for the entire month!',
    'october': 'Walk for at least 20 minutes every day!',
    'november': 'Learn Django for at least 20 minutes every day!',
    'december': None,
}

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
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month': month
        })
    except:
        raise Http404()
