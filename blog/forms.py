from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']

#1:N

# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ["title", "content"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]