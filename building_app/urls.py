from django.urls import path
from building_app import views

app_name="building_app"

urlpatterns =[
    path('',views.BuildingListView.as_view(),name='buildings_list'),
    path('<int:pk>/',views.AptListView.as_view(),name='apts_list'),
    path('building_det/<int:pk>',views.BuildingDetailView.as_view(),name='building'),    
    path('apartment_detail/',views.AptDetailView.as_view(),name='apt_detail'),
    path('apartment_detail/<int:pk>',views.AptUpdateView.as_view(),name='update'),
    path('persons_list/',views.PersonListView.as_view(),name='persons_list'),
    path('persons_list/<int:pk>',views.CreatePunchIn.as_view(),name='punchin'),
   
]