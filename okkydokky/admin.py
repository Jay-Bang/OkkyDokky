from django.contrib import admin
from .models import QuestionTable, DataStats, CodeStats


class QuestionTableAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'post_url',
        'post_title',
        'total_comment',
        'post_datetime',
        'post_content',
        'post_component',
        'code_lang',
        'checked_answer',
        'answer_datetime',
    ]
    search_fields = [
        'id',
        'post_url',
        'post_title',
        'total_comment',
        'post_datetime',
        'post_content',
        'post_component',
        'code_lang',
        'checked_answer',
        'answer_datetime',
    ]

admin.site.register(QuestionTable, QuestionTableAdmin)


class DataStatsAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'year',
        'total_data',
        'no_answer',
        'answer',
        'unchecked_answer',
        'checked_answer',
        'answer_ratio',
        'checked_answer_ratio',
    ]
    search_fields = [
        'id',
        'year',
        'total_data',
        'no_answer',
        'answer',
        'unchecked_answer',
        'checked_answer',
        'answer_ratio',
        'checked_answer_ratio',
    ]

admin.site.register(DataStats, DataStatsAdmin)


class CodeStatsAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'code_language',
        'total_used',
    ]
    search_fields = [
        'id',
        'code_language',
        'total_used',
    ]

admin.site.register(CodeStats, CodeStatsAdmin)