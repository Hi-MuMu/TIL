from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from boards.models import Board, Comment


# Register your models here.
admin.site.register(User)
admin.site.register(Board)
admin.site.register(Comment)
