from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput,TimePickerInput,DateTimePickerInput,MonthPickerInput,YearPickerInput
from django.core.validators import MaxLengthValidator
from .models import *

class Crime_Form(forms.ModelForm):
    class Meta:
        model = Crime
        fields = "__all__"

class Prisoner_Add_Form(forms.ModelForm):
    entry_date = forms.DateField(widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})))

    class Meta:
        model = Prisoner
        fields = "__all__"

class Prisoner_Add_Form(forms.ModelForm):
    entry_date = forms.DateField(widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})))

    class Meta:
        model = Prisoner
        fields = "__all__"

    def clean(self):
        # data from the form is fetched using super function
        super(Prisoner_Form, self).clean()
        prisoner_id = self.cleaned_data.get('identification')
        prisoners_ids = []
        for prisoner in Prisoner.objects.all():
            prisoners_ids.append(prisoner.identification)
        if prisoner_id in prisoners_ids:
            print("same ID")
            self._errors['identification'] = self.error_class(['A Prisoner with similar ID already exists'])
        else:
            print("New ID")
        # return any errors if found
        return self.cleaned_data

class Prisoner_Update_Form(forms.ModelForm):
    entry_date = forms.DateField(widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})))

    class Meta:
        model = Prisoner
        fields = "__all__"

class Complaint_Add_Form(forms.ModelForm): 
    date = forms.DateField(required=False, widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})))
    class Meta:
        model = Complaint
        fields = "__all__"

    def clean(self):
        # data from the form is fetched using super function
        super(Complaint_Add_Form, self).clean()
        prisoner = self.cleaned_data.get('prisoner')
        prisoners_with_complaints = []
        for complaint in Complaint.objects.all():
            prisoners_with_complaints.append(complaint.prisoner)
        print(len(prisoners_with_complaints))
        if prisoner in prisoners_with_complaints:
            print("Has complaint")
            self._errors['prisoner'] = self.error_class(['The selected prisoner has a pending Complaint'])
        else:
            print("Has No complaint")
        # return any errors if found
        return self.cleaned_data

class Complaint_Update_Form(forms.ModelForm): 
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
