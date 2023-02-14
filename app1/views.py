from django.shortcuts import render
from .models import *

def home(request):

    qidiruv_sozi = request.GET.get('searched')
    if qidiruv_sozi is not None and qidiruv_sozi != '' :
        t_s = Togri.objects.filter(soz__contains=qidiruv_sozi)
        if t_s:
            n_s = Notogri.objects.filter(t_soz=t_s[0])
        else:
            n_s = Notogri.objects.filter(n_soz__contains=qidiruv_sozi)

            if n_s:


                n_s = n_s | Notogri.objects.filter(t_soz=n_s[0].t_soz)
                t_s = [n_s[0].t_soz]
            else:
                t_s = ["So'z topilmadi"]



        data = {'togri_soz': t_s[0],
                'notogri_soz':n_s
        }
    else:
        data = {
            'togri_soz': '',
            'notogri_soz': ''
        }






    return render(request,  'result.html', data)


