from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('banini_app.urls')),  # Página inicial redireciona para o app
    path('pagamentos/', include('banini_app.urls')),
]