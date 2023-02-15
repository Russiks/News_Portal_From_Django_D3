from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


# Класс-представление для отображения списка постов. Унаследован от базового представления"ListView"
class PostList(ListView):
    model = Post  # Указываем имя модели, которая будет использоваться для отображения и реализации логики
    template_name = 'flatpages/news.html'  # Указываем имя шаблона, то есть html файла, который будет использоваться
    # для визуализации
    context_object_name = 'news'  # Имя, которое будет использоваться для передачи переменных в шаблон
    queryset = Post.objects.order_by('-dateCreation')
    # ordering = ['-id']  # Задаем последовательность отображения по id
    # paginate_by = 10  # Задаем кол-во отображаемых объектов на странице

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # добавим переменную текущей даты time_now
        context['time_now'] = datetime.utcnow()
        # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['value1'] = None
        return context


# Класс-представление, созданное для поиска объектов по фильтрам
class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'
# Create your views here.