from django import forms
from .models import *

class Case_Form(forms.ModelForm):
    class Meta:
        model = Case
        fields = "__all__"

class Prisoner_Form(forms.ModelForm):
    class Meta:
        model = Prisoner
        fields = "__all__"

class Visitor_Form(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = "__all__"

class Visit_Form(forms.ModelForm):
    class Meta:
        model = Visit
        fields = "__all__"

class Leave_Form(forms.ModelForm):
    class Meta:
        model = Leave
        fields = "__all__"

class Transfer_Form(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = "__all__"

class Complain_Form(forms.ModelForm):
    class Meta:
        model = Complain
        fields = "__all__"