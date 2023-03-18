from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
import datetime
from dateutil.relativedelta import relativedelta
from .forms import *            
from .models import *            

# Create your views here.
def script(request):
    # transfers = Cell.objects.all()
    # for cell in transfers:
    #     print(cell.name,cell.status)
    #     print(cell.prisoner_set.count())
    #     if cell.prisoner_set.count() == 0:
    #         cell.status = "Empty"
    #         cell.save()
    #     elif cell.prisoner_set.count() <= cell.max_inmates:
    #         cell.status = "Contained"
    #         cell.save()
    #     else:
    #         cell.status = "Full"        
    #         cell.save()
    today = datetime.date.today()
    next_today = today + relativedelta(months=1)
    # prisoner.release_date = prisoner.entry_date + relativedelta(years=prisoner.crime.detention_period)
    print(today,next_today)
    return HttpResponse('Done')    
    
@login_required
def crimes_view(request):
    crimes = Crime.objects.all()
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            crime = get_object_or_404(Crime,id=pk)
            crime.delete()
            messages.success(request, f'Crime {crime} - Deletion successful')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'crimes':crimes}
    return render(request,'crimes.html',context)

@login_required
def crime_add_view(request):
    c_form = Crime_Form()
    if request.method == 'POST':
        c_form = Crime_Form(request.POST)
        if c_form.is_valid():
            c_form.save()
            name = c_form.cleaned_data.get('name')
            messages.success(request, f'Crime {name} - Creation successful') 
            return redirect('Crimes')
    context = {'c_form':c_form}
    return render(request,'Crime_add.html',context=context)

@login_required
def crime_details_view(request, pk):
    crime = get_object_or_404(Crime,id=pk)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            crime = get_object_or_404(Crime,id=pk)
            crime.delete()
            messages.success(request, f'Crime {crime} - Deletion successful')
            return redirect('crimes')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'crime':crime}
    return render(request,'crime_details.html',context)

@login_required
def crime_update_view(request,pk):
    crime = get_object_or_404(Crime,id=pk)
    c_form = Crime_Form(instance=crime)
    if request.method == 'POST':
        c_form = Crime_Form(request.POST,instance=crime)
        if c_form.is_valid():
            c_form.save() 
            messages.success(request, f'Crime {crime} - Update successful')
            return redirect('crime_details', pk)
    context = {'c_form':c_form}
    return render(request,'crime_update.html',context=context)

@login_required
def crime_delete_view(request,pk):
    crime = get_object_or_404(Crime,id=pk)
    context = {'instance':crime}
    return render(request,'modal_delete.html',context=context)

@login_required
def complaints_view(request):
    complaints = Complaint.objects.all()
    pending = complaints.filter(status="Pending")
    approved = complaints.filter(status="Approved")
    denied = complaints.filter(status="Denied")
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            complaint = get_object_or_404(Complaint,id=pk)
            complaint.delete()
            messages.success(request,f'Complaint {complaint} - deletion successful')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'complaints':complaints,'pending':pending,'approved':approved,'denied':denied}
    return render(request,'complaints.html',context)

@login_required
def complaint_add_view(request):
    c_form = Complaint_Add_Form()
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'add':
            c_form = Complaint_Add_Form(request.POST)
            if c_form.is_valid():
                c_form.save() 
                name = c_form.cleaned_data.get('prisoner')
                messages.success(request,f'Complaint for {name} - creation successful')
                return redirect('complaints')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'c_form':c_form}
    return render(request,'complaint_add.html',context=context)

@login_required
def complaint_details_view(request, pk):
    complaint = get_object_or_404(Complaint,id=pk)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            complaint = get_object_or_404(Complaint,id=pk)
            complaint.delete()
            messages.success(request, f'Complaint {complaint} - deletion successful')
            return redirect('complaints')
        elif name == 'approval'   :
            pk = str(request.POST.get('instance_id'))
            apr = str(request.POST.get('approval'))
            complaint = get_object_or_404(Complaint,id=pk)
            today = datetime.date.today()
            if apr == "Approve":
                complaint.status = "Approved"
                complaint.date = today + relativedelta(months=2)
                complaint.feedback = f'You complaint has been approved and your court date it {complaint.date}'
                complaint.save()
            elif apr == "Deny":
                complaint.status = "Denied"
                complaint.date = None
                complaint.feedback = f'Your complaint has been denied by the Court'
                complaint.save()
            else:
                complaint.status = "Pending"
                complaint.date = None
                complaint.feedback = default_feedback
                complaint.save()
            messages.success(request, f'Complaint {complaint} was {complaint.status} successful')
            return redirect('complaints')

        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'complaint':complaint}
    return render(request,'complaint_details.html',context)

@login_required
def complaint_update_view(request,pk):
    complaint = get_object_or_404(Complaint,id=pk)
    c_form = Complaint_Update_Form(instance=complaint)
    if request.method == 'POST':
        c_form = Complaint_Update_Form(request.POST,instance=complaint)
        if c_form.is_valid():
            c_form.save() 
            messages.success(request, f'Complaint {complaint} - update successful')
            return redirect('complaint_details', pk)
    context = {'c_form':c_form,'complaint':complaint}
    return render(request,'complaint_update.html',context=context)

