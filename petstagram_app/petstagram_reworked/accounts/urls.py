from django.urls import path
from petstagram_reworked.accounts.views import logout_user, RegisterView, ProfileDetailsView, LoginUserView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='log in user'),
    path('logout/', logout_user, name='log out user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('', ProfileDetailsView, name='profile details'),
)