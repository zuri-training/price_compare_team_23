from django.forms import ModelForm
from category.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
