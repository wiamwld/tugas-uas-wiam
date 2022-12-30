from django.shortcuts import render
from .forms import ContactForm
from .models import blog
# Create your views here.


def index(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    if request.POST:
        Form = ContactForm(request.POST, request.FILES)
        if Form.is_valid():
            Form.save()
            Form = ContactForm()
            pesan = "Data Berhasil Diupload"
            context = {
                'Form': Form,
                'pesan': pesan,
            }
            return render(request, 'tambah.html', context)
    else:
        Form = ContactForm()

        context = {
            'Form': Form,
        }

    return render(request, 'contact.html', context)
