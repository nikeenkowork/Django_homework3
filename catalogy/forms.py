from django import forms
from .models import Product

FORBIDDEN_WORDS = (
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control"
            })

        self.fields["name"].widget.attrs.update({
            "placeholder": "Введите название"
        })

        self.fields["price"].widget.attrs.update({
            "placeholder": "Введите цену"
        })

        self.fields["description"].widget.attrs.update({
            "placeholder": "Введите описание"
        })

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is not None and price < 0:
            raise forms.ValidationError(
                "Цена продукта не может быть отрицательной."
            )

        return price

    def clean(self):
        cleaned_data = super().clean()

        name = (cleaned_data.get("name") or "").lower()
        description = (cleaned_data.get("description") or "").lower()

        for word in FORBIDDEN_WORDS:
            if word in name or word in description:
                raise forms.ValidationError(
                    f'Нельзя использовать слово "{word}".'
                )

        return cleaned_data
