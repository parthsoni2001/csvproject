from django.shortcuts import render
import pandas as pd
import json
from user.forms import UploadCSVForm

# Create your views here.
def home(request):
    context = {}
    if request.method == 'POST':
        # print(request.FILES["upload"])
        # print(request.FILES["upload"].content_type)
        # form = {}
        # form = UploadPDFForm(request.POST, request.FILES)
        files = request.FILES.getlist('upload')
        for x in files:
            df = pd.read_csv(x)
            result = df.to_json(orient="split")
            parsed = json.loads(result)
            # out = json.dumps(parsed, indent=4)
            # print(parsed)
        context['out'] = parsed 
        return render(request, 'table.html', context) 
    else:
        context["form"] = UploadCSVForm()
    
    return render(request, 'home.html', context)

def table(request):
    return render(request, 'table.html')