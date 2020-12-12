from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from courses.views import CourseListView

urlpatterns = [
    path('account/login/', auth_views.LoginView.as_view(), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('course/', include('courses.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('', CourseListView.as_view(), name='course_list'),

]
