from django.contrib import admin

from .models import Question, Choice
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3



# admin.site.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["question_text"]}),
#         ("Date information", {"fields": ["pub_date"]}),
#     ]

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    

# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)

