from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from blog.forms import ProfileUpdateForm, UserUpdateForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_published']
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'


@login_required
def author_profile(request, username):
    author = get_object_or_404(User, username=username)
    u_form = UserUpdateForm(instance=author)
    p_form = ProfileUpdateForm(instance=author.authorprofile)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=author)
        p_form = ProfileUpdateForm(
            request.POST, instance=author.authorprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('author-profile')

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'blog/author-profile.html', context)


class AuthorPostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        author = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=author).order_by('-date_published')


class CreatePostView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create-post.html'
    fields = ['title', 'content', 'cover_image']
    permission_required = 'can_create_post'
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePostView, self).form_valid(form)

    def success_message(self):
        return messages.success(self.request, 'Post has been published successfully.')


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/create-post.html'
    fields = ['title', 'content', 'cover_image']
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePostView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    permission_required = 'can_delete_post'
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def success_message(self):
        return messages.success(self.request, 'Post has been deleted successfully.')
