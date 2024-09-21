from django.forms import ModelForm, ValidationError

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['created_at', 'updated', 'views_counter']

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for each in forbidden_words:
            if each in cleaned_data:
                raise ValidationError('Извините, такое название недопустимо для продукта')

        return cleaned_data
