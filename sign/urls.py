from sign import views_if
from django.urls import path




urlpatterns = [
	#sign system interface
	#ex:/api/add_event/
	path('add_event/',views_if.add_event,name='add_event'),
	#ex:/api/add_guest/
	path('add_guest/',views_if.add_guest,name='add_guest'),
	#ex:/api/get_event_list/
	path('get_event_list/',views_if.get_event_list,name='get_event_list'),
	#ex:/api/get_guest_list/
	path('get_guest_list/',views_if.get_guest_list,name='get_guest_list'),
	#ex:/api/user_sign/
	path('user_sign/',views_if.user_sign,name='user_sign'),
	#/api/get_csrf
	path('get_csrf/',views_if.get_csrf,name='get_csrf')
]

