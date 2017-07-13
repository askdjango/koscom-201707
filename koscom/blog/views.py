from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import Post
from .forms import PostForm


def post_list(request):
    qs = Post.objects.all()

    query = request.GET.get('query', '')
    if query:
        qs = qs.filter(title__icontains=query)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'query': query,
    })

'''
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # form.cleaned_data
            # {'title': '', 'content': '', 'author': ''}
            form.save()  # ModelForm에서만 지원되는 함수
            return redirect('/blog/')
    else:  # GET이라면
        form = PostForm()

    return render(request, 'blog/post_form.html', {
        'form': form,
    })
'''

post_new = CreateView.as_view(model=Post, form_class=PostForm, success_url='/blog/')


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

