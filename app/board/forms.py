from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .models import Submission


def mod11(nr: int):
    mod11_sum = 0

    for i, digit in enumerate(reversed(str(nr))):
        mod11_sum += (i + 1) * int(digit)

    return mod11_sum % 11 == 0


class SubmitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('index')
        self.helper.add_input(Submit('submit', _('Submit')))

    def clean_student_number(self):
        nr = self.cleaned_data['student_number']

        if 7 > len(str(nr)) > 8:
            raise ValidationError(_('Invalid student number'), code='length')

        if not(mod11(nr)):
            raise ValidationError(_('Invalid student number'), code='mod11')

        return nr

    class Meta:
        model = Submission
        fields = [
            'name',
            'student_number',
            'type',
            'staff',
            'submission',

        ]
