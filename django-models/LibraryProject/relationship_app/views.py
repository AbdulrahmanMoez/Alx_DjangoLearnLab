from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Library, Book, Author
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

@login_required
def list_books(request):
    
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'book_list': books, 
        'authors': authors
    }
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = self.object.books.all()
        return context
    
    
class register(CreateView):
    form_class = UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')
class LoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True

class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    next_page = reverse_lazy('login')

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import User
def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'Admin'

@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    """
    View accessible only to Admin users
    """
    context = {
        'admin_message': 'Welcome to the Admin Dashboard',
        'total_users': User.objects.count()
    }
    return render(request, 'relationship_app/admin_view.html', context)

