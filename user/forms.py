from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.hashers import check_password
from .models import User, Profile_image, Flag

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'gender', 'phone_number', 'address']


class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control', }),
                               )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = '기존 비밀번호'
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': False,
        })
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Profile_image
        fields = ['image','title']

class FlagForm(forms.ModelForm):
    class Meta:
        model = Flag
        fields = ['xss1','xss2','sql1','sql2','traversal']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def check(self):

        if self.fields['xss1'] == 'flag':
            return 1
        else:
            return 0

    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('xss1')

        if data:
            if not self.check(data):
                self.add_error('xss1', 'flag가 일치하지 않습니다.')
