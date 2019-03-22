from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='DRF Swagger for API documentation')

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('accounts/', include('accounts.urls'))
]

# Browsable API login
urlpatterns += [
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
