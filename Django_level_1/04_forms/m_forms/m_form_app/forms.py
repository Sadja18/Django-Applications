from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again: ")
    text = forms.CharField(widget=forms.Textarea)

    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError("BOt InPUT")

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        ver_email = all_clean_data["verify_email"]

        if email != ver_email:
            raise forms.ValidationError("Email entry mismatch   ")
