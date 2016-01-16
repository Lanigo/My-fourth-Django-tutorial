from django.db import models
from django.utils import timezone 
from ckeditor.fields import RichTextField   
from django.core.urlresolvers import reverse   # import this

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=255)
	text = RichTextField()
	slug = models.SlugField(max_length=255)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __unicode__(self):
		return self.title

	# add this method
	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'slug': self.slug})	

class Comment(models.Model):
	post = models.ForeignKey('myapp.Post', related_name='comments')
	author = models.CharField(max_length=100)
	text = models.TextField()
	created_date =models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.text