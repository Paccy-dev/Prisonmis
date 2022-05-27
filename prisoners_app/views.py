from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *            

# Create your views here.

@login_required
def cases_view(request):
    cases = Case.objects.all()
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            case = get_object_or_404(Case,id=pk)
            case.delete()
            messages.success(request, f'Case {case} - Deletion successful')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'cases':cases}
    return render(request,'cases.html',context)

@login_required
def case_add_view(request):
    c_form = Case_Form()
    if request.method == 'POST':
        c_form = Case_Form(request.POST)
        if c_form.is_valid():
            c_form.save()
            name = c_form.cleaned_data.get('name')
            messages.success(request, f'Case {name} - Creation successful') 
            return redirect('cases')
    context = {'c_form':c_form}
    return render(request,'case_add.html',context=context)

@login_required
def case_details_view(request, pk):
    case = get_object_or_404(Case,id=pk)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            case = get_object_or_404(Case,id=pk)
            case.delete()
            messages.success(request, f'Case {case} - Deletion successful')
            return redirect('cases')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'case':case}
    return render(request,'case_details.html',context)

@login_required
def case_update_view(request,pk):
    case = get_object_or_404(Case,id=pk)
    c_form = Case_Form(instance=case)
    if request.method == 'POST':
        c_form = Case_Form(request.POST,instance=case)
        if c_form.is_valid():
            c_form.save() 
            messages.success(request, f'Case {case} - Update successful')
            return redirect('case_details', pk)
    context = {'c_form':c_form}
    return render(request,'case_update.html',context=context)

@login_required
def case_delete_view(request,pk):
    case = get_object_or_404(Case,id=pk)
    context = {'instance':case}
    return render(request,'modal_delete.html',context=context)

@login_required
def prisoners_view(request):
    prisoners = Prisoner.objects.all()
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            prisoner = get_object_or_404(Prisoner,id=pk)
            prisoner.delete()
            messages.success(request, f'Prisoner {prisoner} - Deletion successful')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'prisoners':prisoners}
    return render(request,'prisoners.html',context)

@login_required
def prisoner_add_view(request):
    p_form = Prisoner_Form()
    if request.method == 'POST':
        p_form = Prisoner_Form(request.POST,request.FILES)
        if p_form.is_valid():
            name = p_form.cleaned_data.get('firstname')
            p_form.save() 
            messages.success(request, f'Prisoner {name} creation successful')
            return redirect('prisoners')
    context = {'p_form':p_form}
    return render(request,'prisoner_add.html',context=context)

@login_required
def prisoner_details_view(request, pk):
    prisoner = get_object_or_404(Prisoner,id=pk)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            prisoner = get_object_or_404(Prisoner,id=pk)
            prisoner.delete()
            messages.success(request, f'Prisoner {prisoner} - Deletion successful')
            return redirect('prisoners')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'prisoner':prisoner}
    return render(request,'prisoner_details.html',context)

@login_required
def prisoner_update_view(request,pk):
    prisoner = get_object_or_404(Prisoner,id=pk)
    p_form = Prisoner_Form(instance=prisoner)
    if request.method == 'POST':
        p_form = Prisoner_Form(request.POST,request.FILES,instance=prisoner)
        if p_form.is_valid():
            p_form.save() 
            messages.success(request, f'Prisoner {prisoner} - update successful')
            return redirect('prisoner_details', pk) 
    context = {'p_form':p_form,'prisoner':prisoner}
    return render(request,'prisoner_update.html',context=context)

@login_required
def prisoner_delete_view(request,pk):
    prisoner = get_object_or_404(Prisoner,id=pk)
    context = {'instance':prisoner}
    return render(request,'modal_delete.html',context=context)

@login_required
def visitors_view(request):
    visitors = Visitor.objects.all()
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            visitor = get_object_or_404(Visitor,id=pk)
            visitor.delete()
            messages.success(request,f'Visitor {visitor} - deletion successful')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'visitors':visitors}
    return render(request,'visitors.html',context)

@login_required
def visitor_add_view(request):
    vr_form = Visitor_Form()
    if request.method == 'POST':
        vr_form = Visitor_Form(request.POST)
        if vr_form.is_valid():
            vr_form.save() 
            name = vr_form.cleaned_data.get('firstname')
            messages.success(request,f'Visitor {name} - creation successful')
            return redirect('visitors')
    context = {'vr_form':vr_form}
    return render(request,'visitor_add.html',context=context)

@login_required
def visitor_details_view(request, pk):
    visitor = get_object_or_404(Visitor,id=pk)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            visitor = get_object_or_404(Visitor,id=pk)
            visitor.delete()
            messages.success(request, f'Visitor {visitor} - deletion successful')
            return redirect('visitors')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'visitor':visitor}
    return render(request,'visitor_details.html',context)

@login_required
def visitor_update_view(request,pk):
    visitor = get_object_or_404(Visitor,id=pk)
    vr_form = Visitor_Form(instance=visitor)
    if request.method == 'POST':
        vr_form = Visitor_Form(request.POST,instance=visitor)
        if vr_form.is_valid():
            vr_form.save() 
            messages.success(request, f'Visitor {visitor} - update successful')
            return redirect('visitor_details', pk)
    context = {'vr_form':vr_form}
    return render(request,'visitor_update.html',context=context)

@login_required
def visitor_delete_view(request,pk):
    visitor = get_object_or_404(Visitor,id=pk)
    context = {'instance':visitor}
    return render(request,'modal_delete.html',context=context)

