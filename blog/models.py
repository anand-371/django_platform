from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
	Subject=models.CharField(max_length=100)
	domain=models.CharField(max_length=10)
	Description=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	file= models.FileField(default='default.jpg')
	#likes=models.ManyToManyField(User,blank=True,related_name="likes",null=True)
	
	def __str__(self):
		return self.Subject

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})