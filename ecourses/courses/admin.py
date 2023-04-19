from django.contrib import admin
from .models import Category, Course,Lesson, Tag
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class LessonInline(admin.StackedInline):
    model = Lesson
    pk_name = 'course'
    
class CourseAdmin(admin.ModelAdmin):
    inlines = (LessonInline,)

class LessonForm(forms.ModelForm):
    content =  forms.CharField(widget= CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'
        
class LessonTagInline(admin.StackedInline):
    model =Lesson.tags.through 

class LessonAdmin(admin.ModelAdmin):
    class Media:
        css = {'all': ('/static/css/main.css',)}
        
    form = LessonForm
    list_display = ['id','subject', 'created_date', 'active', 'course']
    search_fields = ['subject', 'created_date', 'course__subject']
    list_filter = ['subject', 'course__subject']
    readonly_fields = ['avatar']
    inlines = [LessonTagInline]
    
    def avatar (self, lesson):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width = '120' />".format( img_url = lesson.image.name, alt = lesson.subject))
    

# Register your models here.

admin.site.register(Category)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
