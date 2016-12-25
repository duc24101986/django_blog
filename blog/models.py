from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	STATUS_CHOICE = (
		('draft', 'Draft'),
		('published', 'Published')
	)
	title = models.CharField(max_length=250)
	# slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(User, related_name='blog_post')
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments')
	# name = models.CharField(max_length=80)
	author = models.ForeignKey(User, related_name='blog_comment', null=True)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.author, self.post)