from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, FileResponse
from django.middleware.csrf import get_token
from django.views.generic import View
from django.core.files.storage import FileSystemStorage


from .models import User, FileSet
from .functions import handle_file

import img2pdf
import os
import time
# Create your views here.


def index(request):
    csrf_token = get_token(request)
    return render(request, 'main/index.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "main/login.html")
    return render(request, "main/login.html")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["password2"]
        if password != confirmation:
            return render(request, "main/register.html")

        user = User.objects.create_user(username, email, password)
        user.save()

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "main/register.html")


def user_pdf(request):
    all_pdf = FileSet.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "main/userpdf.html", {"pdfs": all_pdf})


def pdf_delete(request, id):

    pdf = FileSet.objects.get(id=id)
    if os.path.exists(f'mediafiles/{pdf.name}.pdf'):
        os.remove(f'mediafiles/{pdf.name}.pdf')
    pdf.delete()

    return HttpResponseRedirect(reverse('pdfs'))


def pdf_view(request, id):
    pdf = FileSet.objects.get(id=id)
    file_name = pdf.name
    return FileResponse(open(f'mediafiles/{file_name}.pdf', 'rb'))


class PDFHandlerView(View):

    def post(self, request):
        if request.method == "POST":
            length = request.POST['length']
            title = request.POST['title']

            new_length = int(length)
            inputFile = []

            for file_num in range(0, new_length):
                inputFile.append(request.FILES.get(f'images{file_num}'))

            outputFile = open(f'mediafiles/{title}.pdf', 'wb')

            outputFile.write(img2pdf.convert(inputFile))

            outputFile.close()

            if os.path.exists(f'mediafiles/{title}.pdf'):
                FileSet.objects.create(
                    user=request.user,
                    name=title,
                    pdf_file=f'{title}.pdf'
                )

            return JsonResponse({
                'message': "There's nothing!"
            }, content_type="application/json", status=200)
        return JsonResponse({
            'message': "Sad"
        }, content_type="application/json", status=400)
