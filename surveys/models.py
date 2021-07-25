from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


CHOICES = (("Text", "Textfield"), ("One", "Onechoice"), ("Many", "Manychoice"))


class Question(models.Model):
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="questions"
    )
    text = models.TextField()
    type_of_answer = models.CharField(choices=CHOICES, max_length=4)

    def __str__(self):
        return f"{self.pk} - {self.type_of_answer} - {self.text[:20]}"


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    text = models.TextField()

    def __str__(self):
        return self.pk