@login_required
def complaint_delete_view(request,pk):
    complaint = get_object_or_404(Complaint,id=pk)
    context = {'instance':complaint}
    return render(request,'modal_delete.html',context=context)

@login_required
def complaint_approval_view(request,pk,apr):
    complaint = get_object_or_404(Complaint,id=pk)
    approval = apr
    print(approval)
    context = {'instance':complaint,'approval':approval}
    return render(request,'modal_approval.html',context=context)

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
    p_form = Prisoner_Add_Form()
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'add':
            p_form = Prisoner_Add_Form(request.POST,request.FILES)
            if p_form.is_valid():
                name = p_form.cleaned_data.get('firstname')
                prisoner = p_form.save() 
                prisoner.release_date = prisoner.entry_date + relativedelta(years=prisoner.crime.detention_period)
                prisoner.save()
                print(prisoner.entry_date,prisoner.release_date)
                messages.success(request, f'Prisoner {name} creation successful')
                return redirect('prisoners')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
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
def prisoner_details_modal_view(request, pk):
    prisoner = get_object_or_404(Prisoner,id=pk)
    print("some thing")
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
    return render(request,'prisoner_details_modal.html',context)

@login_required
def prisoner_update_view(request,pk):
    prisoner = get_object_or_404(Prisoner,id=pk)
    p_form = Prisoner_Update_Form(instance=prisoner)
    if request.method == 'POST':
        p_form = Prisoner_Update_Form(request.POST,request.FILES,instance=prisoner)
        print(p_form.errors)
        if p_form.is_valid():
            prisoner = p_form.save() 
            prisoner.release_date = prisoner.entry_date + relativedelta(years=prisoner.crime.detention_period)
            prisoner.save()
            print(prisoner.entry_date,prisoner.release_date)
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
    print("'*****************************")
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
def release_form_view(request,pk):
    prisoner = get_object_or_404(Prisoner,id =pk)
    context = {'prisoner':prisoner}
    return render(request,'release_form.html',context=context)

@login_required
def release_details_view(request, pk):
    release = get_object_or_404(Release,id=pk)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            release = get_object_or_404(Release,id=pk)
            release.delete()
            messages.success(request, f'Release {release} - deletion successful')
            return redirect('releases')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'release':release}
    return render(request,'release_details.html',context)

@login_required
def releases_view(request):
    releases = Release.objects.all()
    all_prisoners = Prisoner.objects.all()
    today = datetime.date.today()
    today_yr = today.year
    print(today_yr)
    prisoners = []
    for prisoner in all_prisoners:
        if prisoner.release_date is not None:
            year = prisoner.release_date.year
            if year == today_yr:
                prisoners.append(prisoner)    
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            release = get_object_or_404(Release,id=pk)
            release.delete()
            messages.success(request, f'Release {release} - deletion successful')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'releases':releases,'prisoners':prisoners}
    return render(request,'releases.html',context)

@login_required
def cell_add_view(request):
    c_form = Cell_Form()
    print('passed')
    if request.method == 'POST':
        c_form = Cell_Form(request.POST)
        print(c_form.errors)
        if c_form.is_valid():
            c_form.save() 
            name = c_form.cleaned_data.get('prisoner')
            messages.success(request, f'Cell for {name} - creation successful')
            return redirect('cells')
    context = {'c_form':c_form}
    return render(request,'cell_add.html',context=context)

@login_required
def cell_update_view(request,pk):
    cell = get_object_or_404(Cell,id=pk)
    c_form = Cell_Form(instance=cell)
    if request.method == 'POST':
        c_form = Cell_Form(request.POST,instance=cell)
        print(c_form.errors)
        if c_form.is_valid():
            c_form.save() 
            messages.success(request, f'Cell {cell} - update successful')
            return redirect('cell_details', pk)
    context = {'c_form':c_form}
    return render(request,'cell_update.html',context=context)

@login_required
def cell_delete_view(request,pk):
    cell = get_object_or_404(Cell,id=pk)
    context = {'instance':cell}
    return render(request,'modal_delete.html',context=context)

@login_required
def cell_details_view(request, pk):
    cell = get_object_or_404(Cell,id=pk)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            cell = get_object_or_404(Cell,id=pk)
            cell.delete()
            messages.success(request, f'Cell {cell} - deletion successful')
            return redirect('cells')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'cell':cell}
    return render(request,'cell_details.html',context)

@login_required
def cells_view(request):
    cells = Cell.objects.all()
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            cell = get_object_or_404(Cell,id=pk)
            cell.delete()
            messages.success(request, f'Cell {cell} - deletion successful')
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'cells':cells}
    return render(request,'cells.html',context)

def render_pdf_view(request):
    template_path = 'report_cells.html'
    context = {'cells': Cell.objects.all()}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report_cells.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)
    # if error then show some funny view
    #if pisa_status.errors:
    #   return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    #return render(request, 'report_cells.html',context)