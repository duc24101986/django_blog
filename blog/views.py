from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib import messages


from .models import Post, Comment, User
from .form import EmailPostForm, CommentForm, PostForm

# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	context = {'posts':posts, 'request_user': request.user}
	return render(request, 'blog/post/list.html', context)

def post_new(request):
	if request.user.is_authenticated:
		if request.method=='GET':
			post_form = PostForm()

		elif request.method=='POST':
			print(request.method)
			post_form = PostForm(request.POST)
			if post_form.is_valid():
				post = post_form.save(commit=False)
				# post.author = request.user
				post.published_date = timezone.now()
				post.author = request.user
				post.save()
				print(post.pk)
				print("redirect")
				return redirect('post_detail', post_id=post.pk)

		context = {'post_form': post_form}
		return render(request, 'blog/post/new.html', context)

	else:
		return redirect('login')

def post_edit(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	if request.method=='GET':
		post_form = PostForm(instance=post)
		context = {'post_form': post_form}
		return render(request, 'blog/post/edit.html', context)

	elif request.method=='POST':
		post_form = PostForm(request.POST)
		if post_form.is_valid():
			post = post_form.save(commit=False)
			# post.author = request.user
			# post.published_date = timezone.now()
			# post.author = request.user
			# post.save()

			return redirect('post_detail', post_id=post.pk)

def post_delete(request, post_id):
	if request.method == 'GET':
		post = get_object_or_404(Post, pk=post_id)
		post.delete()
		messages.add_message(request, messages.INFO, 'Post '+ post.title + ' has been deleted!' )

		return redirect('post_list')

def post_detail(request, post_id):
	print(post_id)
	post = get_object_or_404(Post, pk=post_id)
	comments = post.comments.filter(active=True)

	if request.method=='GET':
		comment_form = CommentForm()
		context = {'post': post, 'comments':comments, 'comment_form': comment_form, 'request_user': request.user}
		return render(request, 'blog/post/detail.html', context)
	elif request.method=='POST':
		print(request.POST)
		comment_form=CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
			context = {'post': post, 'comments': comments, 'comment_form': comment_form, 'request_user': request.user}
			return render(request, 'blog/post/detail.html', context)

def post_share(request, post_id):
	sent = False
	if request.method=='GET':
		form = EmailPostForm()
		post = get_object_or_404(Post, pk=post_id)
		context = {'post': post, 'sent': sent, 'form':form}
		return render(request,'blog/post/share.html', context)
	elif request.method=='POST':
		print(request.POST)
		name = request.POST['name']
		email = request.POST['email']
		to = request.POST['to']
		comment = request.POST['comments']
		form = EmailPostForm(request.POST)
		post = get_object_or_404(Post, pk=post_id)

		email_subject = 'Share blog ' + post.title
		email_content = comment

		if form.is_valid():
			send_mail(email_subject, email_content, email, [to], fail_silently=False)
			print('Email sent!')
			sent = True
			return redirect('/blog', post=post)

def dashboard(request):
	return redirect('post_list')

def user_list(request):
	users = User.objects.all()
	context = {'users': users, 'request_user': request.user}
	return render(request, 'blog/user/list.html', context)






