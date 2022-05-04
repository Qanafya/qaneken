from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from . models import *
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

# Create your views here.

rand = 25478

def index(request):
    return render(request, 'index.html')

def service(request):
    ram = Ramiz.objects.all()
    return render(request, 'index2.html', {'ram': ram})

def contact(request):
    return render(request, 'index6.html')

def ser1(request):
    menu = Eltanba.objects.all()
    return render(request, 'index3.html', {'menu':menu})

def ser2(request):
    return render(request, 'index4.html')

def ser3(request):
    an = Anuran.objects.all()
    return render(request, 'index5.html', {'an': an})

def user(request):
    users = Qoldan.objects.all()
    return render(request, 'index7.html', {'users':users})

def delete(request, id):
    users = Users.objects.get(id=id)
    users.delete()
    return redirect("/users/")


def edit(request, id):
    users = Users.objects.get(id=id)
    return render(request, 'index8.html', {'users':users})

@csrf_exempt
def std(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/users/')
            except:
                pass
    else:
        form = UsersForm()
    return render(request, 'index7.html')


def add(request):
    return render(request, 'index9.html')

def update(request, id):
    id = int(id)
    try:
        post_sel = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return redirect('/users/')
    post_form = UsersForm(request.POST or None, instance = post_sel)
    if post_form.is_valid:
        post_form.save()
        return redirect('/users/')
    return render(request, 'index7.html', {'upload_form':post_form})

def registr(request):
    return render(request, 'index10.html')


@csrf_exempt
def reg(request):

    if request.method == "POST":
        form = QoldanForm(request.POST)
        pass1 = request.POST['password']
        pass2 = request.POST['confirm']
        login = request.POST['login']
        em = request.POST['email']
        email_subject = 'User activation'
        email_body = render_to_string('active.html')
        email = EmailMessage(subject=email_subject, body=email_body,
                             from_email='200103214@stu.sdu.edu.kz',
                             to=[em])
        email.attach_file('C:/Users/77086/Desktop/New Мәтіндік құжат.txt')

        if pass1 == pass2:
            if Qoldan.objects.filter(login=login).exists():
                print("login name already used")
                return redirect('/register/')
            else:
                if form.is_valid():
                    try:
                        form.save()
                        print("user created")

                        email.send()
                        return redirect('/register/')
                    except:
                        pass
                else:
                    print('number exists')
                    redirect('/register/')

        else:
            print("invalid password")
            return redirect('/register/')
    else:
        print('Qalmady')
        return render(request, 'index.html')
    return redirect('/register/')

