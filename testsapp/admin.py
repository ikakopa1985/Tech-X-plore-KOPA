from django.contrib import admin
from testsapp.models import *

# Register your models here.


class TestOriginAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TestOrigin._meta.fields]

    class Meta:
        model = TestOrigin
        extra = 0


class TestTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TestType._meta.fields]

    class Meta:
        model = TestType
        extra = 0


class AnswersInline(admin.TabularInline):
    model = Answers
    extra = 0


class TestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Test._meta.fields]
    list_display_links = ('id', 'testDescription')
    inlines = [AnswersInline]
    # search_fields = ('name',)
    # list_editable = ('category','price','is_active')
    # list_filter = ('category',)

    class Meta:
        model = Test


class AnswersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Answers._meta.fields]

    class Meta:
        model = Answers
        extra = 0


class UserIdentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserIdent._meta.fields]
    search_fields = ('full_name',)
    autocomplete_fields = ['user']


admin.site.register(TestOrigin, TestOriginAdmin)
admin.site.register(TestType, TestTypeAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Answers, AnswersAdmin)
admin.site.register(UserIdent, UserIdentAdmin)
