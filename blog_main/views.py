from django.shortcuts import render
from blog_main.forms import RegistrationForm
from blogs.models import Blog, Category


def home(request):
    featured_posts = Blog.objects.filter(
        is_featured=True, status="Published").order_by("-update_at")
    not_featured_posts = Blog.objects.filter(
        is_featured=False, status="Published").order_by("-update_at")
    context = {"featured_posts": featured_posts,
               "not_featured_posts": not_featured_posts}
    return render(request, "home.html", context)


def register(request):
    form = RegistrationForm()
    context = {"form": form}
    return render(request, "register.html", context)
