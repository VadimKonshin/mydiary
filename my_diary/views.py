from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView

from my_diary.forms import DiaryForm
from my_diary.models import Diary


class Home(TemplateView):
    template_name = 'my_diary/home.html'


def question_view(request):
    return render(request, template_name='my_diary/question.html')


def hello_view(request):
    return render(request, template_name='my_diary/about.html')


def why_diary_view(request):
    return render(request, template_name='my_diary/why_diary.html')


def how_start_view(request):
    return render(request, template_name='my_diary/how_start.html')


class DiaryListView(ListView):
    model = Diary

    def get_queryset(self):
        if self.request.user.is_superuser:
            return super().get_queryset()
        return super().get_queryset().filter(owner=self.request.user)


class DiaryDetailView(DetailView):
    model = Diary


class DiaryUpdateView(UpdateView):
    model = Diary
    form_class = DiaryForm
    success_url = reverse_lazy('my_diary:diary_list')

class DiaryCreateView(CreateView):
    model = Diary
    form_class = DiaryForm
    success_url = reverse_lazy('my_diary:diary_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DiaryDeleteView(DeleteView):
    model = Diary
    success_url = reverse_lazy('my_diary:diary_list')
