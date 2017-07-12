from django import forms

def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError('최소 3글자 이상 이벽해주세요.')
