from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         # id, password, password2 만 입력받음
#         model = get_user_model()
#         fields = UserCreationForm.Meta.fields


class CustomUserCreationForm(UserCreationForm):
    # model 속성을 제외하고는 나머지는 모두 meta 클래스 내용을 그대로 가져올 때
    # 아래처럼 Meta class 도 상속받아서 써도 된다.
    class Meta(UserCreationForm.Meta):
        model = get_user_model()