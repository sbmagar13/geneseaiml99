from django.shortcuts import render, redirect

from handset.forms import *
from handset.models import Handset
from django.contrib import messages
from django.db.models import Q


def index(request):
    username = request.user
    return render(request, 'operatorhandset_status.html', {'username': username})


def handset_list(request):
    context = {'handset_list': Handset.objects.all(), 'form2': ApproverForm()}
    return render(request, "operatorhandset_status.html", context)


def handset_view(request, hid=0):
    form2 = ApproverForm()
    if request.method == "GET":
        if hid == 0:
            form = HandsetForm()
        else:
            handset1 = Handset.objects.get(pk=hid)
            form = HandsetForm(instance=handset1)
        return render(request, "handset_register.html", {'form': form, 'form2': form2})
    else:
        form2 = ApproverForm(request.POST)
        if form2.is_valid():
            approverkey = form2.cleaned_data.get("approver_key")
            if approverkey == 'sagar99' or 'geneseaiml':
                if hid == 0:
                    form = HandsetForm(request.POST)
                else:
                    handset1 = Handset.objects.get(pk=hid)
                    form = HandsetForm(request.POST, instance=handset1)
                if form.is_valid():
                    form.save()
                    messages.add_message(request, messages.SUCCESS, 'Saved Successfully!!')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Invalid Input Format!!')
                    return render(request, "handset_register.html", {'form': form, 'form2': form2})
                return redirect('/hslist')


def handset_delete(request, hid):
    sensor = Handset.objects.get(pk=hid)
    form = ApproverForm(request.POST)
    if form.is_valid():
        approverkey = form.cleaned_data.get("approver_key")
        fapprover_values = Handset.objects.values_list('FinalApprover', flat=True)
        if (approverkey in fapprover_values) or (approverkey == 'sagar99' or 'geneseaiml'):
            sensor.delete()
            messages.add_message(request, messages.SUCCESS, 'Deleted Successfully!!')
            return redirect('/hslist')
        else:
            messages.add_message(request, messages.SUCCESS, 'Invalid Approver Key!!')
            return redirect('/hslist')
    else:
        messages.add_message(request, messages.SUCCESS, 'Invalid Input Format!!')
        return redirect('/hslist')


def handsetsearch_view(request):
    form2 = ApproverForm()
    if request.method == 'GET':
        srch = request.GET.get('srh')
        if srch:
            match = Handset.objects.filter(
                Q(PhoneNo__iexact=srch) | Q(ManagerName__icontains=srch) | Q(
                    Department__iexact=srch))
            if match:
                messages.add_message(request, messages.SUCCESS, 'found some results!')
                return render(request, 'handset_search.html', {'match': match, 'form2': form2})
            else:
                messages.add_message(request, messages.SUCCESS, 'no result found!')
        else:
            messages.add_message(request, messages.SUCCESS, 'not valid input!')
            return redirect('/hslist')
    return redirect('/hslist')
