from django.shortcuts import render,get_object_or_404
from .forms import * 

# Create your views here.

def cases_view(request):
    cases = Case.objects.all()
    context = {'cases':cases}
    return render(request,'cases.html',context)

def case_add_view(request):
    c_form = Case_Form()
    if request.method == 'POST':
        c_form = Case_Form(request.POST)
        c_form.save() 
    context = {'c_form':c_form}
    return render(request,'case_add.html',context=context)

def case_details_view(request, pk):
    case = get_object_or_404(Case,id=pk)
    context = {'case':case}
    return render(request,'case_details.html',context)

def case_update_view(request,pk):
    case = get_object_or_404(Case,id=pk)
    c_form = Case_Form(instance=case)
    if request.method == 'POST':
        c_form = Case_Form(request.POST,instance=case)
        c_form.save() 
    context = {'c_form':c_form}
    return render(request,'case_update.html',context=context)

def case_delete_view(request,pk):
    case = get_object_or_404(Case,id=pk)
    if request.method == 'POST':
        case.delete() 
    context = {'case':case}
    return render(request,'case_delete.html',context=context)

def prisoners_view(request):
    prisoners = Prisoner.objects.all()
    context = {'prisoners':prisoners}
    return render(request,'prisoners.html',context)

def prisoner_add_view(request):
    p_form = Prisoner_Form()
    if request.method == 'POST':
        p_form = Prisoner_Form(request.POST,request.FILES)
        p_form.save() 
    context = {'p_form':p_form}
    return render(request,'prisoner_add.html',context=context)

def prisoner_details_view(request, pk):
    prisoner = get_object_or_404(Prisoner,id=pk)
    context = {'prisoner':prisoner}
    return render(request,'prisoner_details.html',context)

def prisoner_update_view(request,pk):
    prisoner = get_object_or_404(Prisoner,id=pk)
    p_form = Prisoner_Form(instance=prisoner)
    if request.method == 'POST':
        p_form = Prisoner_Form(request.POST,request.FILES,instance=prisoner)
        p_form.save() 
    context = {'p_form':p_form}
    return render(request,'prisoner_update.html',context=context)

def prisoner_delete_view(request,pk):
    prisoner = get_object_or_404(Prisoner,id=pk)
    if request.method == 'POST':
        prisoner.delete() 
    context = {'prisoner':prisoner}
    return render(request,'prisoner_delete.html',context=context)

def visit_add_view(request):
    v_form = Visit_Form()
    if request.method == 'POST':
        v_form = Visit_Form(request.POST)
        v_form.save() 
    context = {'v_form':v_form}
    return render(request,'visit_add.html',context=context)

def visit_update_view(request,pk):
    visit = get_object_or_404(Visit,id=pk)
    v_form = Visit_Form(instance=visit)
    if request.method == 'POST':
        v_form = Visit_Form(request.POST,instance=visit)
        v_form.save() 
    context = {'v_form':v_form}
    return render(request,'visit_update.html',context=context)

def visit_delete_view(request,pk):
    visit = get_object_or_404(Visit,id=pk)
    if request.method == 'POST':
        visit.delete() 
    context = {'visit':visit}
    return render(request,'visit_delete.html',context=context)

def visit_details_view(request, pk):
    visit = get_object_or_404(Visit,id=pk)
    context = {'visit':visit}
    return render(request,'visit_details.html',context)

def visits_view(request):
    visits = Visit.objects.all()
    context = {'visits':visits}
    return render(request,'visits.html',context)

def visitors_view(request):
    visitors = Visitor.objects.all()
    context = {'visitors':visitors}
    return render(request,'visitors.html',context)

def visitor_add_view(request):
    vr_form = Visitor_Form()
    if request.method == 'POST':
        vr_form = Visitor_Form(request.POST)
        vr_form.save() 
    context = {'vr_form':vr_form}
    return render(request,'visitor_add.html',context=context)

def visitor_details_view(request, pk):
    visitor = get_object_or_404(Visitor,id=pk)
    context = {'visitor':visitor}
    return render(request,'visitor_details.html',context)

def visitor_update_view(request,pk):
    visitor = get_object_or_404(Visitor,id=pk)
    vr_form = Visitor_Form(instance=visitor)
    if request.method == 'POST':
        vr_form = Visitor_Form(request.POST,instance=visitor)
        vr_form.save() 
    context = {'vr_form':vr_form}
    return render(request,'visitor_update.html',context=context)

def visitor_delete_view(request,pk):
    visitor = get_object_or_404(Visitor,id=pk)
    if request.method == 'POST':
        visitor.delete()
    context = {'visitor':visitor}
    return render(request,'visitor_delete.html',context=context)

def leave_add_view(request):
    l_form = Leave_Form()
    if request.method == 'POST':
        l_form = Leave_Form(request.POST)
        l_form.save() 
    context = {'l_form':l_form}
    return render(request,'leave_add.html',context=context)

def leave_update_view(request,pk):
    leave = get_object_or_404(Leave,id=pk)
    l_form = Leave_Form(instance=leave)
    if request.method == 'POST':
        l_form = Leave_Form(request.POST,instance=leave)
        l_form.save() 
    context = {'l_form':l_form}
    return render(request,'leave_update.html',context=context)

def leave_delete_view(request,pk):
    leave = get_object_or_404(Leave,id=pk)
    if request.method == 'POST':
        leave.delete() 
    context = {'leave':leave}
    return render(request,'leave_delete.html',context=context)

def leave_details_view(request, pk):
    leave = get_object_or_404(Leave,id=pk)
    context = {'leave':leave}
    return render(request,'leave_details.html',context)

def leaves_view(request):
    leaves = Leave.objects.all()
    context = {'leaves':leaves}
    return render(request,'leaves.html',context)



