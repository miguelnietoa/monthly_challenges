from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': 'Drink more water!',
    'february': 'Make breakfast a priority!',
    'march': 'Get more sleep!',
    'april': 'Keep a food journal!',
    'may': 'Go for a walk!',
    'june': 'Eat fruits and veggies!',
    'july': 'Downsize your plates!',
    'august': 'Go meatless!',
    'september': 'Find a workout buddy!',
    'october': 'Savor your meals!',
    'november': 'Unplug and unwind!',
    'december': 'Don\'t skip meals!',
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
