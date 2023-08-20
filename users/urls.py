from django.urls import path

from users.views import login

app_name = "users"

urlpatterns = [
    path('', login, name='login'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
