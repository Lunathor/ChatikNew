from django.urls import path, include
from accounts.views import *


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', Profile.as_view(), name='profile'),
    path('user/', include('django.contrib.auth.urls')),
    path('user/logout/', Logout, name='Logout'),
]