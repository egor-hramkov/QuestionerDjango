from django.db import models


class Survey(models.Model):
    """Модель опроса"""
    title = models.CharField(max_length=255, name="Название опроса")


class Question(models.Model):
    """Модель вопроса"""
    text = models.TextField(max_length=1000, name="Текст вопроса")
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name="Опрос", related_name="questions")


class Answer(models.Model):
    """Модель ответа"""
    text = models.CharField(max_length=255, verbose_name="Текст ответа")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос", related_name="answers")


class Link(models.Model):
    """Связь последовательности вопросов"""
    from_question = models.ForeignKey(Question, related_name='from_question', on_delete=models.CASCADE)
    to_question = models.ForeignKey(Question, related_name='to_question', on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, blank=True, null=True, on_delete=models.CASCADE)
