from django.urls import path

from blog.views import anasayfa, blog_detay

urlpatterns = [
    path('', anasayfa),
    path('blog-detay/<int:id>', blog_detay, name="blog_detay")
]
