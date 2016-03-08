from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder

from .models import List


class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ['name', 'max_points', 'ships']

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-md-3'
    helper.field_class = 'col-md-9'
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
