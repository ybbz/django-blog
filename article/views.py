from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404


# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")


# def detail(request, number):
#     return HttpResponse("The number is %s." % number)


# def database(request, args):
#     post = Article.objects.all()[int(args)]
#     str = ("title = %s, category = %s, date_time = %s" % (post.title, post.category, post.date_time))
#     return HttpResponse(str)

def database(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})


def template(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})
