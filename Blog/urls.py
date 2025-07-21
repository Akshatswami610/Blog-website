from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/signup', views.signup, name="signup"),
    path('blog/login', views.loginuser, name="login"),
    path('blog/logout', views.logoutuser, name="logout"),
    path("", views.index, name="blogHome"),
    path("blog/", views.index, name="blogHome"),
    path("blog/read/<int:post_id>/", views.read, name="read"),
    path("blog/addpost", views.addpost, name="addPost"),
    path("blog/contact", views.contact, name="contact"),
    path("blog/about", views.about, name="aboutUs"),
    path("blog/mypost", views.mypost, name="mypost"),
    path("blog/profile", views.profile, name="profile"),
    path("blog/designed-and-developed", views.designedanddeveloped, name="designed-and-developed"),
    path('blog/delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('delete-user/<str:username>/', views.delete_user_with_csrf, name='delete_user'),
    path('success/', views.submission_success, name='blog_submission_success'),
]

# Serve media only in local development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
