from django.db import models
from django.utils import timezone
from uuid import uuid4


class Project(models.Model):
    _id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    img = models.FileField(upload_to='tmp/static/img/')
    img_alt = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "projet"
        verbose_name_plural = "projets"


class WorkProject(models.Model):
    _id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True)
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "projet"
        verbose_name_plural = "projets pro"


class Work(models.Model):
    _id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True)
    job_title = models.CharField(max_length=150)
    company = models.CharField(max_length=100)
    contract = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    dateFrom = models.DateField(default=timezone.now)
    dateTo = models.DateField(default=timezone.now)
    project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)

    pass

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = "expérience"
        verbose_name_plural = "expériences pro"


class NavLink(models.Model):

    _id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "menu"
        verbose_name_plural = "menus"


class SocialLink(models.Model):
    _id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True)
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "réseau"
        verbose_name_plural = "réseaux sociaux"


class Skill(models.Model):
    _id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True)
    name = models.CharField(max_length=100)
    img = models.FileField(upload_to='tmp/static/img/')
    img_alt = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "compétence"
        verbose_name_plural = "compétences"