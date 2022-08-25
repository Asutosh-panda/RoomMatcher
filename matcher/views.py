from multiprocessing import context
from django.shortcuts import redirect, render
from hostel.models import Register,Hostelite
from .models import SelectMatch,Match

# Create your views here.

def matcher(request):
    # curr_user = SelectMatch.objects.filter(sic__user=request.user).values()
    # for curr in curr_user:
    #     if(curr['status1'] and curr['status2'] ):
    #         return redirect('home')
    stu = Register.objects.all()
    curr = Register.objects.get(user = request.user).sic
    stulist=[]
    for student in stu:
    
        if student.sic != curr:
            students ={
                "first_name" : student.sic.first_name,
                "last_name" : student.sic.last_name,
                "branch" : student.sic.branch+"E",
                "home" : student.sic.home,
                "hobby":student.hobby,
                "desc":student.desc,
                "sic":student.sic
            }
            stulist.append(students)
    context={
       "students":stulist
   }

    return render(request,'matcher/display.html',context)

def wishlist(request):
    # curr_user = SelectMatch.objects.filter(sic__user=request.user).values()
    # for curr in curr_user:
    #     if(curr['status1'] and curr['status2'] ):
    #         return redirect('home')

    later = SelectMatch.objects.filter(sic__user=request.user).values()
    later_list=[]
    
    for i in later:
        student = Register.objects.get(sic =i['later'])
        students ={
                "first_name" : student.sic.first_name,
                "last_name" : student.sic.last_name,
                "branch" : student.sic.branch+"E",
                "home" : student.sic.home,
                "hobby":student.hobby,
                "desc":student.desc,
                "sic":student.sic.sic
            }
        
        if(students not  in later_list):
            later_list.append(students)


    sic_curr = Register.objects.get(user = request.user).sic.sic
    match_curr = SelectMatch.objects.filter(later = sic_curr).values()

    match_list=[]
    for match in match_curr:
        later_id = match['id']
        sic_later = SelectMatch.objects.get(id=later_id).sic
        
        match_later = SelectMatch.objects.filter(later = sic_later.sic.sic).values()
        
        for ml in match_later:
           
            ml_id = ml['id']
            sic_next = SelectMatch.objects.get(id=ml_id).sic
            if(sic_next.sic.sic == sic_curr):
                students ={
                "first_name" : sic_later.sic.first_name,
                "last_name" : sic_later.sic.last_name,
                "branch" : sic_later.sic.branch+"E",
                "home" : sic_later.sic.home,
                "hobby":sic_later.hobby,
                "desc":sic_later.desc,
                "sic":sic_later.sic.sic,
                "status":ml['status1']
            }
            if(students not  in match_list):
                match_list.append(students) 
    
    context={
       "students":later_list,
       "matches": match_list
   }

    return render(request,"matcher/wishlist.html",context)

def add(request,id):
 
    
    curr = Register.objects.get(user= request.user)
    # print(curr.sic.sic)
    if(SelectMatch.objects.filter(later=id).exists()):
        return redirect('matcher')
    try:
        sm= SelectMatch.objects.create(
            sic = curr,
            later = id
        )
        sm.save()
        print("done")
        return redirect('matcher')
    except Exception as e:
        print("f")


    return redirect('matcher')

def remove(request,id):
    try:
        SelectMatch.objects.get(later=id).delete()
        return redirect('wishlist')
    
    except Exception as e:
        print(e)
    
    return redirect('display')

def matched(request):

    sic_curr = Register.objects.get(user = request.user).sic.sic
    match_curr = SelectMatch.objects.filter(later = sic_curr).values()

    match_list=[]
    for match in match_curr:
        later_id = match['id']
        sic_later = SelectMatch.objects.get(id=later_id).sic
        
        match_later = SelectMatch.objects.filter(later = sic_later.sic.sic).values()
        for ml in match_later:
            ml_id = ml['id']
            sic_next = SelectMatch.objects.get(id=ml_id).sic
            if(sic_next.sic.sic == sic_curr):
                students ={
                "first_name" : sic_later.sic.first_name,
                "last_name" : sic_later.sic.last_name,
                "branch" : sic_later.sic.branch+"E",
                "home" : sic_later.sic.home,
                "hobby":sic_later.hobby,
                "desc":sic_later.desc,
                "sic":sic_later.sic.sic 
            }
            if(students not  in match_list):
                match_list.append(students)
    
    
    context={
       "students":match_list
   }


    

    return render(request,'matcher/matched.html',context)

def confirm(request,id):
    confirm_user = SelectMatch.objects.filter(later=id).get(sic__user=request.user)
    try:
        confirm_user.status1 = True
        confirm_user.save()
        print("saved status")
    except Exception as e:
        print(e)

    return redirect('wishlist')


