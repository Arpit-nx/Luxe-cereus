from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import Feedback

def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Shop(request):
    return render(request, 'shop.html')

def Contact(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the feedback in the database
        feedback = Feedback(name=name, email=email, message=message)
        feedback.save()

        # Check if the request is an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"message": "Feedback submitted successfully!"})

        # Redirect back to the contact page after form submission
        return redirect('contact')  # Redirect to the contact page or a success page

    return render(request, 'contact.html')

def Chat(request):
    return render(request, 'chat.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat_page')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
