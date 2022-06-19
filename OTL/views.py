import csv
import time

from django.shortcuts import render
from .models import SpecsValueMap


# Create your views here.

def get_otl_screen(request):
    context = {}
    model_list = []
    if request.method == 'POST':
        start_time = time.time()
        context['spec_id_list'] = SpecsValueMap.objects.values_list('spec_id', flat=True).distinct().order_by('spec_id')
        context['model_id_list'] = SpecsValueMap.objects.values_list('model_id', flat=True).distinct()
        for model_id in context['model_id_list']:
            model = {
                'sku': model_id
            }
            model.update(dict(
                SpecsValueMap.objects.filter(model_id=model_id).values_list('spec_id', 'value').distinct().order_by(
                    'spec_id')))
            model_list.append(model)
        # print(model_list)

        if model_list:
            with open('File/Names.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=model_list[0].keys())
                writer.writeheader()
                writer.writerows(model_list)
                print('File Written')

        context['model_list'] = model_list
        context['time_taken_ms'] = (time.time() - start_time) * 1000
        context['time_taken'] = time.time() - start_time
        context['total_no'] = model_list.__len__()
        return render(request, 'OTL/show_data.html', context)

    context['spec_list'] = SpecsValueMap.objects.all()
    return render(request, 'OTL/home.html', context)
