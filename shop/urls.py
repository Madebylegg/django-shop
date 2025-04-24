from django.urls import path, include
from django.shortcuts import redirect
from shop import views  # use your actual app name

urlpatterns = [
    # ✅ Your custom views
    path('login/', views.login_view, name='shop-login'),
    path('signup/', views.signup_view, name='shop-signup'),
    path('logout/', views.logout_view, name='shop-logout'),

    # ✅ Redirect default allauth routes to your custom pages
    path('accounts/login/', lambda request: redirect('shop-login')),
    path('accounts/signup/', lambda request: redirect('shop-signup')),
    path('accounts/logout/', lambda request: redirect('shop-logout')),

    # ✅ Still include allauth for Google/Facebook login callbacks
    path('accounts/', include('allauth.urls')),

    # ✅ Other app URLs or pages
    path('', views.home, name='home'),  # Example home route
]
