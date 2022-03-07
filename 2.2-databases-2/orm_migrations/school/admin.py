from django.contrib import admin

from .models import Student, Teacher




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    # inlines = ['TeacherInline']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']



