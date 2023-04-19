
from django.urls import path, re_path, include
from. import views
from rest_framework.routers import DefaultRouter
from ecourses.urls import schema_view
import debug_toolbar

router = DefaultRouter()
router.register('course', views.CourseViewSet)
router.register('lesson', views.LessonViewSet)
router.register('users', views.UserViewSet)

# /courses/ - GET xem khoa hoc
# /courses/ - POST them khoa hoc
# /courses/{courses-id} - GET  xem chi tiet
# /courses/{courses-id} - PUT  cap nhat khoa hoc khoa hoc
# /courses/{courses-id} - DELETE  xoa khoa hoc


urlpatterns = [
    # path('', views.index, name='index'),
    path('', include (router.urls)),
    
    path ('test/', views.TestView.as_view()),
    
    path ('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    re_path(r'^swagger (?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),name='schema-json'),
    re_path(r'^swagger/$',  schema_view.with_ui('swagger', cache_timeout = 0), name='schema-swagger-ui'),
    re_path(r'^redoc/$',  schema_view.with_ui('redoc',  cache_timeout = 0), name='schema-redoc'),
    path('__debug__/', include(debug_toolbar.urls)) 

]