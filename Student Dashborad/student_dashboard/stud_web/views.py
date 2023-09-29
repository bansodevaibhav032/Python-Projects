from django.shortcuts import render, redirect
from .models import stud_info

# Create your views here.
def retrieve(request):
    details = stud_info.objects.all()
    return render(request, 'show.html',{ 'details' : details})

def create(request):
    if request.method == 'POST':
        stud_fname = request.POST['stud_fname']
        stud_lname = request.POST['stud_lname']
        stud_class = request.POST['stud_class']
        stud_email = request.POST['stud_email']
        stud_age = request.POST['stud_age']
        stud_address= request.POST['stud_address']
        stud_city= request.POST['stud_city']
        stud_contact = request.POST['stud_contact']
        stud_bloodgroup= request.POST['stud_bloodgroup']
        stud_DOB = request.POST['stud_DOB']
        stud_gen = request.POST['stud_gen']

        obj = stud_info.objects.create\
            (stud_fname=stud_fname, stud_lname=stud_lname,stud_class=stud_class,
             stud_email=stud_email, stud_age=stud_age,stud_address=stud_address,stud_city=stud_city,
             stud_contact=stud_contact,stud_bloodgroup=stud_bloodgroup,stud_DOB=stud_DOB,stud_gen=stud_gen)
        obj.save()
        return redirect('/')
    return render(request, 'index.html')


def edit(request,stud_id):
    data = stud_info.objects.get(stud_id=stud_id)
    return render(request,'edit.html',{'data':data})



def update(request,stud_id):
    if request.method == 'POST':
        obj = stud_info.objects.get(stud_id =stud_id)
        stud_fname = request.POST['stud_fname']
        stud_lname = request.POST['stud_lname']
        stud_class = request.POST['stud_class']
        stud_email = request.POST['stud_email']
        stud_age = request.POST['stud_age']
        stud_address = request.POST['stud_address']
        stud_city = request.POST['stud_city']
        stud_contact = request.POST['stud_contact']
        stud_bloodgroup = request.POST['stud_bloodgroup']
        stud_DOB = request.POST['stud_DOB']
        stud_gen = request.POST['stud_gen']
        obj.save()
        return redirect("/")
    return render(request,'edit.html')


def delete(request, stud_id):
    stud_info.objects.get(stud_id=stud_id).delete()
    return redirect("/")