from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib import messages

from user_profile.models import UserProfile
from blog.models import Post, Comment, User

# Create your views here.
def user_profile_list(request):
	user_profiles = UserProfile.objects.all()
	context = {'user_profiles':user_profiles, 'request_user': request.user}
	return render(request, 'user_profile/list.html', context)

def user_profile_detail(request, user_profile_id):
	print(user_profile_id)
	user_profile = get_object_or_404(UserProfile, pk=user_profile_id)

	# Find post of users
	posts = Post.objects.filter(author_id= user_profile.user.id)

	context = {'user_profile': user_profile, 'posts':posts, 'request_user': request.user}
	return render(request, 'user_profile/detail.html', context)





