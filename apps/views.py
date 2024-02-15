from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from apps.forms import BlogForm
from apps.models import Blog


# Create your views here.


class IndexView(ListView):
    template_name = 'index.html'
    queryset = Blog.objects.all()
    context_object_name = 'blogs'


class AddBlogView(CreateView):
    template_name = 'add.html'
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('index')


class DeleteBlogView(DeleteView):
    model = Blog
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        send_mail(
            'Your data has been deleted',
            'Sizning malumotlaringiz ochirildi.',
            '',
            [instance.author.email],
            fail_silently=False,
        )
        return super().delete(request, *args, **kwargs)
