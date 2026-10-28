from django.shortcuts import render, redirect
from .models import Teacher

# Create your views here.
def teachers_list (request):
    teachers = Teacher.objects.all()
    return render(request, 'index.html', {'teachers': teachers})


def add_teacher(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        subject = request.POST.get('subject')
        image = request.FILES.get('image')

        teacher_info = Teacher(name=name, email=email, contact_number=contact_number, subject=subject, image= image if image else None)
        teacher_info.save()
        return redirect('teachers_list')
    return render(request, 'index.html')


