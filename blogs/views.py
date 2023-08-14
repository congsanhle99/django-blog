from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.


def posts_by_category(request, category_id):
    # fetch posts
    posts = Blog.objects.filter(status="Published", category=category_id)
    # category name by id
    # try:
    #     category_by_posts = Category.objects.get(pk=category_id)
    # except:
    #     return redirect("home")
    category_by_posts = get_object_or_404(Category, pk=category_id)
    context = {"posts": posts,
               "category_by_posts": category_by_posts}
    return render(request, "posts_by_category.html", context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status="Published")
    context = {"single_blog": single_blog}
    return render(request, "blogs.html", context)


def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(
        short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published")

    context = {"keyword": keyword, "blogs": blogs}
    return render(request, "search.html", context)
