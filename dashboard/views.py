from django.shortcuts import render, redirect

from dashboard.models import Dashboard
from forms import DashboardForm
from members.models import Member


def create_dashboard(request):
    print('230: ' + str(request.POST.get('first_class')))
    print('330: ' + str(request.POST.get('second_class')))
    print('430: ' + str(request.POST.get('third_class')))
    print('530: ' + str(request.POST.get('fourth_class')))
    print('630: ' + str(request.POST.get('fifth_class')))
    if request.method == 'POST':
        form = DashboardForm(request.POST or None)

        if form.is_valid():
            dashboard = form.save()
            return render(request, 'dashboard.html', {'dashboard': dashboard})

    # GET이라면 입력값을 받을 수 있는 html을 가져다 줘야함
    else:
        form = DashboardForm()

    return render(request, 'create_dashboard_form.html', {'form': form})


# Create your views here.
def get_dashboard(request):
    dashboard = Dashboard.objects.reverse().first()
    first_class_members = Member.objects.all().filter(mem_level=dashboard.first_class)
    second_class_members = Member.objects.all().filter(mem_level=dashboard.second_class)
    third_class_members = Member.objects.all().filter(mem_level=dashboard.third_class)
    fourth_class_members = Member.objects.all().filter(mem_level=dashboard.fourth_class)
    fifth_class_members = Member.objects.all().filter(mem_level=dashboard.fifth_class)

    if request.method == 'GET':

        context = {
            'dashboard': dashboard,
            'first_class_members': first_class_members,
            'second_class_members': second_class_members,
            'third_class_members': third_class_members,
            'fourth_class_members': fourth_class_members,
            'fifth_class_members': fifth_class_members,
        }

        return render(request, "dashboard.html", context)

    return redirect('lottery:index')