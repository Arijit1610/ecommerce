from django.shortcuts import render,redirect
from .forms import RegistrationForm
import random


def send_otp_email(email):
    otp = str(random.randint(100000, 999999))
    print(otp)
    return otp

# Create your views here.
def home(request):
	return render(request,'mercury/home.html')


# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Redirect to login page after successful registration
#         else:
#             # Raise error for incorrect form fill-up
#             # Option 1: Using Django's validation errors
#             errors = form.errors
#             return render(request, 'mercury/registration.html', {'form': form, 'errors': errors})

#             # Option 2: Customizing error messages
#             username_error = None
#             email_error = None
#             password_error = None

#             if 'username' in errors:
#                 username_error = errors['username'][0]  # Access first error message
#             if 'email' in errors:
#                 email_error = errors['email'][0]
#             if 'password1' in errors or 'password2' in errors:
#                 password_error = "Password validation failed."  # Generic message

#             return render(request, 'mercury/registration.html', {'form': form,
#                                                                  'username_error': username_error,
#                                                                  'email_error': email_error,
#                                                                  'password_error': password_error})
#     else:
#         form = RegistrationForm()
#     return render(request, 'mercury/registration.html', {'form': form})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Generate OTP and send email
            email = form.cleaned_data['email']
            otp = send_otp_email(email)

            # Update form to display OTP field and disable email field
            form.fields['otp'].widget.attrs['readonly'] = False
            form.initial['otp'] = otp
        else:
            otp = None
    else:
        form = RegistrationForm()
        otp = None

    return render(request, 'mercury/registration.html', {'form': form, 'otp': otp})

def verify_otp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Verify OTP
            otp_entered = form.cleaned_data['otp']
            if otp_entered == form.initial['otp']:
                # Create user
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                password = form.cleaned_data['password']
                User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                return render(request, 'mercury/registration_success.html')
            else:
                form.add_error('otp', 'Invalid OTP. Please try again.')
        else:
            form.add_error(None, 'Form is not valid. Please correct the errors.')
    else:
        form = UserRegistrationForm()

    return render(request, 'mercury/registration.html', {'form': form})