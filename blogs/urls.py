from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views
urlpatterns = [
    # path('category/', include('blogs.urls')),
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
]
