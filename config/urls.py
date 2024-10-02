
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_diary.urls', namespace='my_diary')),
    path('users/', include('users.urls', namespace='users')),
]
