# blog_project/urls.py
from django.contrib import admin
from django.urls import include, path # new
from rest_framework.schemas import get_schema_view # new
from rest_framework_swagger.views import get_swagger_view # new



from rest_framework.documentation import include_docs_urls # new
API_TITLE = 'Blog API' # new
API_DESCRIPTION = 'A Web API for creating and editing blog posts.' # new



# schema_view = get_schema_view(title='Blog API') # new
schema_view = get_swagger_view(title=API_TITLE) # new




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), # new
    path('api-auth/', include('rest_framework.urls')), # new
    path('api/v1/rest-auth/', include('rest_auth.urls')), # new
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),# new
    # path('schema/', schema_view), # new

    path('docs/', include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)), # new
    path('swagger-docs/', schema_view), # new



]