from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')
    # students - прикрепленный к нему студент

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    teachers = models.ManyToManyField(Teacher, related_name='students')
    group = models.CharField(max_length=10, verbose_name='Класс')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name

# t1 = Teacher.objects.all()
# student_name = t1.name.all()
# s1 = Student.objects.all()
# teacher_name = s1.students.all(), где students - строка в таблице Teacher
