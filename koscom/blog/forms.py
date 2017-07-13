from django import forms
from .models import Post


'''
class PostForm(forms.Form):
    author = forms.CharField()
    title = forms.CharField()
    content = forms.CharField()
'''


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__' # 혹은 list

    def clean_title(self):
        title = self.cleaned_data['title']
#       if len(title) < 10:
#           raise forms.ValidationError('10글자 이상!!!')
        return title.replace('_', '')  # 변환된 값으로 cleaned_data 에 저장

