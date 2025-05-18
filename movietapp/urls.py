from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('adminindex/',views.adminindex,name='adminindex'),
    path('about/',views.about,name='about'),
    path('e-ticket/',views.e_ticket,name='e_ticket'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('ticket-booking/',views.ticket_booking,name='ticket-booking'),
    path('adminadd/',views.adminadd,name='adminadd'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('adminupdate/<int:id>/', views.adminupdate,name='adminupdate'),
    path('admindelete/<int:id>/', views.admindelete,name='admindelete'),
    path('admindetail/<int:moviet_id>/', views.admindetail, name='admindetail'),

]
