from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.user_register, name='register'),
    path('pdfs', views.user_pdf, name='pdfs'),
    path('delete/<int:id>', views.pdf_delete, name='delete'),
    path('views/<int:id>', views.pdf_view, name='view'),
    path('profile', views.user_profile, name='profile'),
    path('profile/edit', views.user_edit, name='edit'),
    path('send', views.send_mail, name='send'),
    path('success', views.PDFHandlerView.as_view()),

    path('reset', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset/sent', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/complete', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
