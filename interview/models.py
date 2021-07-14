from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Question(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	question_text = models.CharField(max_length = 200)
	timer = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.question_text



class Interview(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	question = models.ManyToManyField(Question)
	is_finished = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return str(self.user)
