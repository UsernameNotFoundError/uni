from django.shortcuts import render
from django.http import HttpResponse
from updateapp.DataBaseGenerator import SuperUpdate

def first_page(request):
    """
    first page
    """
    return render(request, "updateapp/progress_page.html")

def home_page(request):
    """
    other page
    """
    print("test")
    if request.method == 'POST':
        print("HERE =>>>>>", request.POST)
        print("\nwow =>>>>>", request.FILES)
        print("plop: >>", request.FILES['files_list'])
        mm = request.FILES['files_list']
        my_files = []
        # Problem here
        for f in request.FILES.getlist('files_list'):
            my_files += f
        print("checkpoint:", my_files)
        
    return render(request, "updateapp/home_page.html")


def celary_test_page(request):
    if request.user.is_superuser:
        HttpResponse("Work in progress!")
        Tt = SuperUpdate()
    else: 
        return HttpResponse("Unauthorised access !")
    
    return HttpResponse("This is a celary testing page please take a look at the terminal!")


