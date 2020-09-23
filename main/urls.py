from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # path('', views.ImageView.as_view(), name='imageform'),
    path('', views.index, name='index'),
    path('success', views.PDFHandlerView.as_view()),
    path('view', views.view, name='view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
