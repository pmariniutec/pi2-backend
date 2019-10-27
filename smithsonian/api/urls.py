from django.urls import path

from smithsonian.api.views import users

urlpatterns = [
    path('user/', users.UserDetail.as_view(), name='user'),

]
