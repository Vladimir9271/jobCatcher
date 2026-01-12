from django.shortcuts import render, get_object_or_404
from .models import Vacancy, Job

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

def vacancy_detail(request, slug):

    vacancy = get_object_or_404(Vacancy, slug=slug, available=True)

    recommendations = Vacancy.objects.filter(
        job=vacancy.job,
        available=True
    ).exclude(id=vacancy.id).order_by('-created')[:4]  # 4 последние вакансии
    
    context = {
        'vacancy': vacancy,
        'recommendations': recommendations,
    }
    return render(request, 'main/vacancy_detail.html', context)