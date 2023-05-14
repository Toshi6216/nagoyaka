from django.urls import path
from . import views

urlpatterns = [
    path('home/',  views.HomeView.as_view(), name="home"),
    path('index/',  views.IndexView.as_view(), name="index"),
    path('about/',  views.AboutView.as_view(), name="about"),
    path('products/',  views.ProductsView.as_view(), name="products"),
    path('store/',  views.StoreView.as_view(), name="store"),

]
