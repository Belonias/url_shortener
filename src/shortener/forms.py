from django import forms
from .validators import validate_dot_com, validate_url

class SubmitUrlForm(forms.Form):
    #custom made validator
    url = forms.CharField(label='Submit URL', validators=[validate_url])

    """def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()
        print(cleaned_data)
        url = cleaned_data.get('url')
        url_validator = URLValidator()
        try:
            url_validator(url)
        except:
            raise forms.ValidationError("Invalid Url")
        return url"""

"""    #only for SubmitUrlForm.url
    def clean_url(self):
        url = self.cleaned_data['url']
        url_validator = URLValidator()
        if not "com" in url:
            raise forms.ValidationError("Invalid Url")
        return url
"""
