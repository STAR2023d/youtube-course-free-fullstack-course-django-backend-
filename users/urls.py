from django.urls import include, path
from users.views import CustomRegisterView

app_name = "users"



urlpatterns = [
    path("register/", CustomRegisterView.as_view(), name="register"),
    
]
