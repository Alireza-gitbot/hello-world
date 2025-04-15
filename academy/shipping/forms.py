from django import forms
from django.core.exceptions import ValidationError

from lib.validators import min_length_validator
from shipping.models import ShippingAddress


class ShippingAddressForm(forms.ModelForm):
    # zipcode = forms.CharField(validators=[min_length_validator])

    class Meta:
        model = ShippingAddress
        fields = ('city', 'zipcode', 'address', 'number')
        # exclude = ('city',)
        # fields = "__all__"

    def clean_zipcode(self):
        zipcode = self.cleaned_data['zipcode']
        # city = self.cleaned_data('city')
        if len(zipcode) != 16:
            raise ValidationError("length is not 16")
        return zipcode

    def clean(self):
        clean_data = super().clean()
        return clean_data