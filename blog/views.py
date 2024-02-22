from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.models import User
from .models import Post

# a list of dictionaries where each dictionary represents a blog post
# posts = [
#     {
#         'author': 'zheer',
#         'title': 'title of the post',
#         'content': 'content of the post',
#         'date_posted': 'February 16, 2024'
#     },
#     {
#         'author': 'Faruq',
#         'title': 'title of the post 2',
#         'content': 'content of the post 2',
#         'date_posted': 'February 17, 2024'
#     }
# ]

# function based views
def homePage(request):
    # dictionary that contains the data we want to pass in
    context = {
        'posts': Post.objects.all(),

        # 'posts': posts, # the key is the name of the variable we will use in the template
        # # and the value is the actual data we want to pass in
        # 'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

# class based views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering the posts by date posted in descending order meaning the most recent post will be the first post
    ordering = ['-date_posted'] # the - sign is used to reverse the order
    paginate_by = 5 # this will paginate the posts by 5 posts per page

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    # this method is used to get the posts of a particular user
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    #template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['title', 'content']

    # this method is used to set the author of the post to the current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['title', 'content']

    # this method is used to set the author of the post to the current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin ,DeleteView):
    model = Post
    success_url = '/' # this will redirect the user to the home page after deleting a post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        


def aboutPage(request):
    return render(request, 'blog/about.html')
# The views are the functions that handle the requests and return responses.
