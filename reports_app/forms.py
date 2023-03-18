from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

class Period_Form(forms.Form):
    date_range = forms.BooleanField(label='All times',required=False)
    start_date = forms.DateField(widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})),required=False)
    end_date = forms.DateField(widget=(DatePickerInput(attrs={'placeholder':' yyyy-mm-dd '})),required=False)

REPORT_CHOICES = [
    ('Prisoners', 'Prisoners'),
    ('Transfers', 'Transfers'),
    ('Complaints', 'Complaints'),
    ('Releases', 'Releases'),
]

class Report_Form(forms.Form):
    report= forms.CharField(label='Choose Report Type', widget=forms.RadioSelect(choices=REPORT_CHOICES))

