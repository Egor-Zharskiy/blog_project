from django.urls import path

from users.views import login, registration, logout, profile, user_posts, create_post

app_name = "users"

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('user_posts', user_posts, name='user_posts'),
    path('create_post', create_post, name='create_post'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
