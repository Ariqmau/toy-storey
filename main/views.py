from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Toy Storey',
        'name': 'Ariq Maulana Malik Ibrahim',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)