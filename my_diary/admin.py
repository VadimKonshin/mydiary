from django.contrib import admin

from my_diary.models import Diary


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions', 'owner', 'text_diary',)
    search_fields = ('title', 'descriptions',)
    list_filter = ('title', )