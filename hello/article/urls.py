from django.urls import path

from article.views import (
    IndexView,
    ArticleView,
    CreateArticleView,
    ArticleUpdateView,
    ArticleCommentCreate,
    ArticleDeleteView,
    ArticleLike,
    ArticleUnlike,
    CommentLike,
    CommentUnlike
)



app_name = 'article'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('add/', CreateArticleView.as_view(), name='add'),
    path('<int:pk>/', ArticleView.as_view(), name='view'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='delete'),
    path('<int:pk>/comments/add/', ArticleCommentCreate.as_view(), name='comment-create'),
    path('<int:pk>/article_like', ArticleLike.as_view(), name='article_like'),
    path('<int:pk>/article_unlike', ArticleUnlike.as_view(), name='article_unlike'),
    path('<int:pk>/comment_like', CommentLike.as_view(), name='comment_like'),
    path('<int:pk>/comment_unlike)', CommentUnlike.as_view(), name='comment_unlike')
]

