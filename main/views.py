from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.views.generic import View
from django.core.files.storage import FileSystemStorage


from .models import ImageSet
from .forms import ImageForm
from .functions import handle_file

import img2pdf
import os
import time
# Create your views here.


def index(request):
    csrf_token = get_token(request)
    return render(request, 'main/index.html')


def view(request):
    fs = FileSystemStorage()
    filename = 'try.pdf'
    if fs.exists(f'media/{filename}'):
        with open(f'media/{filename}') as pdf:
            response = HttpResponse(
                pdf,
                content_type='application/pdf'
            )
            response['Content-Disposition'] = f'inline; filename={filename}'
            return response
        pdf.close()


class PDFHandlerView(View):

    def post(self, request):
        if request.method == "POST":
            length = request.POST['length']
            title = request.POST['title']

            new_length = int(length)
            inputFile = []

            for file_num in range(0, new_length):
                inputFile.append(request.FILES.get(f'images{file_num}'))

            outputFile = open(f'media/{title}.pdf', 'wb')

            outputFile.write(img2pdf.convert(inputFile))

            outputFile.close()

            if os.path.exists(f'media/{title}.pdf'):
                ImageSet.objects.create(
                    pdf_file=f'{title}.pdf'
                )

            # if os.path.exists(f'media/{title}.pdf'):
            #     time.sleep(10)
            #     os.remove(f'media/{title}.pdf')

        return JsonResponse({
            'message': "There's nothing!"
        }, content_type="application/json", status=200)
