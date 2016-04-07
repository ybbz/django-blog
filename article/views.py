from django.shortcuts import render, redirect
from django.http import HttpResponse
from article.models import Article, Blog
from datetime import datetime
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection


# Create your views here.
def test(request):
    return HttpResponse("Hello World, Django")


# def detail(request, number):
#     return HttpResponse("The number is %s." % number)


# def database(request, args):
#     post = Article.objects.all()[int(args)]
#     str = ("title = %s, category = %s, date_time = %s" % (post.title, post.category, post.date_time))
#     return HttpResponse(str)

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})


def home(request):
    posts = Article.objects.all()  # 获取全部的Article对象
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list,
                                             'error': False})


def about(request):
    return render(request, 'about.html')


def tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})


def search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': False})
    return redirect('/')


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content


def category(request):
    cate_sql = 'select count(id),category from blog group by category'
    categories = get_custom_sql(cate_sql)
    category_list = []
    for cate in categories:
        category_list.append(cate[1] + '(' + str(cate[0]) + ')')
    return render(request, 'category.html', {'category_list': category_list})


def home2(request):
    posts = Blog.objects.all()  # 获取全部的Article对象
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home2.html', {'post_list': post_list})


def get_custom_sql(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    return row
