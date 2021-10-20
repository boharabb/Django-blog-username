from django.urls import path
from userprofile.views import loginview, logout_view, signupview, viewprofile, updateprofile, updatepass, usersprofile


app_name = "userprofile"
urlpatterns=[
    path("", logout_view, name="logoutuser"),
    path("loginview/", loginview, name="userlogin"),
    path("signup/", signupview, name="usersignup"),
    path("profileview/<int:user_id>/", viewprofile, name="profileview"),
    path("profileview/", usersprofile, name="users"),
    path("profileview/updateprofile/", updateprofile, name="updateprofile"),
    path("passchange/", updatepass, name="changepass"),

]