from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'requests/submit_request.html', {'form': form})

@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'requests/request_list.html', {'requests': requests})

@login_required
def request_detail(request, pk):
    service_request = ServiceRequest.objects.get(pk=pk, user=request.user)
    return render(request, 'requests/request_detail.html', {'request': service_request})