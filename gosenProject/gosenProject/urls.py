from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from rest_framework_swagger.views import get_swagger_view
from Admin import urls as AdminUrls
from employee import urls as EmployeeUrls
from client import urls as ClientUrls
from service import urls as ServiceUrls
from stocks import urls as StockUrls
from products import urls as ProductUrls
from works import urls as WorkUrls

schema_view = get_swagger_view(title='Demo Swagger API')

urlpatterns = [
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('admins/', include(AdminUrls)),
    path('employees/', include(EmployeeUrls)),
    path('clients/', include(ClientUrls)),
    path('services/', include(ServiceUrls)),
    path('stocks/', include(StockUrls)),
    path('products/', include(ProductUrls)),
    path('works/', include(WorkUrls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
