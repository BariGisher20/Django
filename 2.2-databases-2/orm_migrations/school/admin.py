from django.contrib import admin

from .models import Student, Teacher, TeacherStudentMarks


class TeacherStudentMarksInline(admin.TabularInline):
    model = TeacherStudentMarks
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [TeacherStudentMarksInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    inlines = [TeacherStudentMarksInline]


@admin.register(TeacherStudentMarks)
class TeacherStudentMarksAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'teacher', 'mark']

