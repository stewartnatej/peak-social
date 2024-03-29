"""
URL configuration for frog_jog_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from blogging.views import PostViewSet, UserViewSet, CategoryViewSet

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("users", UserViewSet, basename="users")
router.register("categories", CategoryViewSet, basename="categories")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include("blogging.urls")),
    path("polling/", include("polling.urls")),
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
