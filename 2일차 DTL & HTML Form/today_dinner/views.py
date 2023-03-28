from django.shortcuts import render
import random

# Create your views here.


def today_dinner(request):
    foods = ['짜장면', '보쌈', '포케', '피자']
    context = {
        'foods': random.choice(foods),
    }
    return render(request, 'today_dinner/today_dinner.html', context)
