from django.urls import path,re_path
from .views import register, log_in, welcome, log_out
app_name = "basicapp"

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',log_in, name="login"),
    path('welcome/',welcome, name="welcome"),
    path('logout/',log_out, name="logout"),
]