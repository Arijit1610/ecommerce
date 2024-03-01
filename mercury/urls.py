from . import views
from django.urls import path

urlpatterns = [
	path('',views.home, name='home'),
	# path('register/',views.register,name='register')
	path('register/', views.registration_view, name='register'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
]

