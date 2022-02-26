from django.shortcuts import render,HttpResponse
from sigma import encryption
from sigma.models import signup
def sign(request):
    context={'passw':'Password','confpassw':'Confirm Password'}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        passw = request.POST.get('pass')
        confpassw = request.POST.get('confpass')
        if encryption.check(passw,confpassw):
            signinObject=signup(name=name,email=email,passw=encryption.encrypt(passw))
            signinObject.save()
        else:
            context={'passw':'Passwords dont match','confpassw':'Passwords Dont match'}
    return render(request,'signup.html',context)
