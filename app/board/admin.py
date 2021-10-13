from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from solo.admin import SingletonModelAdmin

from .models import Submission, Dictionary, Text, Board, TestCase, User, SiteConfigurations


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    filter_horizontal = ['testcases']
    list_display = ['title', 'slug']


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['text', 'dictionary', 'used_in']


admin.site.register(Submission)
admin.site.register(Dictionary)
admin.site.register(Text)
admin.site.register(SiteConfigurations, SingletonModelAdmin)
