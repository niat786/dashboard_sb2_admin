from django.shortcuts import render

def test(request):
    return render(request, 'dashboard/pages/add-new-product.html')

def dashboard(request):
    return render(request, 'dashboard/layouts/dashboard.html')
