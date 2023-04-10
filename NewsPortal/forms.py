from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):

    content = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'post_author',
            'post_title',
            'post_text',
            'post_categories',
        ]

    def clean(self):
        cleaned_data = super().clean()
        post_title = cleaned_data.get("post_title")
        post_text = cleaned_data.get("post_text")

        if post_title == post_text:
            raise ValidationError(
                "Заголовок не должен быть идентичным содержанию."
            )

        return cleaned_data