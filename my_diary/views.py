from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView

from my_diary.forms import DiaryForm
from my_diary.models import Diary


class Home(TemplateView):
    ''' класс отображения страницы home'''
    template_name = 'my_diary/home.html'


# def question_view(request):
#     return render(request, template_name='my_diary/question.html')


def hello_view(request):
    '''Функция для отображения страницы "о нас"'''
    return render(request, template_name='my_diary/about.html')


def why_diary_view(request):
    '''Функция для отображения страницы "зачем вести дневник"'''
    return render(request, template_name='my_diary/why_diary.html')


def how_start_view(request):
    '''Функция для отображения страницы "как начать"'''
    return render(request, template_name='my_diary/how_start.html')


class DiaryListView(ListView):
    '''Класс отображения дневников'''
    model = Diary

    def get_queryset(self):
        '''функция для отображения записей в дневнике'''
        if self.request.user.is_superuser:
            return super().get_queryset()
        return super().get_queryset().filter(owner=self.request.user)


class DiaryDetailView(DetailView):
    '''Класс для подробного отображения дневника'''
    model = Diary


class DiaryUpdateView(UpdateView):
    '''Класс для обновленя дневника'''
    model = Diary
    form_class = DiaryForm
    success_url = reverse_lazy('my_diary:diary_list')

    def get_object(self, queryset=None):
        '''функция ограничения доступа'''

        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            return self.object
        raise PermissionDenied


class DiaryCreateView(CreateView):
    '''Класс для создания дневника'''
    model = Diary
    form_class = DiaryForm
    success_url = reverse_lazy('my_diary:diary_list')

    def form_valid(self, form):
        '''функция автомтического присваивания владельца записи'''
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DiaryDeleteView(DeleteView):
    '''Класс для удаления дневника'''
    model = Diary
    success_url = reverse_lazy('my_diary:diary_list')

    def get_object(self, queryset=None):
        '''функция ограничения'''
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            return self.object
        raise PermissionDenied


class DiarySearchView(ListView):
    '''Класс для поиска дневника'''

    model = Diary
    template_name = 'my_diary/diary_list.html'

    def get_queryset(self):
        '''функция поиска'''
        query = self.request.GET.get('q')
        if query:
            return Diary.objects.filter(
                Q(title__icontains=query) | Q(text_diary__icontains=query)
            )
        else:
            return Diary.objects.all()
