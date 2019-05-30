# -*- coding: utf-8 -*
from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import get_user_model
import logging
from django.contrib.auth.decorators import login_required

# Create your views here.
# post_list라는 함수(def) 만들어 요청(request)을 넘겨받아
# render메서드를 호출한다.
# 이 함수는 호출하여 받은 (return) blog/post_list.html 템플릿을 보여준다.

# render 함수에는 매개변수 request 와 blog/post_list.html 템플릿이 있다.
# {} 이곳에 템플릿을 사용하기 위해 매개변수를 추가할 것이다.
# {'posts': posts} 이렇게.. : 이전에 문자열이 와야하고, 작은따옴표를 양쪽에 붙여야 한다.

'''
def get_user(request):
    from django.contrib.auth.models import AnonymousUser
    try:`
        user_id = request.session[SESSION_KEY]
        backend_path = request.session[BACKEND_SESSION_KEY]
        backend = load_backend(backend_path)
        user = backend.get_user(user_id) or AnonymousUser()
    except KeyError:
        user = AnonymousUser()
    return user
'''

'''
def get_user(request):
    if not hasattr(request, '_cached_user'):
        request._cached_user = auth.get_user(request)
    return request._cached_user
'''


# 리스트
@login_required
def post_list(request):
    logging.info("■ post_list")
    # posts = Post.objects.filter(
    # published_date__lte = timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list2.html', {'posts': posts})

# 포스트 상세 내용
def post_detail(request, pk):
    logging.error("■ post_detail")
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 포스트 입력하는 폼
@login_required
def post_new(request):
    logging.error("■ post_new request.method : " + request.method)
    logging.error("・get user : " + str(get_user_model()))
    logging.error("・request.user1 : " + str(request.user))
    # logging.error("・ano : " + AnonymousUser())
    # logging.error("・boolean anonymous : " + str(request.user.is_anonymous()))
    # logging.error("・request.user : " + str(get_user_model().objects.get(username='eunji.song')))
    # 포스트 저장하기
    if request.method == "POST":
        form = PostForm(request.POST)
        '''
        # if (request.user is None or type(request.user) == AnonymousUser):
        #    from django.contrib.auth.models import AnonymousUser
        #    request.user = AnonymousUser()
            # if request.user.AnonymousUser() is True:
            # User.objects.all()
            # User객체를 생성
            # User = get_user_model()
            # me = User.objects.get(username='eunji.song')
'''
        if form.is_valid():
            post = form.save(commit=False)
            # 어드민 부분이 개발이 덜 됐으므로 미리 수동으로 넣어줌
            post.author = get_user_model().objects.get(username='eunji.song')
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# 포스트 수정하기
@login_required
def post_edit(request, pk):
    logging.error("■ post_edit request.method"+ request.method)
    logging.error("・get user : " + str(get_user_model()))
    #logging.error("・request.user : "+ str(get_user_model().objects.get(username='eunji.song')))
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # if request is not post, initialize an empty form
        form = PostForm(request.POST, instance=post)
        # form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # 서버쪽에 어드민이 로그인 되어 있지 않으면 AnonymousUser로 에러가 나옴
            # 테스트를 위해 어드민을 리퀘스트 받지 않고 임의로 넣어준다.
            post.author = get_user_model().objects.get(username='eunji.song')
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'app/users_detail.html', {'user':user})
