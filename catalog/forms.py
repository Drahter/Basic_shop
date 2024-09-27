from django.forms import ModelForm, ValidationError, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
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


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("category", "description", "is_active")


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
