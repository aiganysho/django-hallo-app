from django import forms

from article.models import Article, Comment


class ArticleForm(forms.ModelForm):
    """
    Форма для создания и редактирваония объектов статьи
    https://docs.djangoproject.com/en/3.1/ref/forms/
    """
    class Meta:
        model = Article
        fields = ('title', 'content', 'tags')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')
