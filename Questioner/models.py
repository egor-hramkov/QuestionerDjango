from django.db import models


class Survey(models.Model):
    """Модель опроса"""
    title = models.CharField(max_length=255, verbose_name="Название опроса")

    def __str__(self):
        return f"{self.id}: {self.title}"


class Question(models.Model):
    """Модель вопроса"""
    text = models.TextField(max_length=1000, verbose_name="Текст вопроса")
    survey = models.ManyToManyField(Survey, verbose_name="Опрос", related_name="questions")

    def __str__(self):
        return f"{self.id}: {self.text}"


class Answer(models.Model):
    """Модель ответа"""
    text = models.CharField(max_length=255, verbose_name="Текст ответа")
    question = models.ManyToManyField(Question, verbose_name="Вопрос", related_name="answers")

    def __str__(self):
        return f"{self.id}: {self.text}"


class Link(models.Model):
    """Связь последовательности вопросов"""
    from_question = models.ForeignKey(
        Question,
        related_name='from_question',
        on_delete=models.CASCADE,
        verbose_name="От какого вопроса"
    )
    to_question = models.ForeignKey(
        Question,
        related_name='to_question',
        on_delete=models.CASCADE,
        verbose_name="К какому вопросу"
    )
    survey = models.ForeignKey(
        Survey,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="links",
        verbose_name="В каком опросе"
    )

    def __str__(self):
        return f"От <{self.from_question.text}> к <{self.to_question.text}> в опросе <{self.survey.title}>"
