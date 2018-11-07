from django.shortcuts import render

def home(request):
	return render(request, "home.html", {})

def about(request):
	my_name = "Hello! My name is Chinedu Anayokafor"
	return render(request, "about.html", {"my_name" : my_name})

def contact(request):
	contact = "Hello! I would like to speak with you"
	return render(request, "contact.html", {"contact" : contact})
