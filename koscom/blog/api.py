import json
from django.http import HttpResponse
from .models import Post


def post_list(request):
    if request.method == 'GET':
        # 글목록
        data = []
        for post in Post.objects.all():
            data.append({
                'title': post.title,
                'content': post.content,
            })
        json_string = json.dumps(data, ensure_ascii=False)
        return HttpResponse(json_string)

    elif request.method == 'POST':
        # 받은 데이터로 글 생성
        pass

