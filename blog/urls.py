from django.urls import path
from .views import home, post_detail, about


urlpatterns = [
    # path(url-name, function)
    path('', home),
    path('posts/<int:id>', post_detail),
    path('about', about)
]
