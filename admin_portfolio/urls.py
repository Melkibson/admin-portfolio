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
from django.contrib import admin
from django.urls import path
from admin_portfolio import views

urlpatterns = [
    path('', admin.site.urls),
    path('api/skills/', views.get_skills),
    path('api/skills/<uuid:_id>', views.get_skill),
    path('api/projects/', views.get_projects),
    path('api/projects/<uuid:_id>/', views.get_project),
    path('api/works/', views.get_works),
    path('api/work/<uuid:_id>', views.get_work),
    path('api/workprojects/', views.get_work_projects),
    path('api/workproject/<uuid:_id>', views.get_work_project),
    path('api/navlinks/', views.get_nav_links),
    path('api/navlink/<uuid:_id>/', views.get_nav_link),
    path('api/sociallinks/', views.get_social_links),
    path('api/sociallink/<uuid:_id>/', views.get_social_link)
]
