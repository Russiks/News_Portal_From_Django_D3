from django.urls import path
# from django.urls.resolvers import URLPattern
from django.urls import path
from .views import PostList, PostDetail  # Импортируем представления, написанные в файле "views.py"

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),  # pk — это первичный ключ новости или статьи, который будет выводиться у
    # нас в шаблон int — указывает на то, что принимаются только целочисленные значения
]
# Path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, чуть позже станет ясно почему.
# Т.к. наше объявленное представление является классом, а Django ожидает функцию, нам надо представить этот класс в
# виде view. Для этого вызываем метод as_view.