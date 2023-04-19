from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, permissions, generics
from .models import Course, Lesson, User
from .serializers import CourseSerializer, LessonSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
# Create your views here.


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active = True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]
    extra_kwargs = {
        'password': {'write_only': 'true'}
    }
    
    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        return[permissions.AllowAny()]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active = True)
    serializer_class = CourseSerializer
    # swagger_schema = None
    
    # permission_classes = [permissions.IsAuthenticated]  # xac thuc dang nhap
    
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
    
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active = True)
    serializer_class = LessonSerializer
    
    # an lesson(active = Flase)
    @action(methods=['POST'], detail= True, url_path='hide_lesson', url_name= 'hide_lesson')
    #/lesson/{pk}/hide_lesson
    def hide_lesson (self, request, pk):
        try:
            l = Lesson.objects.get(pk = pk)
            l.active =False
            l.save()
        except Lesson.DoesNotExist:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        
        return Response(data= LessonSerializer(l, context = {'request': request}).data, status= status.HTTP_200_OK)
            
        
        

    
def index(request):
    
    return render(request, template_name='index.html',context={'name':'hanoi'})


 
class TestView(View):
    def get(self, request):
        return HttpResponse('TEST')
    
    def posr(self, request):
        pass
