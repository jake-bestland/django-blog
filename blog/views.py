from django.shortcuts import render
from .models import Post
from django.views import generic


# Create your views here.
# def index(request):
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request, 'blog/index.html', context)

class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

# def detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     context = {'post': post}
#     return render(request, 'blog/detail.html', context)