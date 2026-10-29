from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
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


def update_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    if request.method == 'POST':
        teacher.name = request.POST.get('name')
        teacher.email = request.POST.get('email')
        teacher.contact_number = request.POST.get('contact_number')
        teacher.subject = request.POST.get('subject')
        image = request.FILES.get('image')
        if image:
            teacher.image = image
        teacher.save()
        return redirect('teachers_list')
    return render(request, 'index.html', {'teacher': teacher})



@require_POST
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher.delete()
    return redirect('teachers_list')