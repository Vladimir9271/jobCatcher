from django.shortcuts import render, get_object_or_404, redirect
from .models import Vacancy, Job
from django.contrib.auth.decorators import login_required
from .forms import VacancyForm

def vacancy_list(request):
    jobs = Job.objects.all()
    selected_job = request.GET.get('job')
    vacancies = Vacancy.objects.filter(available=True)

    if selected_job:
        vacancies = vacancies.filter(job__slug=selected_job)
    
    context = {
        'vacancies': vacancies,
        'jobs': jobs,
        'selected_job': selected_job,
    }
    return render(request, 'main/vacancy_list.html', context)

def about(request):
    return render(request, 'main/about.html')

def vacancy_detail(request, slug):

    vacancy = get_object_or_404(Vacancy, slug=slug, available=True)

    recommendations = Vacancy.objects.filter(
        job=vacancy.job,
        available=True
    ).exclude(id=vacancy.id).order_by('-created')[:4]
    
    context = {
        'vacancy': vacancy,
        'recommendations': recommendations,
    }
    return render(request, 'main/vacancy_detail.html', context)

@login_required
def vacancy_create(request):
    # Простая проверка роли
    if request.user.role != 'employer':
        # Можно перенаправить на другую страницу или показать ошибку
        return redirect('vacancy_list')
    
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            # Здесь можно связать вакансию с пользователем
            # vacancy.user = request.user
            vacancy.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm()
    
    return render(request, 'main/vacancy_form.html', {'form': form})


