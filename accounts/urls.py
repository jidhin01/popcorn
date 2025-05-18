from django.urls import path
from .import views

app_name = 'accounts'  # Namespace for URLs

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),  # Single page for Sign In & Sign Up
    path('logout/',views. logout_view, name='logout'),
]
