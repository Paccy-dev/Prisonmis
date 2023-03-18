from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.staticfiles import finders
from xhtml2pdf import pisa
from .forms import *
from prisoners_app.models import Prisoner,Transfer,Complaint,Release

@login_required
def report_view(request):
    r_form = Report_Form()
    p_form = Period_Form()
    if request.method == 'POST':
        logout(request)
        messages.success(request, f'Logout successful')
        return redirect('login')
    context = {'r_form':r_form,'p_form':p_form}
    return render(request, 'reports.html', context)

def report_generate_view(request):
    r_form = Report_Form(request.POST)
    p_form = Period_Form(request.POST)
    if r_form.is_valid():
        report = r_form.cleaned_data.get('report')
    if p_form.is_valid():
        date_range = p_form.cleaned_data.get('date_range')
        start_date = p_form.cleaned_data.get('start_date')
        end_date = p_form.cleaned_data.get('end_date')  
        today = datetime.now().date
    if report == 'Prisoners':
        if date_range == True:
            instances = Prisoner.objects.all()
        else:
            instances = []
            for prisoner in Prisoner.objects.all():
                date = prisoner.entry_date
                if date >= start_date and date <= end_date:
                    instances.append(prisoner)
    elif report == 'Transfers':
        if date_range == True:
            instances = Transfer.objects.all()
        else:
            instances = []
            for transfer in Transfer.objects.all():
                date = transfer.date
                if date > start_date and date <= end_date:
                    instances.append(transfer)
    if report == 'Complaints':
        if date_range == True:
            instances = Complaint.objects.all()
        else:
            instances = []
            for complaint in Complaint.objects.all():
                date = complaint.date
                if date > start_date and date <= end_date:
                    instances.append(transfer)
    if report == 'Releases':
        if date_range == True:
            instances = Prisoner.objects.all()
        else:
            instances = []
            for release in Prisoner.objects.all():
                date = release.release_date 
                if date > start_date and date <= end_date:
                    instances.append(release)
        
    template_path = 'report_generate.html'
    context = {'report':report,'instances': instances,'start_date':start_date,'end_date':end_date,'today':today}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
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
