from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import status
from .serializers import ProjectSerializer, WorkSerializer, SkillSerializer, NavLinkSerializer, SocialLinkSerializer, WorkProjectSerializer
from .models import Project, Work, Skill, NavLink, SocialLink, WorkProject


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    response = JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    return response


@api_view(['GET'])
def get_project(request, _id):
    item = Project.objects.get(_id=_id)
    serializer = ProjectSerializer(item)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_works(request):
    items = Work.objects.all()
    serializer = WorkSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_work(_id=None):
    if _id:
        item = Work.objects.get(_id=_id)
        serializer = WorkSerializer(item)
        return JsonResponse({"status": "success", "data": serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_work_projects(request):
    items = WorkProject.objects.all()
    serializer = WorkProjectSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_work_project(_id=None):
    if _id:
        item = WorkProject.objects.get(_id=_id)
        serializer = WorkProjectSerializer(item)
        return JsonResponse({"status": "success", "data": serializer.data}, safe=False, status=status.HTTP_200_OK)


# class SkillViews(APIView):
@api_view(['GET'])
def get_skills(request):
    items = Skill.objects.all()
    serializer = SkillSerializer(items, many=True)
    return JsonResponse({"status": "success", "data": serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_skill(request, _id=None):
    if _id:
        item = Skill.objects.get(_id=_id)
        serializer = SkillSerializer(item)
        return JsonResponse({"status": "success", "data": serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_nav_links(request):
    items = NavLink.objects.all()
    serializer = NavLinkSerializer(items, many=True)
    return JsonResponse({"status": "success", "data": serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_nav_link(request, _id=None):
    if _id:
        item = NavLink.objects.get(_id=_id)
        serializer = NavLinkSerializer(item)
        return JsonResponse({"status": "success", "data": serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_social_links(request):
    items = SocialLink.objects.all()
    serializer = SocialLinkSerializer(items, many=True)
    return JsonResponse({"status": "success", "data": serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_social_link(request, _id=None):
    if _id:
        item = SocialLink.objects.get(_id=_id)
        serializer = SocialLinkSerializer(item)
        return JsonResponse({"status": "success", "data": serializer.data}, safe=False, status=status.HTTP_200_OK)
