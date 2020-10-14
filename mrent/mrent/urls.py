from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from servicos.views import servicos, marido, contratante

urlpatterns = [
    path('', include('servicos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', servicos.SignUpView.as_view(), name='signup'),
    path('accounts/signup/marido/', marido.MaridoSignUpView.as_view(), name='marido_signup'),
    path('accounts/signup/contratante/', contratante.ContratanteSignUpView.as_view(), name='contratante_signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


