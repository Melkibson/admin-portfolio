"""admin_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from rest_framework import routers
import adminApi.views as views

router = routers.DefaultRouter()

router.register(r'projects', views.ProjectsViewSet, basename='project')
router.register(r'works', views.WorksViewSet, basename='work')
router.register(r'work-projects', views.WorkProjectsViewSet, basename='work-project')
router.register(r'skills', views.SkillViewSet, basename='skill')
router.register(r'navigation', views.NavLinksViewSet, basename='navigation')
router.register(r'socials', views.SocialLinksViewSet, basename='social')