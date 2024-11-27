from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from new_app.forms import LoginForm, CustomerForm, SellerForm, BlogForm
from new_app.models import Blog, Customer


# Create your views here.
def Login(request):

    if request.method == 'POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        print(password)
        user =authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_staff:

                return redirect('index_dashboard')
            elif user.is_Customer:

                return redirect('index_dashboard')
            elif user.is_Seller:

                return redirect('index_dashboard')
        else:
            messages.info(request,'invalid Credentials')
    return render(request,'Login.html')



def customer(request):
    form1  = LoginForm()
    form2 = CustomerForm()

    if request.method =="POST":
        form1 = LoginForm(request.POST)
        form2 = CustomerForm(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            user1 = form1.save(commit=False)
            user1.is_Donor = True
            user1.save()

            user2 = form2.save(commit=False)
            user2.user = user1
            user2.save()
            return redirect("login")

    return render(request,'customer.html',{"form1":form1 , "form2":form2})

def seller(request):
    form1  = LoginForm()
    form2 = SellerForm()

    if request.method =="POST":
        form1 = LoginForm(request.POST)
        form2 = SellerForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            user1 = form1.save(commit=False)
            user1.is_Receiver = True
            user1.save()

            user2 = form2.save(commit=False)
            user2.user = user1
            user2.save()
            return redirect("login")

    return render(request,'seller_reg.html',{"form1":form1, "form2":form2})

def index_dashboard(request):
    return render(request,'index_dashboard.html')

def index(request):
    return render(request,'index.html')

def blog(request):
    data = BlogForm()
    user1 = request.user
    rmr = Customer.objects.get(user=user1)

    if request.method == "POST":
        req = BlogForm(request.POST)
        print(req)
        if req.is_valid():
            print("ok")
            obj = req.save(commit=False)
            obj.Customer_name = rmr
            obj.save()
    return render(request,'blog/blog.html',{"form":data})


def view(request):
    user1 = request.user
    data = Blog.objects.get(user=user1)
    obj = BlogForm.objects.filter(Customer_name=data)
    return render(request, 'view.html', {'data': obj})