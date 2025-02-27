from django.shortcuts import render, redirect, resolve_url

from dashboard.models import Dashboard
from forms import DashboardForm
from members.models import Member


def create_dashboard(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST or None)

        if form.is_valid():
            dashboard = form.save()
            return render(request, 'dashboard.html', {'dashboard': dashboard})

    # GET이라면 입력값을 받을 수 있는 html을 가져다 줘야함
    else:
        form = DashboardForm()

    return render(request, 'create_dashboard.html', {'form': form})


# Create your views here.
def get_dashboard(request, class_time, class_level):
    dashboard = Dashboard.objects.reverse().first()
    class_members = Member.objects.filter(mem_time=class_time, mem_level=class_level)

    for member in class_members:
        total_points = member.total_points
        stamps = int(total_points / 5)
        chances = int(stamps / 30)
        remaining_stamps = stamps - chances * 30

        member.total_points = total_points
        member.stamps = stamps
        member.chances = chances
        member.remaining_stamps = remaining_stamps

        member.save()


    if request.method == 'GET':

        context = {
            'dashboard': dashboard,
            'class_time': class_time,
            'class_level': class_level,
            'class_members': class_members,
        }
        return render(request, "dashboard.html", context)

    return redirect('lottery:index')