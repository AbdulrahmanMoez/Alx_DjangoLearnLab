from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.views.generic.detail import DetailView
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = self.object.books.all()
        return context

class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class LoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True

class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    next_page = reverse_lazy('login')

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
@permission_required('Library.can_add_books', raise_exception=True)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
@permission_required('Library.can_change_book', raise_exception=True)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
@permission_required('Library.can_delete_book', raise_exception=True)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
