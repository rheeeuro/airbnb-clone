from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField(label="이메일")
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
