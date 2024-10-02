from django.forms import ModelForm

from my_diary.models import Diary


class DiaryForm(ModelForm):

    class Meta:
        model = Diary
        fields = '__all__'