from django.urls import path, re_path  # Use path and re_path from django.urls

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name="signup"),
    re_path(r"^signup/validate$", views.signup_validate, name="signup_validate"),
    path('login', views.c_login, name="login"),
    path('login/send_otp', views.send_otp, name="send_otp"),
    re_path(r"^login/validate$", views.login_validate, name="login_validate"),
    path('search', views.search, name="search"),
    re_path(r'country/(?P<country_name>[\w|\W]+)$', views.get_country_details, name="country_page"),
    path('logout', views.c_logout, name="logout"),
]
