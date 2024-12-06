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
from django.http import HttpResponseForbidden

def user_is_admin(user):
    """
    Check if the user has an Admin role
    """
    return hasattr(user, 'profile') and user.profile.role == 'Admin'

def user_is_librarian(user):
    """
    Check if the user has a Librarian role
    """
    return hasattr(user, 'profile') and user.profile.role == 'Librarian'

def user_is_member(user):
    """
    Check if the user has a Member role
    """
    return hasattr(user, 'profile') and user.profile.role == 'Member'

@user_passes_test(user_is_admin)
def admin_view(request):
    """
    View accessible only to Admin users
    """
    context = {
        'admin_message': 'Welcome to the Admin Dashboard',
        'total_users': User.objects.count()
    }
    return render(request, 'relationship_app/admin_view.html', context)

@user_passes_test(user_is_librarian)
def librarian_view(request):
    """
    View accessible only to Librarian users
    """
    context = {
        'librarian_message': 'Librarian Management Panel',
        'recent_books': Book.objects.all()[:5]
    }
    return render(request, 'relationship_app/librarian_view.html', context)

@user_passes_test(user_is_member)
def member_view(request):
    """
    View accessible only to Member users
    """
    context = {
        'member_message': 'Your Personal Library Dashboard',
        'borrowed_books': Book.objects.filter(borrower=request.user)
    }
    return render(request, 'relationship_app/member_view.html', context)

