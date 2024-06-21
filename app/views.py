from django.shortcuts import render

# Create your views here.
def change_base_address(request):
    return render(request,'baseaddress.html')
