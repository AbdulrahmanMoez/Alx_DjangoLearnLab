from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),  
    path('logout/', views.LogoutView.as_view(), name='logout'),

path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian-panel/', views.librarian_view, name='librarian_panel'),
    path('member-dashboard/', views.member_view, name='member_dashboard'),
]


