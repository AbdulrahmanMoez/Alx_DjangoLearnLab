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

def Admin(user):
    return user.userprofile.role == 'Admin'

def Librarian(user):
    return user.userprofile.role == 'Librarian'

def Member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(Admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(Librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(Member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



