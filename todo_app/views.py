from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from . models import*
from django.contrib.auth.decorators import login_required



# Create your views here.
# ADD TO DO TASKS
@login_required(login_url='/signin/')
def home(request):
    user_task=task.objects.filter(user=request.user)
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['description']
        date=request.POST['date']
        status=request.POST['status']
        todo=task(title=title,description=desc,date=date,status=status,user=request.user)
        todo.save()
        return redirect('/home/')
    else:
        return render(request,"home.html",{'tasks':user_task})
    

#UPDATE TO DO TASKS
def update(request):
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['description']
        date=request.POST['date']
        status=request.POST['status']
        uid=request.GET['uid']

        update=task.objects.filter(id=uid).update(title=title,description=desc,date=date,status=status)
        return redirect('/home/')
    else:
        uid=request.GET['uid']
        query=task.objects.filter(id=uid)
        return render(request,"updatetodo.html",{"data":query})
    
#DELETE TO DO
def delete(request):
    uid=request.GET['uid']
    query=task.objects.filter(id=uid).delete()
    return redirect('/home/')


#REGISTER USER
def signup(request):
    if request.method=="POST":
        user_name=request.POST['username']
        email=request.POST['email']
        pass_word=request.POST['password']
        confpwd=request.POST['confirmpwd']

        if pass_word==confpwd:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username already taken")
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('/register/')
            else:
                user=User.objects.create_user(username=user_name,email=email,password=pass_word)
                user.save()

        else:
            messages.info(request,"Password not matched")
            return redirect('/register/')
        return redirect('/')
    
    return render(request,"register.html")


# LOGIN USER
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home/')
        else:
            messages.info(request,"Invalid details")
            return redirect('/')

    return render(request,"signin.html")







