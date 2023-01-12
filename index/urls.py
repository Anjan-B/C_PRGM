from django.urls import path,include
from . import views

urlpatterns = [
    path('stockindex/',views.stockpage,name = 'stockpage'),
    path('addstock/',views.addstock,name = 'addstock'),
    path('stats/',views.stats,name = 'stats'),
    path('search/',views.search,name = 'search'),
    path('update/<update_id>',views.update,name = 'update'),
    path('delete/<delete_id>',views.delete,name = 'delete'),
    path('cryptoindex/',views.cryptopage,name = 'cryptopage'),
    path('fdindex/',views.fdpage,name = 'fdpage'),
    path('all_index/',views.all_index_page,name = 'all_index_page'),
]
