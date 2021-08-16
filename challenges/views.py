from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


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
    'december': 'Go to the gym!',
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    if 1 <= month <= 12:
        months = list(monthly_challenges.keys())
        redirect_month = months[month-1]
        return HttpResponseRedirect(f'/challenges/{redirect_month}')
    else:
        return HttpResponseNotFound('Invalid month')


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound('This month is not supported!')
