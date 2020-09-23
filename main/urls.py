from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # path('', views.ImageView.as_view(), name='imageform'),
    path('index', views.index, name='index'),
    path('success', views.PDFHandlerView.as_view()),
    path('logout', views.user_logout, name='logout'),
    path('', views.user_login, name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
