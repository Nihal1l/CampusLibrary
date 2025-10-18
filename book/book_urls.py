from django.urls import path
from book import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book-list'),
    path('<int:id>/', views.BookDetails.as_view(), name='book-details'),
]