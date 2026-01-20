from django import forms
from .models import Vacancy

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['job', 'name', 'slug', 'description', 'salary', 'available']
        widgets = {
            'slug': forms.HiddenInput(), 
            'name': forms.TextInput(attrs={
                'id': 'vacancy-name',
                'placeholder': 'Название вакансии',
                'onkeyup': 'generateSlug()'   
            }),
            'job': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'salary': forms.NumberInput(),
            'available': forms.CheckboxInput(),
        }
    
    def clean_slug(self):

        slug = self.cleaned_data.get('slug')
        name = self.cleaned_data.get('name')
        
        if not slug and name:
            slug = slugify(name)
        

        if Vacancy.objects.filter(slug=slug).exists():
            
            import random
            slug = f"{slug}-{random.randint(1000, 9999)}"
        
        return slug