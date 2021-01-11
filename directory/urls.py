from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='dir-home'),
    # path('create/', views.Home.as_view(), name='dir-create'),
    path('edit/<int:pk>', views.Home.as_view(), name='dir-edit'),
    path('filter/', views.Home.as_view(), name='dir-filter'),
    path('bulk-upload/', views.Home.as_view(), name='dir-bulkupload'),
    path('', views.Home.as_view(), name='dir-home'),
	path('detail/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
	path('create/', views.TeacherCreateView.as_view(), name='teacher-create')
]