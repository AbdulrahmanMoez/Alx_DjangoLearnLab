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

def admin_view(request):
    # Logic for the admin view
    return render(request, 'admin_view.html')

@user_passes_test(lambda u: u.userprofile.role == 'admin')
def admin_restricted_view(request):
    # Logic for the admin-only view
    return render(request, 'admin_restricted_view.html')

@user_passes_test(lambda u: u.userprofile.role == 'librarian')
def librarian_view(request):
    # Logic for the librarian view
    return render(request, 'librarian_view.html')

@user_passes_test(lambda u: u.userprofile.role == 'member')
def member_view(request):
    # Logic for the member view
    return render(request, 'member_view.html')
