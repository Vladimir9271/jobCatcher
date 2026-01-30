from django import forms
from django.utils.text import slugify
from .models import Vacancy
from unidecode import unidecode

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['job', 'name', 'description', 'salary']   
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Название вакансии',
            }),
            'job': forms.Select(),
            'description': forms.Textarea(attrs={'rows': 5}),
            'salary': forms.NumberInput(),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)

       
        instance.slug = slugify(unidecode(instance.name))

        
        instance.available = True

        if commit:
            instance.save()
        return instance
