from django.forms import ModelForm

from apps.models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'email', 'name']

