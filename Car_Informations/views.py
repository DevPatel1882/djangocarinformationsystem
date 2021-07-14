from django.shortcuts import render, redirect
from car_data.models import Feedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from car_data.models import contact
from car_data.models import maruti_arena
from car_data.models import maruti_nexa
from car_data.models import tata_moter
from car_data.models import jaguar_moter
from car_data.models import mahindra_moter

from car_data.models import hundai_moter
from car_data.models import honda_moter
from car_data.models import renult_moter
from car_data.models import ford_moter
from car_data.models import nissan_moter

from car_data.models import Sell_Car_details
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def index(request):
    car = maruti_arena.objects.all()

    return render(request, 'index.html', {'car': car})


def master(request):
    if request.method == "POST":
        feedback = request.POST['feedback']
        Short_Summery = request.POST['Short_Summery']
        email = request.POST['email']
        ins = Feedback(feedback=feedback, Short_Summery=Short_Summery, email=email)
        ins.save()

    return render(request, 'index.html')


# login and signup functions
def handlesignup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pass = request.POST['confirm_pass']

        myuser = User.objects.create_user(username, email, password)
        myuser.confirm_pass = confirm_pass
        myuser.firstname = firstname
        myuser.lastname = lastname
        myuser.save()

        return render(request, 'login.html')

    else:

        return render(request, 'signup.html')


def handlelogin(request):
    if request.method == 'POST':
        lusername = request.POST['lusername']
        lpassword = request.POST['lpassword']

        user = authenticate(username=lusername, password=lpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "You Are Successfully Login. ")
            return render(request, 'index.html')
        else:
            messages.error(request, "Please Enter Valid Username and Password")
    return render(request, 'login.html')


# sell car functions
def sell_car(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone_num = request.POST.get('phone_num')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        car_company = request.POST.get('car_company')
        car_year = request.POST.get('car_year')
        car_model = request.POST.get('car_model')
        kms_driven = request.POST.get('kms_driven')
        fule_type = request.POST.get('fule_type')
        car_ownership = request.POST.get('car_ownership')
        Expected_price = request.POST.get('Expected_price')
        car_img = request.FILES.get('car_img')
        ins = Sell_Car_details(address=address, fule_type=fule_type, firstname=firstname, lastname=lastname,
                               email=email, phone_num=phone_num, state=state, city=city, pincode=pincode,
                               car_company=car_company, car_year=car_year, car_model=car_model, kms_driven=kms_driven,
                               car_ownership=car_ownership, Expected_price=Expected_price, car_img=car_img)
        ins.save()

    return render(request, 'sell_car/sell_car.html')


def seller_info(request, id):
    usedcar = Sell_Car_details.objects.filter(id=id).first()
    context = {'usedcar': usedcar}
    return render(request, 'sell_car/seller_info.html', context)


def sell_car_details(request):

    usedcar = Sell_Car_details.objects.all()
    print(usedcar)
    return render(request, 'sell_car/sell-car-details.html', {'usedcar': usedcar})


#  cars functions

def maruti_cars(request):
    car1 = maruti_arena.objects.all()
    car2 = maruti_nexa.objects.all()

    return render(request, 'cars/maruti.html', {'car1': car1, 'car2': car2})


def maruti_info(request, car_name):
    arena = maruti_arena.objects.filter(car_name=car_name).first()
    nexa = maruti_nexa.objects.filter(car_name=car_name).first()
    contaxt = {'arena': arena, 'nexa': nexa}
    return render(request, 'cars/maruti_info.html', contaxt)


# all cars details
def tata(request):
    tata_car = tata_moter.objects.all()
    return render(request, 'Cars_Company/tata.html', {'tata_car': tata_car})


def jaguar(request):
    jaguar = jaguar_moter.objects.all()
    return render(request, 'Cars_Company/jaguar.html', {'jaguar': jaguar})


def mahindra(request):
    mahindra = mahindra_moter.objects.all()
    return render(request, 'Cars_Company/mahindra.html', {'mahindra': mahindra})


def hundai(request):
    hundai = hundai_moter.objects.all()
    return render(request, 'Cars_Company/hundai.html', {'hundai': hundai})


def honda(request):
    honda = honda_moter.objects.all()
    return render(request, 'Cars_Company/honda.html', {'honda': honda})


def ford(request):
    ford = ford_moter.objects.all()
    return render(request, 'Cars_Company/ford.html', {'ford': ford})


def renult(request):
    renult = renult_moter.objects.all()
    return render(request, 'Cars_Company/renult.html', {'renult': renult})


def nissan(request):
    nissan = nissan_moter.objects.all()
    return render(request, 'Cars_Company/nissan.html', {'nissan': nissan})


def car_info(request, car_name):
    tata_car = tata_moter.objects.filter(car_name=car_name).first()
    jaguar = jaguar_moter.objects.filter(car_name=car_name).first()
    mahindra = mahindra_moter.objects.filter(car_name=car_name).first()
    hundai = hundai_moter.objects.filter(car_name=car_name).first()
    honda = honda_moter.objects.filter(car_name=car_name).first()
    ford = ford_moter.objects.filter(car_name=car_name).first()
    renult = renult_moter.objects.filter(car_name=car_name).first()
    nissan = nissan_moter.objects.filter(car_name=car_name).first()
    contaxt = {'tata_car': tata_car, 'jaguar': jaguar, 'mahindra': mahindra, 'hundai': hundai, 'honda': honda,
               'ford': ford, 'renult': renult, 'nissan': nissan}
    return render(request, 'car_info/car_info.html', contaxt)


def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        print(name, email, comment)
        contacts = contact(name=name, email=email, comment=comment)
        contacts.save()
        return render(request, 'index.html')
    else:
        return render(request,'contact.html')
