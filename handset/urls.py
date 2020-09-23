from django.urls import path, include
from handset import views


urlpatterns = [
    path('', views.index, name=''),

    path('handset/', views.handset_view, name='handset_insert'),
    path('hsupdate/<int:hid>/', views.handset_view, name='handset_update'),
    path('hsdelete/<int:hid>/', views.handset_delete, name='handset_delete'),
    path('hslist/', views.handset_list, name='handset_list'),

    path('handset/search/', views.handsetsearch_view, name='handset_search'),

]
