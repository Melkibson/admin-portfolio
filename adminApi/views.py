from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .serializers import ProjectSerializer, WorkSerializer, SkillSerializer, NavLinkSerializer, SocialLinkSerializer, WorkProjectSerializer
from .models import Project, Work, Skill, NavLink, SocialLink, WorkProject


class ProjectsViewSet(ModelViewSet):
    queryset = Project.objects.all()

    def list(self, request):
        query_set = Project.objects.all()
        serializer = ProjectSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        query_set = self.get_object()
        serializer = ProjectSerializer(query_set)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)


class WorksViewSet(ModelViewSet):
    queryset = Work.objects.all()

    def list(self, request):
        query_set = Work.objects.all()
        serializer = WorkSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        query_set = self.get_object()
        serializer = WorkSerializer(query_set)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)


class WorkProjectsViewSet(ModelViewSet):
    queryset = WorkProject.objects.all()

    def list(self, request):
        query_set = WorkProject.objects.all()
        serializer = WorkProjectSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        query_set = self.get_object()
        serializer = WorkProjectSerializer(query_set)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()

    def list(self, request):
        query_set = Skill.objects.all()
        serializer = SkillSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        query_set = self.get_object()
        serializer = SkillSerializer(query_set)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)


class NavLinksViewSet(ModelViewSet):
    queryset = NavLink.objects.all()

    def list(self, request):
        query_set = NavLink.objects.all()
        serializer = NavLinkSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        query_set = self.get_object()
        serializer = NavLinkSerializer(query_set)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)


class SocialLinksViewSet(ModelViewSet):
    queryset = SocialLink.objects.all()

    def list(self, request):
        query_set = SocialLink.objects.all()
        serializer = SocialLinkSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        query_set = self.get_object()
        serializer = SocialLinkSerializer(query_set)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
