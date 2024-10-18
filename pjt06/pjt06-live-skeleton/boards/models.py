from django.db import models
from django.conf import settings

# Create your models here.
class Board(models.Model):
    # 실제 개발할 때는 on_delete를 어떻게 설정할까
    # - 유저가 지워졌을 때 어떻게 작업할래?
    # 유저 탈퇴 시 DB 에서 잘 안날린다.

    # - 아무 행동 안한다.
    # - admin 으로 변경
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'boards')
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'comments')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)