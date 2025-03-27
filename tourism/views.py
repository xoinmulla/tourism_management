from django.shortcuts import render,redirect
from .models import Destination, Package,Review
from .models import ContactMessage  # Import the model
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        # Save message to database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Send confirmation email (optional)
        send_mail(
            "New Contact Message",
            f"Name: {name}\nEmail: {email}\nMessage: {message}",
            "your-email@example.com",  # Replace with your email
            ["admin@example.com"],  # Replace with the admin email
            fail_silently=False,
        )

        return redirect("contact")  # Redirect to the same page

    return render(request, "contact.html")

def home(request):
    return render(request, 'home.html')

def packages(request):
    all_packages = Package.objects.all()
    return render(request, 'packages.html', {'packages': all_packages})

def destination(request):
    destination = Destination.objects.all()
    print(destination)  # Debugging line to check data
    return render(request, 'destination.html', {'destination': destination})

def reviews(request):
    reviews_list = Review.objects.all().order_by('-date')  # Fetch all reviews
    return render(request, 'reviews.html', {'reviews': reviews_list})