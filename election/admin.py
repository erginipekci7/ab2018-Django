from django.contrib import admin
from election.models import Survey
from election.models import Question
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class SurveyResource (resources.ModelResource):
    class Meta:
        model = Survey
        fields = ('id', 'name', 'created_at', 'active', )

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created_at', 'updated_at',)
    list_filter = ('active',)
    search_fields = ('name',)
class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'survey', 'choice_one', 'choice_two', 'choice_three', 'choice_four',)
    search_fields = ('title',)


admin.site.register(Survey,SurveyAdmin)
admin.site.register(Question,QuestionAdmin)
