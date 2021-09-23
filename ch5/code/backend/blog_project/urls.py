# blog_project/urls.py
from django.contrib import admin
from django.urls import include, path # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), # new
    path('api-auth/', include('rest_framework.urls')), # new
    path('api/v1/rest-auth/', include('rest_auth.urls')), # new
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls'))# new


]