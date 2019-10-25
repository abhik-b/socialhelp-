from django.urls import path
from .views import accept_friend_request, send_friend_request, profile_view, home, search, remove_friend, cancel_friend_request, delete_friend_request


app_name = 'users'
urlpatterns = [
    path('', home, name='home'),
    path('profile/<int:id>', profile_view, name='profile'),
    path('sendrequest/<int:id>', send_friend_request, name='sendrequest'),
    path('acceptrequest/<int:id>', accept_friend_request, name='acceptrequest'),
    path('search/', search, name='search'),
    path('removefriend/<int:id>', remove_friend, name='removefriend'),
    path('cancelrequest/<int:id>', cancel_friend_request, name='cancelrequest'),
    path('deleterequest/<int:id>', delete_friend_request, name='deleterequest'),
]
