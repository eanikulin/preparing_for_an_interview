from django import forms
from product.models import Product


class DateInput(forms.DateInput):
    input_type = 'date'

class ProductForm(forms.ModelForm):
    class Meta:
        widgets = {'date': DateInput()}
        model = Product
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
