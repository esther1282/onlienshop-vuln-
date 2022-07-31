from django import forms
from .models import Post
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

class WriteForm(forms.ModelForm):
    title = forms.CharField(
        label='글 제목',
        widget = forms.TextInput(attrs={'placeholder': '게시글 제목'}),
        required=True,
    )
    content = SummernoteTextField()
    is_secret = forms.BooleanField(label="비밀글")

    class Meta:
        model = Post
        fields = ['title', 'content', 'is_secret']
        widgets = {'content': SummernoteWidget()}

    def __init__(self, *args, **kwargs):
        super(WriteForm, self).__init__(*args, **kwargs)
        self.fields['is_secret'].required = False

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        content = cleaned_data.get('content', '')
        is_secret = cleaned_data.get('is_secret', '')

        if title == '':
            self.add_error('title', '글 제목을 입력해주세요')
        elif content == '':
            self.add_error('content', '글 내용을 입력해주세요')
        else:
            self.title = title
            self.content = content
            self.is_secret = is_secret