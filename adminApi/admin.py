from django.contrib import admin
from .models import Project, Skill, Work, NavLink, SocialLink, WorkProject

admin.site.register([Project, Work, NavLink, SocialLink, Skill, WorkProject])
