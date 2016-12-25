from django import forms
import bootstrapform
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=200)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
	class Meta:
		model= Comment
		fields = ('author', 'body')



