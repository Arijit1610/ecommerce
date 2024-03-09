from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import RegistrationForm, UserLoginForm
import random
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib import messages
from .tokens import account_activation_token
from django.contrib.auth.models import User
from .models import *


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('mercury/template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')
# Create your views here.


def home(request):
    return render(request, 'mercury/home.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('login')
        else:
            errors = form.errors
            return render(request, 'mercury/registration.html', {'form': form, 'errors': errors})
            username_error = None
            email_error = None
            password_error = None
            if 'username' in errors:
                username_error = errors['username'][0]
            if 'email' in errors:
                email_error = errors['email'][0]
            if 'password1' in errors or 'password2' in errors:
                password_error = "Password validation failed."
            return render(request, 'mercury/registration.html', {'form': form, 'username_error': username_error, 'email_error': email_error, 'password_error': password_error})
    else:
        form = RegistrationForm()
    return render(request, 'mercury/registration.html', {'form': form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if user.is_active == True:
            messages.info(request, 'You have already activated your account')
        else:
            user.is_active = True
            user.save()

            messages.success(
                request, 'Thank you for your email confirmation. Now you can login your account.')
    else:
        messages.error(request, 'Activation link is invalid!')
    if request.user.is_authenticated:
        return redirect('home')

    return redirect('login')


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    form = UserLoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        try:
            try:
                print("block1")
                user = User.objects.get(email=username)
                print(user.username)
                user = authenticate(
                    request, username=user.username, password=password)
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                print("login Sucessess")
                return redirect('home')
            except:
                print("block2")
                user = authenticate(
                    request, username=username, password=password)
                print("block3")
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                print("login Sucessess")
                return redirect('home')
        except:
            try:
                print("block4")
                try:
                    print("block5")
                    user = User.objects.get(email=username)
                except:
                    print("block6")
                    user = User.objects.get(username=username)
                print("block7")
                messages.error(
                    request, "Incorrect Password!!! Please Try Again")
            except:
                print("block8")
                messages.error(
                    request, "User Not Found!!! Please Create Your Account ")
            print("block9")
            print("login failure")
    context = {'page': page, 'form': form}
    return render(request, "mercury/registration.html", context)


def logoutPage(request):
    logout(request)
    messages.success(request, "You have successfully logout from your account")
    return redirect('login')


def searchProducts(request):
    query = request.GET.get('q')
    fashion_results = Fashion.objects.filter(fashion_name__icontains=query) | \
        Fashion.objects.filter(brand_name__icontains=query) | \
        Fashion.objects.filter(fashion_section__icontains=query) | \
        Fashion.objects.filter(differentfashion__icontains=query) | \
        Fashion.objects.filter(product_type__product_type__icontains=query)

    electronics_results = Eletronices.objects.filter(product_name__icontains=query) | \
        Eletronices.objects.filter(company_name__icontains=query) | \
        Eletronices.objects.filter(types__icontains=query) |\
        Eletronices.objects.filter(product_type__product_type__icontains=query)

    beauty_results = BeautyCosmetics.objects.filter(product_name__icontains=query) | \
        BeautyCosmetics.objects.filter(company_name__icontains=query) | \
        BeautyCosmetics.objects.filter(types__icontains=query) |\
        BeautyCosmetics.objects.filter(
            product_type__product_type__icontains=query)

    books_results = BooksAndStationery.objects.filter(title__icontains=query) | \
        BooksAndStationery.objects.filter(author_name__icontains=query) | \
        BooksAndStationery.objects.filter(publisher_name__icontains=query) | \
        BooksAndStationery.objects.filter(types__icontains=query) |\
        BooksAndStationery.objects.filter(
            product_type__product_type__icontains=query)

    sports_results = Sportsandoutdoor.objects.filter(product_name__icontains=query) | \
        Sportsandoutdoor.objects.filter(company_name__icontains=query) | \
        Sportsandoutdoor.objects.filter(sportscatagory__icontains=query) |\
        Sportsandoutdoor.objects.filter(
            product_type__product_type__icontains=query)

    home_results = HomeandKitchen.objects.filter(product_name__icontains=query) | \
        HomeandKitchen.objects.filter(company_name__icontains=query) | \
        HomeandKitchen.objects.filter(Productcatagory__icontains=query) |\
        HomeandKitchen.objects.filter(
            product_type__product_type__icontains=query)

    context = {
        'fashion_results': fashion_results,
        'electronics_results': electronics_results,
        'beauty_results': beauty_results,
        'books_results': books_results,
        'sports_results': sports_results,
        'home_results': home_results,
        'query': query
    }

    return render(request, 'mercury/search_results.html', context)


def eletronices(request):
    types = "Eletronices"
    products = Eletronices.objects.all()
    context = {'products': products, 'types': types}
    return render(request, 'mercury/product_view.html', context)


def fashion(request):
    types = "Fashion"
    products = Fashion.objects.all()
    context = {'products': products, 'types': types}
    return render(request, 'mercury/product_view.html', context)


def homeandkitchen(request):
    types = "Home and Kitchen"
    products = HomeandKitchen.objects.all()
    context = {'products': products, 'types': types}
    return render(request, 'mercury/product_view.html', context)


def sportsandoutdoor(request):
    types = "Sports and Outdoors"
    products = Sportsandoutdoor.objects.all()
    context = {'products': products, 'types': types}
    return render(request, 'mercury/product_view.html', context)


def beautycosmetics(request):
    types = "Beauty and Cosmetics"
    products = BeautyCosmetics.objects.all()
    context = {'products': products, 'types': types}
    return render(request, 'mercury/product_view.html', context)


def booksandstationery(request):
    types = "Book and Stationery"
    products = BooksAndStationery.objects.all()
    context = {'products': products, 'types': types}
    return render(request, 'mercury/product_view.html', context)


def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response
