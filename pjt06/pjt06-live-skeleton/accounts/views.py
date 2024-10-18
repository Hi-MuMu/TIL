from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm


# Create your views here.
'''
1. 회원 가입 기능
2. 로그인
3. 로그아웃
+ 회원 탈퇴, 회원정보 수정, 비밀번호 수정(도전과제)
4. 게시글 작성자만 삭제 및 수정
5. 댓글 작성자만 삭제 및 수정

함수를 다 작성하고 실행하지 말고
하나씩 하면서 해야함 로그인 먼저 만들고 로그인부터 진행 완료되고 이제 로그아웃을 만들기
즉 기능하나 만들고 테스트 하기
'''
@require_http_methods(["GET", "POST"])
def signup(request):
    # 바로 가져다 쓰지 못하는 이유는?
    # 이유: 기본 Auth User를 바라보기 때문에(장고는) 우리의 커스텀 유저를 보게 해야함 
    # form = UserCreationForm() -- > X
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원 가입 후 바로 로그인
            auth_login(request,user)
            return redirect("boards:index")
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # next가 있다면, next 경로로 보내라
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            
            return redirect("boards:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)

@require_http_methods(["POST"])
def logout(request):
    # DB 에서 세션 삭제, 쿠키에서 세션ID 삭제 등등
    auth_logout(request)
    return redirect("boards:index")