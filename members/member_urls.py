from django.urls import path
from book import views

urlpatterns = [
    path('', views.MemberList.as_view(), name='member-list'),
    path('<int:id>/', views.MemberDetails.as_view(), name='member-details'),
]