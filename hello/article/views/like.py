from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import View

from article.models import Article, Comment

class ArticleLike(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        article = Article.objects.get(pk=pk)

        if request.user in article.like.all():
            pass
        else:
            article.like.add(request.user)
            return HttpResponse(article.like.count())


class ArticleUnlike(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        article = Article.objects.get(pk=pk)
        if request.user in article.like.all():
            article.like.remove(request.user)
            return HttpResponse(article.like.count())

        else:
            return HttpResponseForbidden("error")

class CommentLike(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        comment = Comment.objects.get(pk=pk)

        if request.user in comment.like.all():
            pass
        else:
            comment.like.add(request.user)
            return HttpResponse(comment.like.count())


class CommentUnlike(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        comment = Comment.objects.get(pk=pk)
        if request.user in comment.like.all():
            comment.like.remove(request.user)
            return HttpResponse(comment.like.count())

        else:
            return HttpResponseForbidden("error")



