from . import views
from django.urls import path

urlpatterns = [
	path('',views.home, name='home'),
	path('register/',views.register,name='register'),
	path('login/',views.loginPage,name='login'),
	path('logout/',views.logoutPage,name='logout'),
	path('search/', views.searchProducts, name = 'search'),
	path('eletronices/',views.eletronices,name='eletronices'),
	path('bookandstationery/',views.booksandstationery,name='bookandstationery'),
	path('beautycosmetics/',views.beautycosmetics,name='beautycosmetics'),
	path('fashion/',views.fashion,name='fashion'),
	path('sports',views.sportsandoutdoor,name='sports'),
	path('homeandkitchen',views.homeandkitchen,name='homeandkitchen'),
	path('activate/<uidb64>/<token>', views.activate, name='activate'),
]

