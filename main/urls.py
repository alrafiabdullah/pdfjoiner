from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.user_register, name='register'),
    path('pdfs', views.user_pdf, name='pdfs'),
    path('delete/<int:id>', views.pdf_delete, name='delete'),
    path('views/<int:id>', views.pdf_view, name='view'),
    path('success', views.PDFHandlerView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
