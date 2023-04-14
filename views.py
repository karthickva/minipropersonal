from django.shortcuts import render
from personal_app.models import Personal_information


# Create your views here.
def Personal_info(request):
   Personal_data=Personal_information.objects.all()
   per_data={"Perdata":Personal_data}
   return render(request,'personal_app/hi.html',context=per_data)
