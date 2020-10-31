from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# Send an email
		send_mail(
			'Message from' + message_name,		#-subject
			message,							#-message
			message_email,						#-from email
			['mmethiforex@gmail.com']			#-to email
			)

		return render(request, 'contact.html', {'message_name': message_name})
	else:
		return render(request, 'contact.html', {})

def episodes(request):
	return render(request, 'episodes.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def gallery(request):
	return render(request, 'gallery.html', {})