from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m') # lưu trữ và quản lý hình ảnh, tải các tệp ảnh và cung cấp đường dẫn

class Category(models.Model):#loại 
    name = models.CharField(max_length= 100, null=False, unique=True)#
    
    def __str__(self):
        return self.name
    
class ItemBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=255, null= False)# lưu trữ chuỗi kí tự có giới hạn/ tên môn học
    created_date = models.DateTimeField(auto_now_add= True) #update khi add 
    updated_date = models.DateTimeField(auto_now= True)#update khi co su thay doi
    active = models.BooleanField(default=True) # lưu trữ các giá trị True hoặc False
    image = models.ImageField(upload_to= 'courses/%Y/%m', default=None)
    
    def __str__(self):
        return self.subject
    
class Course (ItemBase):
    class Meta:
        unique_together = ('subject', 'category')
    description = models.TextField(null=True, blank=True)#
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True)#
    
class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'course')
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)#tạo quan hệ one to one giữa 2 model khác nhau / khóa học
    content =RichTextField()  #lưu trữ chuỗi kí tự không giới hạn
    tags = models.ManyToManyField('Tag', related_name='lessons', blank= True, null= True) #moi quan he many to many
    
class Tag(models.Model):
    name = models.CharField(max_length= 50, unique= True)
    
    def __str__(self):
        return self.name
    
   
    
    