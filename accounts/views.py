from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth import logout as auth_logout


def register(request):
    if request.method == 'POST':
        print("=== DEBUG REGISTRATION ===")
        print("POST данные:", dict(request.POST))
        
        form = RegisterForm(request.POST)
        print("Форма валидна?", form.is_valid())
        
        if form.is_valid():
            user = form.save()
            print("Пользователь создан:", user.username, user.role)
            login(request, user)
            print("Пользователь авторизован")
            return redirect('vacancy_list')   
        else:
            print("Ошибки формы:")
            for field, errors in form.errors.items():
                print(f"  {field}: {errors}")
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('/')   