#coding=utf-8
from django.db import models

# Create your models here.

class Author(models.Model):
	AuthorID = models.CharField(max_length = 15, primary_key = True)
	Name = models.CharField(max_length = 15)
	Age = models.CharField(max_length = 15)
	Country = models.CharField(max_length = 15)
	def __unicode__(self):
		return self.AuthorID
    
		
class Book(models.Model):
	ISBN = models.CharField(max_length = 15, primary_key = True)
	Title = models.CharField(max_length = 30)
	AuthorID  = models.CharField(max_length = 15)
	Publisher = models.CharField(max_length = 20)
	PublishDate = models.DateField()
	Price = models.CharField(max_length = 10)
	

	

