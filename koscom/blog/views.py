from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()

    query = request.GET.get('query', '')
    if query:
        qs = qs.filter(title__icontains=query)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'query': query,
    })

def mysum(request, numbers):
    # numbers = "10/20/30/40//"

    # generator expression
    result = sum(
        int(number or 0)
        for number in numbers.split('/'))

    return HttpResponse(result)


def hello(request, name, age):
    message = '안녕하세요. {}. 저는 {}살입니다.'.format(name, age)
    return HttpResponse(message)

