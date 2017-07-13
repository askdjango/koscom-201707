from django import forms
from django.utils.deconstruct import deconstructible


@deconstructible
class MinLengthValidator:
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) < self.min_length:
            raise forms.ValidationError('최소 {}글자 이상 입력해주세요.'.format(self.min_length))

