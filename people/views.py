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
from django.views.decorators.csrf import csrf_exempt
from django.db.models import get_model
# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# def file_reader(f):
#     return csv.reader(f)
key_data ={}
form_data = []
def upload_file(request):
    obj = uploadData.objects.all()
    models = uploadData._meta.get_all_field_names()
    headers_all = []
    
    if request.method == 'POST' and 'submit1' in request.POST:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.DictReader(request.FILES['file'])
            # return re
            headers = reader.next()
            for header in headers:
                # form_data[header] =[]
                headers_all.append(str(header))
                # print header
            for row in reader:
                print form_data.append(row)
                # k, v = row
                # form_data[k] = v
                    # print h,v
        
        return render(request, 'people/upload.html', {'objects': obj, 'headers':headers_all, 'models':models})
            # print form_data['name']
        # print form_data['name']
    if request.method == 'POST' and 'submit2' in request.POST:
        # print key_data
        for key, value in request.POST.dict().items():
            if not key == 'csrfmiddlewaretoken' and not key== 'submit2':
                # print key, value
                key_data.update({key:value})
        # if key_data:
        # new_value = uploadData.objects.create()
        # print "New_Vlue ", new_value
        # new_value.xyz = "checking"
        # print "xyz ", new_value
        # new_value.name = "checking name"
        # print "name ", new_value

    # print k
        # if k == 'email' :
        for value in form_data:
            new_value = uploadData.objects.create()
            for k,v in key_data.items():
                setattr(new_value, k, value[str(v)])
                # new_value.email = value['email']
                # new_value.name = value['name']
                # new_value.link = value['test_link']
                new_value.save()

                    
                    # print file['email'] for file in form_data
            #         new_value.save()
            # elif k == 'name':
            #     for value in form_data['name']:
            #         new_value.name = value
            #         new_value.save()
            # elif k == 'link':
            #     for value in form_data['test_link']:
            #         new_value.link = value
            #         new_value.save()

            # for value in form_data[str(v)]:
            #     new_value = uploadData.objects.create()
            #     print k, value
            #     con_k = str(k)
            #     print con_k, value
            #     new_value.name = value
            #     print new_value
            #     new_value.save()

                    # print value , k

                # new_value.k = form_data[str(v)]
                # new_value.save()
                # print form_data[str(v)], k
            # pdb.set_trace()
                # print form_data[str(v)]

        
            # for k, v in key_data.items():
            #     pdb.set_trace()
            #     print form_data[str(v)]
        # for k,v in form_data_form.items():
        #     print form_data[str(v)]
        # #print form_data
        # # for k,v in form_data.items():
        # #     print k + '' + v  #this is working
        # # # # print data
        # # for d in data:
        # #     print d #this is working

        # # I'm combining and doing the same thing through nested loop but this isn't working
        # print data[0]
            # for k, v in form_data.items():
            #     print d[v], v, d
            #     # print d[k]
            

        return render(request, 'people/upload.html', {'objects': obj, 'headers':headers_all, 'models':models})
    else:
        form = FileUploadForm()
    
    return render(request, 'people/upload.html', {'form': form})

def complete_upload(request):
    # if request.method = 'POST':
    #     field = request.POST.get('')

    obj = uploadData.objects.all()
    return render(request, 'people/complete.html', {'test':obj})

