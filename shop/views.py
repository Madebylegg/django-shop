from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from allauth.account.forms import SignupForm
from django.contrib.auth import logout
from .forms import CustomLoginForm, CustomSignupForm


def home(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/home.html', { 'products': products })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'shop/product_detail.html', { 'product': product })

def login_view(request):
    form = CustomLoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.login_user(request)
        return redirect(request.POST.get('next', '/'))

    return render(request, 'shop/login.html', {
        'form': form
    })


def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('/')  # or LOGIN_REDIRECT_URL
    else:
        form = CustomSignupForm()
    
    return render(request, 'shop/signup.html', {'form': form})

    
    return render(request, 'shop/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('shop-login')  # or use LOGOUT_REDIRECT_URL






def privacy_view(request):
    return render(request, "shop/privacy.html")


def terms_view(request):
    return render(request, "shop/terms.html")