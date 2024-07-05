from django.contrib import admin
from testsapp.models import *

# Register your models here.


class Category3Admin(admin.ModelAdmin):
    list_display = [field.name for field in Category3._meta.fields]

    class Meta:
        model = Category3
        extra = 0


class Category2Admin(admin.ModelAdmin):
    list_display = [field.name for field in Category2._meta.fields]

    class Meta:
        model = Category2
        extra = 0


class Category1Admin(admin.ModelAdmin):
    list_display = [field.name for field in Category1._meta.fields]

    class Meta:
        model = Category1
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


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

    class Meta:
        model = Product
        extra = 0


admin.site.register(Category3, Category3Admin)
admin.site.register(Category2, Category2Admin)
admin.site.register(Category1, Category1Admin)

admin.site.register(Product, ProductAdmin)

admin.site.register(Test, TestAdmin)
admin.site.register(Answers, AnswersAdmin)
admin.site.register(UserIdent, UserIdentAdmin)
