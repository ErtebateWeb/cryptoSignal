from django import forms
from .models import binarysignal


class SignalForm(forms.ModelForm):
    class Meta:
        model = binarysignal


        fields = (
            'SymbolTitle', 'TimeFrame', 'NowPrice', 'TriggerPrice', 'StopLoss', 'TakeProfit1', 'TakeProfit2',
            'TakeProfit3', 'TakeProfit4', 'updatedDate', 'Publisher', 'Images',)
        widgets = {
            'SymbolTitle': forms.TextInput(attrs={'placeholder': 'Enter Symbols','class': 'form-control'}),
            'TimeFrame': forms.TextInput(attrs={'class': 'form-control'}),
            'NowPrice': forms.TextInput(attrs={'placeholder': 'Enter Now Price','class': 'form-control'}),
            'TriggerPrice': forms.TextInput(attrs={'class': 'form-control'}),
            'StopLoss': forms.TextInput(attrs={'class': 'form-control'}),
            'TakeProfit1': forms.TextInput(attrs={'class': 'form-control'}),
            'TakeProfit2': forms.TextInput(attrs={'class': 'form-control'}),
            'TakeProfit3': forms.TextInput(attrs={'class': 'form-control'}),
            'TakeProfit4': forms.TextInput(attrs={'class': 'form-control'}),
            'updatedDate': forms.TextInput(attrs={'class': 'form-control'}),
             'Publisher': forms.Select(attrs={'class': 'form-control'}),

        }

# class SubmitSignals(forms.Form):
#     SymbolTitle = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter symbol"}))
#     TimeFrame = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter symbol"}))
#     NowPrice = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter symbol"}))
#     TriggerPrice = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter symbol"}))
#     StopLoss = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter symbol"}))
#     TakeProfit1 = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter symbol"}))
#     TakeProfit2 = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter symbol"}))
#     TakeProfit3 = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter symbol"}))
#     TakeProfit4 = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter symbol"}))
#     Publisher = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter symbol"}))
#     Images = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter symbol"}))
#
#
#
#
#     # def clean_email(self):
#     #     email = self.cleaned_data.get("email")
#     #
#     #     if not "gmail.com" in email:
#     #         raise forms.ValidationError("Email has to be gmail.com")
#     #
#     #     return email
