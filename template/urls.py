from django.urls import path

from template.views import IndexView ,Cycke6View,DatacollectionView,NtrcaView,SearchView,TableView

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('cycke/',Cycke6View.as_view(),name='cycke'),
    path('datacollection/',DatacollectionView.as_view(),name='datacollection'),
    path('ntrca/',NtrcaView.as_view(),name='ntrca'),
    path('search/',SearchView.as_view(),name='search'),
    path('table/',TableView.as_view(),name='table'),
]