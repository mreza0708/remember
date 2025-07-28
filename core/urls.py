from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to DevConnect!")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),      # API routes for user app
    path('test/', include('courses.urls')),   # Test route for courses app
    path('', home),                            # Root URL
]
