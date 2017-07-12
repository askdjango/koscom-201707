from django import forms

def min_length(min_value):
    def wrap(value):
        if len(value) < min_value:
            raise forms.ValidationError('최소 {}글자 이상 이벽해주세요.'.format(min_value))
    return wrap

