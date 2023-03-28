from django.shortcuts import render

# Create your views here.
def number_print(request, num):
    context = {
        'num':num,
    }
    return render(request, 'articles/number_print.html', context)


def calculate(request, num1, num2):
    context = {
        'plus':num1+num2,
        'minus':num1-num2,
        'mul':num1*num2,
        'div':num1/num2,
    }
    
    return render(request, 'articles/calculate.html', context)