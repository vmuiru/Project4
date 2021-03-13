from django.forms import ModelForm, TextInput
from .models import Comment, Category



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'date']

class UpdateCommentForm (ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'date']

class CategoryForm (ModelForm):
    class Meta:
        model = Category
        fields = ['name']