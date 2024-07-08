from django.contrib import admin
from .models import Course, Lesson, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'price', 'created_at')
    list_filter = ('instructor', 'created_at')
    search_fields = ('title', 'description', 'instructor__username')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    search_fields = ('title', 'content', 'course__title')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'date_enrolled')
    list_filter = ('course', 'date_enrolled')
    search_fields = ('user__username', 'course__title')