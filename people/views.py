import os
import csv
from django.shortcuts import render
from .forms import FileUploadForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.validators import validate_email
from collections import defaultdict
from .models import uploadData
from django.shortcuts import render, get_object_or_404, redirect
import pdb

from django.db.models import get_model
# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def file_reader(f):
    return csv.DictReader(f)


def upload_file(request):
    obj = uploadData.objects.all()
    
    if request.method == 'POST':
        models = uploadData._meta.get_all_field_names()
        form_data = {}
        headers_all = []
        data =[]
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            
            reader = file_reader(request.FILES["file"])
            for row in reader:
                data.append(row)
            headers = reader.fieldnames
            for header in headers:
                headers_all.append(header)
 
        
        for key, value in request.POST.dict().items():
            if not key == 'csrfmiddlewaretoken':
                form_data.update({key:value})
        
        #print form_data
        for k,v in form_data.items():
            print k + '' + v  #this is working
        # # print data
        for d in data:
            print d #this is working

        # I'm combining and doing the same thing through nested loop but this isn't working
        for d in data:
            for k, v in form_data.items():
                print d[v], v, d
                # print d[k]
            

        return render(request, 'people/upload.html', {'objects': obj, 'headers':headers_all, 'models':models})
    else:
        form = FileUploadForm()
    
    return render(request, 'people/upload.html', {'form': form})

def complete_upload(request):
    # if request.method = 'POST':
    #     field = request.POST.get('')

    obj = uploadData.objects.all()
    return render(request, 'people/complete.html', {'test':obj})

