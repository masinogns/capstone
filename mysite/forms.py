from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms

class CreateUserForm(UserCreationForm): # 내장 회원가입 폼을 상속받아서 확장한다.
    email = forms.EmailField(required=True) # 이메일 필드 추가
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "password1", "password2")

    def save(self, commit=True): # 저장하는 부분 오버라이딩
        user = super(UserCreationForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다.
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]

        if commit:
            user.save()

        return user
