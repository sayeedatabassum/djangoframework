from django.urls import path
from jobapp import views

urlpatterns = [
	path('bangalore/', views.bangalore_job),
    path('mysore/', views.mysore_job),
    path('mumbai/', views.mumbai_job),
]