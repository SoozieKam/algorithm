import random
from django.shortcuts import render

# Create your views here.
# 특정 기능을 수행하는 view 함수들을 작성
# 모든 view 함수는 첫번째 인자로 요청 객체를 필수적으로 받는다./


def index(request):
    context = {
        'name': 'Soozie'
    }

    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = ['짜장면', '보쌈', '포케', '피자']
    context = {
        'foods': foods,
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    data = request.GET.get('message')
    context = {
        'data': data,
    }
    return render(request, 'articles/catch.html', context)


# Create your views here.


def today_dinner(request):
    foods = ['짜장면', '보쌈', '포케', '피자']
    context = {
        'foods': random.choice(foods),
    }
    return render(request, 'articles/today_dinner.html', context)


def detail(request, name):
    context = {
        'str': name,
    }

    return render(request, 'articles/detail.html', context)
