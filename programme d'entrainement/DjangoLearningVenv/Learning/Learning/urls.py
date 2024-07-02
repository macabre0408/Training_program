
from django.contrib import admin
from django.urls import path
from Listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name="band_list"),
    path('bands/<int:id>', views.band_detail, name="band_detail"),
    path('about us/', views.aboutUs),
    path('contact us/', views.contact, name='contact'),
    path('listings/', views.listings_list, name='listings-list'),
    path('listings/<int:id>', views.listings_detail, name='listings-detail'),
    path('bands/add', views.band_create, name='band-create'),
]
