from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    emailconf = forms.EmailField(label='Confirm Email')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        emailconf = all_clean_data['emailconf']

        if email != emailconf:
            raise forms.ValidationError("Email addresses do not match.")
