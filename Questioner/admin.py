from django.contrib import admin

from Questioner.models import Survey, Answer, Question, Link


@admin.register(Survey)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Link)
class TaskAdmin(admin.ModelAdmin):
    pass
