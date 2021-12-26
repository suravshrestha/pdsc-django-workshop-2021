from django import forms


class FormAverage(forms.Form):
    # Validations are handled by django forms
    first_number = forms.DecimalField()
    second_number = forms.DecimalField()
