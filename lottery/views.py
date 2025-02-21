from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from dashboard.models import Dashboard
from lottery.functions.sum_points import sum_points
from lottery.models import Point
from members.models import Member, Level


def index(request):
    member_list = Member.objects.order_by("-name")
    dashboard = Dashboard.objects.reverse().first()
    context = {
        "member_list": member_list,
        "dashboard": dashboard,
    }
    return render(request, "index.html", context)

def create_point(request, member_id):
    if request.method == 'POST':
        member = get_object_or_404(Member, id=member_id)
        new_point = Point.objects.create(member=member)
        new_point.date = datetime.now()

        is_dashboard = True


        if request.POST.get('pt_point_five'): new_point.points = 0.5
        if request.POST.get('pt_one'): new_point.points = 1
        if request.POST.get('pt_two'): new_point.points = 2
        if request.POST.get('pt_three'): new_point.points = 3
        if request.POST.get('pt_four'): new_point.points = 4
        if request.POST.get('pt_five'): new_point.points = 5
        if request.POST.get('pt_ten'): new_point.points = 10

        if request.POST.get('pt_minus_point_five'): new_point.points = -0.5
        if request.POST.get('pt_minus_one'): new_point.points = -1
        if request.POST.get('pt_minus_two'): new_point.points = -2
        if request.POST.get('pt_minus_three'): new_point.points = -3
        if request.POST.get('pt_minus_four'): new_point.points = -4
        if request.POST.get('pt_minus_five'): new_point.points = -5
        if request.POST.get('pt_minus_ten'): new_point.points = -10

        if request.POST.get('addPoints'):
            new_point.points = 0
            is_dashboard = False

        new_point.save()

        member.total_points = sum_points(member_id)
        member.save()


        print('new_point.points: ', new_point.points)
        print(member.total_points)

        if is_dashboard:
            return redirect('dashboard:get_dashboard')

    return redirect(reverse('members:detail', kwargs={'member_id': member_id}))


def delete_point(request, point_id):
    point = get_object_or_404(Point, id=point_id)
    member = point.member
    if request.method == 'POST':
        point.delete()

    member.total_points = sum_points(member.id)
    member.save()
    print('total_points', member.total_points)

    return redirect(reverse('members:detail', kwargs={'member_id': member.id}))