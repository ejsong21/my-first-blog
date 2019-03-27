# -*- coding: utf-8 -*-
from django.utils import timezone
from .models import Post
from django.shortcuts import render,redirect, get_object_or_404
from .forms import PostForm
from django.contrib.auth.models import User
import logging

# Create your views here.
# post_list라는 함수(def) 만들어 요청(request)을 넘겨받아
# render메서드를 호출한다.
# 이 함수는 호출하여 받은 (return) blog/post_list.html 템플릿을 보여준다.

#render 함수에는 매개변수 request 와 blog/post_list.html 템플릿이 있다.
# {} 이곳에 템플릿을 사용하기 위해 매개변수를 추가할 것이다.
# {'posts': posts} 이렇게.. : 이전에 문자열이 와야하고, 작은따옴표를 양쪽에 붙여야 한다.

# 리스트
def post_list(request):
    logging.info("-------------------------post_list1")
    #posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list2.html', {'posts':posts})

# 포스트 상세 내용
def post_detail(request, pk):
    logging.info("-------------------------post_detail1")
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

# 포스트 입력하는 폼    
def post_new(request):
    logging.error("-------------------------■post_new1 request.method : "+ request.method)
    print("-------------------------■request.user : "+ str(request.user))
    # 포스트 저장하기
    if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
            post = form.save(commit=False)
            # User객체로 author를 넣어야 한다고 자꾸 에러가 남..그래서 강제로 포스트 할 유저를 넣음.
            me = User.objects.get(username='eunji.song')
            # post.author = request.user
            post.author = me
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})
    
# 포스트 수정하기
def post_edit(request, pk):
    logging.error("-------------------------■post_edit1"+ request.method)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # if request is not post, initialize an empty form
        form = PostForm(request.POST, instance=post)
        #form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})
     
    
    
    
''' 
def getVideoTitle(ch, term_start, term_end, next):
  # チャンネルの指定期間内の動画一覧を取得
  request = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?channelId=" + ch + "&part=id,snippet" + term_start + term_end + "&maxResults=50&key=***your api key***" + next)
  response = request.read()  # 文字列が返ってくる
  data = json.loads(response) #文字列をjson化

  id_list = []
  title_list = []
  for d in data["items"]:
    if "videoId" in d["id"]:
      id_list.append(d["id"]["videoId"])
      title_list.append(d["snippet"]["title"])

  videoid = "&id=" + ','.join(id_list)
  titles = []
  if len(id_list) > 0:
    # 取得した動画の再生数を取得し判定後，タイトルリストに追加
    request = urllib.urlopen("https://www.googleapis.com/youtube/v3/videos?part=statistics" + videoid + "&fields=items(statistics)&key=***your api key***")
    response = request.read()
    count = 0
    for item in json.loads(response)["items"]:
      if int(item["statistics"]["viewCount"]) > 1000000:  # 任意の再生数を指定
        titles.append(title_list[count])
      count += 1

  if "nextPageToken" in data["items"]:
    npt = data["nextPageToken"]
  else:
    npt = ""

  return [npt, titles]
'''

    



     