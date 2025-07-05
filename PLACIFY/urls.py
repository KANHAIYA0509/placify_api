from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/students/', include('student.urls')),
    path('api/staff/', include('staff.urls')),
    path('api/companies/', include('company.urls')),
    path('api/applications/', include('application.urls')),
    path('api/users/', include('users.urls')),
]
