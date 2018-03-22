from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    # Default template name: post_list.html
    template_name = 'ginko/index.html'
    # Default context variable is `post_list`
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-create_time')[:5]


class DetailView(generic.DetailView):
    model = Post
    # Default template name: post_detail.html
    template_name = 'ginko/detail.html'

