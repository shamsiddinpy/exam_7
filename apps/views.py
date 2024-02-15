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


class DeleteProductView(DeleteView):
    template_name = 'delete.html'
    model = Blog
    context_object_name = 'blog_delete'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, "Vazifa muvaffaqiyatli o'chirildi.")
        return super().form_valid(form)