from django.urls import path

from posts.views import index

app_name = "posts"

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>', index, name='category')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
