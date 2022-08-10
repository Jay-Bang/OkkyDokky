from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class QuestionTable(models.Model):
    post_url = models.URLField()
    post_title = models.CharField(max_length=100)
    total_comment = models.IntegerField()
    post_datetime = models.DateTimeField()
    post_content = models.TextField()
    post_component = models.CharField(max_length=20, null=True, blank=True)
    code_lang = models.CharField(max_length=20, blank=True)
    checked_answer = models.TextField(blank=True)
    answer_datetime = models.DateTimeField(blank=True)
    customer = models.ManyToManyField(Customer, blank=True)

    def __str__(self):
        return self.post_url

class DataStats(models.Model):
    year = models.IntegerField()
    total_data = models.IntegerField()
    no_answer = models.IntegerField()
    answer = models.IntegerField()
    unchecked_answer = models.IntegerField()
    checked_answer = models.IntegerField()
    answer_ratio = models.IntegerField()
    checked_answer_ratio = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.year)

class CodeStats(models.Model):
    code_language = models.TextField()
    total_used = models.IntegerField(blank=True)

    def __str__(self):
        return self.code_language