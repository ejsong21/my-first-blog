# -*- coding: utf-8 -*-
# from 으로 다른 파일에 있는 것을 추가함
from django.conf import settings
from django.db import models
from django.utils import timezone

# class모델을 정의함
# 모델의 이름은 Post
# models 는 Post가 장고 모델임을 의미함. 이코드 때문에 장고는 Post가
# 데이터베이스에 저장되어야한다고 알게됨
# models.CharField 짧은 문자열 정보
# models.TextField 글자수 제한없는 텍스트
# models.DateTimeField 날짜와 시간
# models.ForeignKey 다른 모델에 대한 링크
# def publish(self)는 publish라는 메서드
# def 는 이것이 함수/메서드라는 뜻임
# 메서드 이름은 소문자 나 언더스코어를 사용함
# 메서드는 무언가를 돌려줌 return
# 여기서는 __str__를 호출하면 Post모델의 제목 텍스트(string)를 받게 됨

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # cover = models.ImageField(upload_to='images/')
    profile_pic = models.ImageField(upload_to="blog/profile_pic")
    photo = models.ImageField(blank=True, upload_to="blog/%Y/%m/%d")

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Photo(models.Model):
    title = models.CharField (max_length = 150)
    comment = models.TextField (blank = True)
    image = models.ImageField (upload_to = 'photos')
    created_at = models.DateTimeField (auto_now = True)

    def __str__(self):
        return self.title

'''
class item(models.Model):
    purchase_url = models.URLField('product URL'), max_length=400, black=True)
    image_file = models.ImageField('product image'), upload_to='items', black=True)


class Work(models.Model):
    #作品モデル
    class Meta:
        db_table = 'work'

    name = models.CharField(verbose_name="作品名", max_length=255)
    memo = models.Charfield(verbose_name="メモ", max_length=255, default='', blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url(self):
        return reverse('pictures:index')
#    image = ThumbnailImageField(upload_to = 'photo/%y/%m')

class Image(models.Model):
    #イメージモデル
    class Meta:
        db_table = 'image'

    work = models.ForeignKey(Work, verbose_name='作品', on_delete=models.PROTECT)
    image = models.ImageField(upload_to="image/", verbose_name='イメージ')
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeFiled(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.work.name + ":" + str(self.data_datetime)
'''
