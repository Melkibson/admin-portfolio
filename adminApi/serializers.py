from rest_framework import serializers
from .models import Project, Work, WorkProject, Skill, NavLink, SocialLink


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = (
            '_id',
            'title',
            'description',
            'img',
            'img_alt',
            'url',
        )


class WorkProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkProject
        fields = (
            '_id',
            'name',
            'url'
        )


class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = (
            '_id',
            'job_title',
            'company',
            'location',
            'dateFrom',
            'dateTo',
            'projects',
        )


class NavLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = NavLink
        fields = (
            '_id',
            'name',
            'url'
        )


class SocialLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialLink
        fields = (
            '_id',
            'name',
            'url'
        )


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = (
            '_id',
            'img',
            'img_alt',
        )