@login_required
def leave_add_view(request):
    l_form = Leave_Form()
    if request.method == 'POST':
        l_form = Leave_Form(request.POST)
        if l_form.is_valid():
            l_form.save() 
            name = l_form.cleaned_data.get('prisoner')
            messages.success(request, f'Leave for prisoner {name} - creation successful')
            return redirect('leaves')
    context = {'l_form':l_form}
    return render(request,'leave_add.html',context=context)

@login_required
def leave_update_view(request,pk):
    leave = get_object_or_404(Leave,id=pk)
    l_form = Leave_Form(instance=leave)
    if request.method == 'POST':
        l_form = Leave_Form(request.POST,instance=leave)
        if l_form.is_valid():
            l_form.save() 
            messages.success(request, f'Leave {leave} - update successful')
            return redirect('leave_details', pk)
    context = {'l_form':l_form}
    return render(request,'leave_update.html',context=context)

@login_required
def leave_delete_view(request,pk):
    leave = get_object_or_404(Leave,id=pk)
    context = {'instance':leave}
    return render(request,'modal_delete.html',context=context)

@login_required
def leave_details_view(request, pk):
    leave = get_object_or_404(Leave,id=pk)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            leave = get_object_or_404(Leave,id=pk)
            messages.success(request, f'Leave for prisoner {leave.prisoner} - deletion successful')
            leave.delete()
            return redirect('leaves')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'leave':leave}
    return render(request,'leave_details.html',context)

@login_required
def leaves_view(request):
    leaves = Leave.objects.all()
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            leave = get_object_or_404(Leave,id=pk)
            messages.success(request, f'Leave for prisoner {leave.prisoner} - deletion successful')
            leave.delete()
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'leaves':leaves}
    return render(request,'leaves.html',context)

@login_required
def transfer_add_view(request):
    t_form = Transfer_Form()
    if request.method == 'POST':
        t_form = Transfer_Form(request.POST)
        if t_form.is_valid():
            t_form.save() 
            name = t_form.cleaned_data.get('prisoner')
            messages.success(request,f'Transfer for prisoner {name} - creation successful')
            return redirect('transfers')
    context = {'t_form':t_form}
    return render(request,'transfer_add.html',context=context)

@login_required
def transfer_update_view(request,pk):
    transfer = get_object_or_404(Transfer,id=pk)
    t_form = Transfer_Form(instance=transfer)
    if request.method == 'POST':
        t_form = Transfer_Form(request.POST,instance=transfer)
        if t_form.is_valid():
            t_form.save() 
            name = t_form.cleaned_data.get('prisoner')
            messages.success(request,f'Transfer for prisoner {name} - update successful')
            return redirect('transfer_details', pk)
    context = {'t_form':t_form}
    return render(request,'transfer_update.html',context=context)

@login_required
def transfer_delete_view(request,pk):
    transfer = get_object_or_404(Transfer,id=pk)
    context = {'instance':transfer}
    return render(request,'modal_delete.html',context=context)

@login_required
def transfer_details_view(request, pk):
    transfer = get_object_or_404(Transfer,id=pk)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            transfer = get_object_or_404(Transfer,id=pk)
            transfer.delete()
            messages.success(request,f'Transfer for prisoner {transfer.prisoner} - deletion successful')
            return redirect('transfers')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'transfer':transfer}
    return render(request,'transfer_details.html',context)

@login_required
def transfers_view(request):
    transfers = Transfer.objects.all()
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            transfer = get_object_or_404(Transfer,id=pk)
            transfer.delete()
            messages.success(request,f'Transfer for prisoner {transfer.prisoner} - deletion successful')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'transfers':transfers}
    return render(request,'transfers.html',context)

@login_required
def complain_add_view(request):
    c_form = Complain_Form()
    if request.method == 'POST':
        c_form = Complain_Form(request.POST)
        if c_form.is_valid():
            c_form.save() 
            name = c_form.cleaned_data.get('prisoner')
            messages.success(request, f'Complain for {name} - creation successful')
            return redirect('complains')
    context = {'c_form':c_form}
    return render(request,'complain_add.html',context=context)

@login_required
def complain_update_view(request,pk):
    complain = get_object_or_404(Complain,id=pk)
    c_form = Complain_Form(instance=complain)
    if request.method == 'POST':
        c_form = Complain_Form(request.POST,instance=complain)
        c_form.save() 
        messages.success(request, f'Complain {complain} - update successful')
        return redirect('complain_details', pk)
    context = {'c_form':c_form}
    return render(request,'complain_update.html',context=context)

@login_required
def complain_delete_view(request,pk):
    complain = get_object_or_404(Complain,id=pk)
    context = {'instance':complain}
    return render(request,'modal_delete.html',context=context)

@login_required
def complain_details_view(request, pk):
    complain = get_object_or_404(Complain,id=pk)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            complain = get_object_or_404(Complain,id=pk)
            complain.delete()
            messages.success(request, f'Complain {complain} - deletion successful')
            return redirect('complains')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'complain':complain}
    return render(request,'complain_details.html',context)

@login_required
def complains_view(request):
    complains = Complain.objects.all()
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            complain = get_object_or_404(Complain,id=pk)
            complain.delete()
            messages.success(request, f'Complain {complain} - deletion successful')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'complains':complains}
    return render(request,'complains.html',context)



