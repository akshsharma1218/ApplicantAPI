from django.urls import path
from . import views

urlpatterns = [
    path('',views.ApplicantListCreateView.as_view(),name='list-create'),
    path('<int:pk>',views.ApplicantUpdateDeleteView.as_view(),name='update-delete'),
]