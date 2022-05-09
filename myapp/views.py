from django.db.models.expressions import F
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from myapp.models import Organization
from django.contrib.auth import authenticate, login


# Create your views here.
def openPage(request):
    return render(request, 'index.html')


def registerPage(request):
    return render(request, 'register.html')

def loginPage(request):
    return render(request, 'login.html')

def orgReg(request):
    if Organization.objects.filter(org_email=request.POST['email-id']).exists():
        return HttpResponse("10")
    else:
        lclId = Organization.objects.count()
        lclId = lclId + 1
        Organization.objects.create(
            org_id=lclId,
            org_name =request.POST["name"],
            org_email =request.POST['email-id'],
            org_pw = request.POST['password'],
            org_status = "0"
        )
        return HttpResponse("1")


def orgLogin(request):
    if Organization.objects.filter(org_email=request.POST['email-id'], org_pw=request.POST['password']).exists():
        jsonData = Organization.objects.filter(org_email=request.POST['email-id']).values()
        data = list(jsonData)
        listValue = data[0]
        request.session['Email'] = listValue['org_email']
        print(request.session)
        return HttpResponse("11")

    else:
        return HttpResponse("12")