from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html')

def mysum(request, numbers):
    # numbers = "10/20/30/40"
    result = 0
    for number in numbers.split('/'):  # ['10', '20', '30', '40']
        result += int(number)
    return HttpResponse(result)

