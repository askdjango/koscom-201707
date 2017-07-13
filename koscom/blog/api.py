import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from .serializers import PostSerializer


@csrf_exempt
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
        serializer = PostSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

