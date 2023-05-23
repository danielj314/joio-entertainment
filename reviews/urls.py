from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('review_form', views.review_form, name='review_form'),
    path('submit_review', views.submit_review, name='submit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),

]
