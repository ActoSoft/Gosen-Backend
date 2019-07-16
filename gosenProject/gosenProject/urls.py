from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view
from Admin import urls as AdminUrls
from employee import urls as EmployeeUrls
from client import urls as ClientUrls

schema_view = get_swagger_view(title='Demo Swagger API')

urlpatterns = [
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    #path('login/', ),
    #path('forgot_password/', ),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('admins/', include(AdminUrls)),
    path('employees/', include(EmployeeUrls)),
    path('clients/', include(ClientUrls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)