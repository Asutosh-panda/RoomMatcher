from django.urls import path

from . import views


urlpatterns =[
    path('matcher/',views.matcher,name="matcher"),
    path('wishlist/',views.wishlist,name="wishlist"),
     path('matched/',views.matched,name="matched"),
    path('add/<str:id>',views.add,name="add"),
    path('remove/<str:id>',views.remove,name="remove"),


]