from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.

'''def index(request):

    post=Post.objects.all()
    return render(request,"base.html",{"post":post})'''

#class based view for index

class PostListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "post"
    ordering = ["-date_posted"]
    paginate_by = 2

class PostDetailView(DetailView):

    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):

    model = Post
    fields = ["title","content"]
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

    model = Post
    fields = ["title","content"]
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeletelView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):

    model = Post
    success_url = "/"
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}!')
            return redirect("login")



    else:
        form = UserRegistrationForm()
    return render(request, "registernew.html", {"form": form})


@login_required
def profile(request):
    if request.method=="POST":

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'your account has been updated!')
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)


    context={
        "u_form":u_form,
        "p_form":p_form,
    }

    return render(request,"profile.html",context)


