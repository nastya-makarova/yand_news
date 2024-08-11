import pytest

from django.test.client import Client

from news.models import Comment, News


@pytest.fixture
def author(django_user_model):
    """Фиктсутра возвращает автора комментария."""
    return django_user_model.objects.create(username='Автор')


@pytest.fixture
def not_author(django_user_model):
    """Фиктсутра возвращает обычного пользователя, не автора комментария."""
    return django_user_model.objects.create(username='Не автор')


@pytest.fixture
def author_client(author):
    """Фикстура возвращает клиента, авторизованного для автора."""
    client = Client()
    client.force_login(author)
    return client


@pytest.fixture
def not_author_client(not_author):
    """Фикстура возвращает клиента, авторизованного 
    для обычного пользователя не автора.
    """
    client = Client()
    client.force_login(not_author)
    return client


@pytest.fixture
def news():
    """Фикстура возвращает объект новости."""
    news = News.objects.create(
        title='Заголовок', text='Текст'
    )
    return news


@pytest.fixture
def comment(news, author):
    """Фикстура возвращает объект комментария."""
    comment = Comment.objects.create(
        news=news,
        author=author,
        text='Текст комментария'
    )
    return comment


@pytest.fixture
def news_id_for_args(news):
    return (news.id,)


@pytest.fixture
def comment_id_for_args(comment):
    return (comment.id,)
