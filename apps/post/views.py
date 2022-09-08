from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from apps.post.models import Post
from .models import AboutUs, Category
from django.shortcuts import render, redirect, get_object_or_404   
from .forms import CreatePostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models import Q


def PostAbout(request):
    about = AboutUs.objects.all()
    
    context = {
        'about': about
    }
    return render(request, 'blog/about-us.html', context)


def Home(request):
    return render(request, 'blog/index.html')



def Contact(request):
    return render(request, 'blog/contact-us.html')


def NotFound(request, exception=None):
    return render(request, 'blog/404.html',)



def Blog(request):
    return render(request, 'blog/blog-item.html',)


def PostListView(request):
    
    category = request.GET.get('category')
    
    if category == None:
        posts = Post.objects.all
    else:
        posts = Post.objects.filter(category__name=category)
    
    posts = Post.objects.all().order_by('-date_created')
    
    page_num = request.GET.get("page")
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    categories = Category.objects.all().annotate(posts_count=Count('post'))
    
    context = {
        'posts': posts,
        'category': categories,
    }
    
    return render(request, 'blog/blogs.html', context)


def PostDetailView(request, slug=None):
    
    post = Post.objects.get(slug=slug)
    related_posts = Post.objects.filter(category=post.category).exclude(slug=slug)
    context = {
        'post': post,
        'related_posts' : related_posts
    }
    return render(request, 'blog/blog-item.html', context)


def CategoryListView(request, slug=None):    
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).order_by('-date_created')
    cate = Category.objects.get(slug=slug)
    
    page_num = request.GET.get("page")
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    categories = Category.objects.all().annotate(posts_count=Count('post'))
    
    context = {
        'cate':cate,
        'category': category,
        'posts' : posts,
        'categories': categories
    }
    return render(request, 'blog/category-item.html', context)


@login_required()
def PostCreateView(request):
    form = CreatePostForm()
    
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            posts = Post(user=request.user, title=request.POST['title'], postText=request.POST['postText'], category=form.cleaned_data['category'])
            posts.save()
            return redirect('post:blog-home')
        else:
            form = CreatePostForm()
    form = CreatePostForm()
    context = {
        'form': form
    }
    return render(request, 'blog/post_create.html', context)


@login_required()
def PostUpdateView(request, slug=None):
    post = Post.objects.get(slug=slug)
    
    form = CreatePostForm(instance=post)
    
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid:
            form.save()
            return redirect('post:blog-home')
        
    context = {
        'form': form
    }
        
    return render(request, 'blog/post_create.html', context)

@login_required()
def PostDeleteView(request, slug=None):
    post = Post.objects.get(slug=slug)
    post.delete()
    return redirect("post:blog-home")


def SearchBar(request):
    if request.method == "GET":
        posts = Post.objects.all()
        query = request.GET.get('query')
        if query:
            posts = Post.objects.filter(Q(title__icontains=query) | Q(postText__icontains=query)).distinct().order_by('-date_created')
            
            page_num = request.GET.get("page")
            paginator = Paginator(posts, 5)
            try:
                posts = paginator.page(page_num)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage: 
                posts = paginator.page(paginator.num_pages)
            
            return render(request, 'blog/search.html', {'posts':posts, 'query':query})
        else:
            print("No information found")
            return render(request, 'blog/search.html', {})
        
    
    
    
  