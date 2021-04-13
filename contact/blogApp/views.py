from django.shortcuts import render
from .models import Contact
from django.http import  HttpResponse

def index(request):
	if request.method == "POST":
		contact = Contact()
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		# to get attributes to contact class
		contact.name = name
		contact.email = email
		contact.subject = subject
		contact.save()
		return HttpResponse("<h1>Thank you for contacting us</h1>")

	return render(request, 'index.html')
