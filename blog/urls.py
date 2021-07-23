from django.urls import path
from .views import home, post_detail, about, contact, search


urlpatterns = [
    # path(url-name, function)
    path('', home),
    path('posts/<int:id>', post_detail),
    path('about', about),
    path('contact', contact),
    path('search', search)
]
