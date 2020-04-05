from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from rest_framework_swagger.views import get_swagger_view
from Admin import urls as admin_urls
from employee import urls as employee_urls
from client import urls as client_urls
from service import urls as service_urls
from stocks import urls as stock_urls
from products import urls as product_urls
from works import urls as work_urls
from financials import urls as financial_urls
from potential_employees import urls as potential_employees_urls

schema_view = get_swagger_view(title='Demo Swagger API')

urlpatterns = [
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('admins/', include(admin_urls)),
    path('employees/', include(employee_urls)),
    path('clients/', include(client_urls)),
    path('services/', include(service_urls)),
    path('stocks/', include(stock_urls)),
    path('products/', include(product_urls)),
    path('works/', include(work_urls)),
    path('financials/', include(financial_urls)),
    path('potential_employees/', include(potential_employees_urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
