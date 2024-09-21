from django.forms import ModelForm, ValidationError

from catalog.models import Product, Version


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

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for each in forbidden_words:
            if each in cleaned_data:
                raise ValidationError('Извините, такое описание недопустимо для продукта')

        return cleaned_data


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
