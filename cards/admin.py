from django.contrib import admin
from .models import DailyReflection, WeeklyReflection, UnitReflection, Category, Question, Progress, Quiz
from .models import CSVUpload
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from mcq.models import MCQQuestion, Answer
from django.utils.translation import ugettext_lazy as _


class CSVUploadsAdmin(admin.ModelAdmin):
    model = CSVUpload
    list_display = ("title",)


class AnswerInline(admin.TabularInline):
    model = Answer


class QuizAdminForm(forms.ModelForm):
    """
    below is from
    http://stackoverflow.com/questions/11657682/
    django-admin-interface-using-horizontal-filter-with-
    inline-manytomany-field
    """

    class Meta:
        model = Quiz
        exclude = []

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(),
        required=False,
        label=_("Questions"),
        widget=FilteredSelectMultiple(verbose_name=_("Questions"), is_stacked=False),
    )

    def __init__(self, *args, **kwargs):
        super(QuizAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields[
                "questions"
            ].initial = self.instance.question_set.all().select_subclasses()

    def save(self, commit=True):
        quiz = super(QuizAdminForm, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data["questions"])
        self.save_m2m()
        return quiz


class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm

    list_display = (
        "title",
        "category",
    )
    list_filter = ("category",)
    search_fields = (
        "description",
        "category",
    )


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("category",)


class MCQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "category",
    )
    list_filter = ("category",)
    fields = ("content", "category", "figure", "quiz", "explanation", "answer_order")

    search_fields = ("content", "explanation")
    filter_horizontal = ("quiz",)

    inlines = [AnswerInline]


class ProgressAdmin(admin.ModelAdmin):
    """
    to do:
            create a user section
    """

    search_fields = (
        "user",
        "score",
    )


class DailyReflectionAdmin(admin.ModelAdmin):
    readonly_fields = ["author"]

class WeeklyReflectionAdmin(admin.ModelAdmin):
    readonly_fields = ["author"]

class UnitReflectionAdmin(admin.ModelAdmin):
    readonly_fields = ["author"]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MCQQuestion, MCQuestionAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(CSVUpload, CSVUploadsAdmin)
admin.site.register(DailyReflection, DailyReflectionAdmin)
admin.site.register(WeeklyReflection, WeeklyReflectionAdmin)
admin.site.register(UnitReflection, UnitReflectionAdmin)