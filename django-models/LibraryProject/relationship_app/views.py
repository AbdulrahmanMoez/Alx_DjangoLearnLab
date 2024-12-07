from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Library, Book, Author
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView


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

    def get_context_data(self, kwargs):
        context = super().get_context_data(kwargs)
        context['book_list'] = self.object.books.all()
        return context

class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')
    
    
    

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib.auth.models import User

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    users = User.objects.all()
    return render(request, 'relationship_app/admin_view.html', {'users': users})

@user_passes_test(is_librarian, login_url='login')
def librarian_view(request):
    # Add librarian-specific logic here
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member, login_url='login')
def member_view(request):
    # Add member-specific logic here
    return render(request, 'relationship_app/member_view.html')
