from django.urls import path
from my_diary.apps import MyDiaryConfig
from my_diary.views import Home, why_diary_view, hello_view, how_start_view, DiaryListView, \
    DiaryDetailView, DiaryUpdateView, DiaryDeleteView, DiaryCreateView, DiarySearchView

app_name = MyDiaryConfig.name

urlpatterns = [
    path('', Home.as_view(), name='index'),
    # path('question/', question_view, name='question'),
    path('about/', hello_view, name='about'),
    path('why_diary/', why_diary_view, name='why_diary'),
    path('how_start/', how_start_view, name='how_start'),
    path('diary_list/', DiaryListView.as_view(), name='diary_list'),
    path('diary/<int:pk>/detail/', DiaryDetailView.as_view(), name='diary_detail'),
    path('diary/<int:pk>/update/', DiaryUpdateView.as_view(), name='diary_update'),
    path('diary/<int:pk>/delete/', DiaryDeleteView.as_view(), name='diary_delete'),
    path('diary/create/', DiaryCreateView.as_view(), name='diary_create'),
    path('search/', DiarySearchView.as_view(), name='diary_search'),
]
