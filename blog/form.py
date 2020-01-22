from django import forms

from .models import Post, Comment
from .widgets import DatePickerWidget
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'name','gender','text','phone_no',
        			'published_date')
        widgets = {
        	'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ), 
            'phone_no': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'published_date': forms.DateTimeInput(attrs={'class':'datetime-input'}),
         
        }        

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
