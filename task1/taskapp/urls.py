from . import views
from django.urls import path
from task1 import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.operation,name='operation'),
    # path('opp/',views.result,name='result'),
    # path('contact/',views.contact,name='contact'),
    # path('detail/',views.detail,name='detail'),
    # path('thanks/',views.thanks,name='thanks'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)