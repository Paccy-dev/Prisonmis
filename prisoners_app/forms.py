from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput,TimePickerInput,DateTimePickerInput,MonthPickerInput,YearPickerInput
from .models import *

class Crime_Form(forms.ModelForm):
    class Meta:
        model = Crime
        fields = "__all__"

class Prisoner_Form(forms.ModelForm):
    entry_date = forms.DateField(widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})))
    class Meta:
        model = Prisoner
        fields = "__all__"


class Complaint_Form(forms.ModelForm): 
    date = forms.DateField(required=False, widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})))
    class Meta:
        model = Complaint
        fields = "__all__"

class Transfer_Form(forms.ModelForm):
    date = forms.DateField(required=False, widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})))
    class Meta:
        model = Transfer
        fields = "__all__"

class Release_Form(forms.ModelForm):
    class Meta:
        model = Release
        fields = "__all__"

class Cell_Form(forms.ModelForm):
    class Meta:
        model = Cell
        fields = "__all__"

class Report_Form(forms.Form):
    start_date = forms.DateField(widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})))
    end_date = forms.DateField(widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})))

#class Visitor_Form(forms.ModelForm):
    # class Meta:
    #     model = Visitor
    #     fields = "__all__"

#class Leave_Form(forms.ModelForm): 
    # start_date = forms.DateField(widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})))
    # end_date = forms.DateField(widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})))
    # class Meta:
    #     model = Leave
    #     fields = "__all__"
