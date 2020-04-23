from django.contrib import admin
from django.urls import path
from . import views
from django.urls import reverse_lazy

  
# importing views from views..py 

from .views import itemview
from .views import itemupdateview
from .views import itemdeleteview
from .views import ItemDetailView,itemlistview

urlpatterns = [ 

    path('', itemview.as_view(success_url=reverse_lazy('item_create')), name='item_create' ),
    path('update/<int:pk>', itemupdateview.as_view(success_url=reverse_lazy('item_update')), name='item_update' ),
    path('delete/<int:pk>', itemdeleteview.as_view(success_url=reverse_lazy('item_delete')), name='item_delete' ),
    path('detail/<int:pk>', ItemDetailView.as_view(), name='item_detail' ),
    path('list', itemlistview.as_view(), name='item_list' ),

]

# urlpatterns = [
#     path('home', views.homepageview,name='home'),
#     path('about', views.aboutpageview,name='about'),
#     path('contact', views.contactpageview,name='contact'),
# ]
