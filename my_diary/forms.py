from django.forms import ModelForm, CheckboxInput

from my_diary.models import Diary


class StyleFormMixin:
    '''Класс стилей'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class DiaryForm(StyleFormMixin, ModelForm):
    '''Форма для дневника'''

    class Meta:
        model = Diary
        fields = '__all__'
        exclude = ('owner',)
