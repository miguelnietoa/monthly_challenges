from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

# Challenges from <https://co.pinterest.com/pin/220465344245180683/>
monthly_challenges = {
    'january': {
        'challenge': 'Drink more water!',
        'description': 'It sounds so simple, but it works. One study found that drinking water \
                helps you lose weight. Water keeps you feeling full so you\'ll eat less. Plus, \
                it flushes out toxins. Drink a minimum of eight 8-ounce cups per day. And if \
                you\'re thirsty, drink another glass.'},
    'february': {
        'challenge': 'Make breakfast a priority!',
        'description': 'A study of people who lost 30 pounds or more and kept it off for more \
                than a year showed 78 percent ate breakfast. Keep breakfast simple with a bowl \
                of whole-grain cereal with nonfat milk and fruit or whole-wheat toast with \
                low-fat cheese and yogurt.'},
    'march': {
        'challenge': 'Get more sleep!',
        'description': 'Research shows that one-quarter of adults in the U.S. don\'t get \
                enough sleep. Getting your ZZZs helps your body fight off illnesses like \
                the cold or flu, and may lower your risk of heart disease and diabetes. \
                For a better, healthier you, aim for 7 to 8 hours of sleep a night.'},
    'april': {
        'challenge': 'Keep a food journal!',
        'description': 'Writing down what you eat may double your weight loss, \
                according to researchers. Keeping track of your intake makes you \
                more aware of what you\'re eating. It also helps you identify \
                specific food habits and where you can make healthy changes.'},
    'may': {
        'challenge': 'Go for a walk!',
        'description': 'When it comes to exercise, walking is free, requires no special \
                equipment and can be done anywhere. You need 30 minutes of walking at a \
                brisk pace five days a week. If time is a problem, break your walks into \
                10 or 15-minute intervals two to three times a day.'},
    'june': {
        'challenge': 'Eat fruits and veggies!',
        'description': 'Low in calories and full of fiber, you can\'t go wrong eating \
                more of these nutrient-rich gems. You\'ll have an easier time maintaining \
                a healthy weight and also a lower risk of heart disease, diabetes and \
                certain types of cancer. Fill half your plate with fruits and veggies.'},
    'july': {
        'challenge': 'Downsize your plates!',
        'description': 'Your eyes can sometimes be too big for your stomach. \
                Trade your large dinner for a smaller lunch plate to cut \
                portions and save calories. Your plate will look full and \
                satisfying, but you\'ll eat less.'},
    'august': {
        'challenge': 'Go meatless!',
        'description': 'You don\'t have to give up meat altogether, but make \
                a plan to eat one or two meatless meals a week for better health. \
                One study showed that eating less meat, specifically red meat and \
                deli meat, may lower your risk of cancer and heart disease.'},
    'september': {
        'challenge': 'Find a workout buddy!',
        'description': 'Working out with a friend may increase your motivation \
                to exercise. It makes workouts more fun when you add a social \
                element to them. Plus, an accountability system helps you stay consistent.'},
    'october': {
        'challenge': 'Savor your meals!',
        'description': 'Perfect the art of slow eating. It takes your brain \
                20 minutes to send out signals of fullness. Taking your time \
                when eating helps you eat fewer calories and leaves you feeling more satisfied.'},
    'november': {
        'challenge': 'Unplug and unwind!',
        'description': 'The constant buzz of phone and email messages makes it \
                hard to relax. Research shows that heavy technology use may lead \
                to an increased risk of depression, stress and sleep disorders. \
                Make time to put the technology away and connect with yourself and loved ones.'},
    'december': {
        'challenge': 'Don\'t skip meals!',
        'description': 'Don\'t let your social calendar thwart all your efforts. \
                You may be tempted to skip lunch or dinner in an effort to save \
                room for party food, but it may backfire. Skipping meals leads \
                to extreme hunger, and you may end up eating more than you intended.'},
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
        challenge = monthly_challenges[month]['challenge']
        description = monthly_challenges[month]['description']
        return render(request, 'challenges/challenge.html', {
            'month': month,
            'challenge': challenge,
            'description': description,
        })
    except:
        raise Http404()
