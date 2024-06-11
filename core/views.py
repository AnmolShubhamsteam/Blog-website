from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from core.models import Post,User,Category
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.views.generic import DeleteView
from core.forms import PostForm,EditForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import UserIsOwnerMixin
import re
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
#     query=Post.objects.all()
#     context={"posts":query}
#     return render(request,"home.html",context)

# A list view that displays a list of all of the objects of one model in minimal detail, e.g., just the listing title, or just the band name.

# A detail view that displays one object in full detail with all fields displayed. 


class home(LoginRequiredMixin,ListView):
    model=Post
    template_name="home.html"
    ordering=["-id"]

class article(LoginRequiredMixin,DetailView):
    model=Post
    template_name="article_details.html"

class addblog(LoginRequiredMixin,CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'

class editblog(LoginRequiredMixin,UserIsOwnerMixin,UpdateView):
    model=Post
    form_class=EditForm
    template_name='update_post.html'
    # fields=["title","body"]

class deleteblog(LoginRequiredMixin,UserIsOwnerMixin,DeleteView):
    model=Post
    template_name="delete_post.html"
    success_url = reverse_lazy('home')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login_page.html", {})

def sign_up(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
        if not password_regex.match(password1):
            messages.error(request, "Password must contain at least one lowercase letter, one uppercase letter, one digit, and be at least 8 characters long.")
            return render(request, 'sign_up.html')
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'sign_up.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'sign_up.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'sign_up.html')
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        
        messages.success(request, "User created successfully.")
        return redirect("login")
    
    return render(request, "sign_up.html")

def log_out(request):
    logout(request)
    return redirect("login")

@login_required
def addCategory(request):
    if request.method == "POST":
        category_new = request.POST.get("category")
        if Category.objects.filter(name=category_new).exists():
            # Handle the case where the category already exists
            pass
        else:
            Category.objects.create(name=category_new)
            return redirect("home")
    return render(request, "add_category.html", {})

@login_required
def ListCategories(request):
    query=Category.objects.all()
    context={"Categories":query}
    return render(request,"showcategories.html",context)

@login_required
def Specific_categories(request, pk):
    category = Category.objects.get(id=pk)
    posts = Post.objects.filter(category=category)
    context = {
        "posts": posts
    }
    return render(request, 'specific_category.html', context)
