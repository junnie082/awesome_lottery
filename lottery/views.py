from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from dashboard.models import Dashboard
from lottery.functions.sum_points import sum_points
from lottery.models import Point
from members.models import Member


def index(request):
    page = request.GET.get('page', 1)
    member_list = Member.objects.order_by("-name")
    paginator = Paginator(member_list, 10)
    page_obj = paginator.get_page(page)
    dashboard = Dashboard.objects.reverse().first()

    context = {
        "member_list": page_obj,
        "dashboard": dashboard,
    }
    return render(request, "index.html", context)

def entire_mem_point(request, class_time, class_level):
    if request.method == "POST":
        print('entire_point', class_time, class_level)
        members = Member.objects.filter(mem_time=class_time, mem_level=class_level)
        point = 0
        print('enter_point')
        if request.POST.get('pt_point_five'): point = 0.5
        if request.POST.get('pt_one'): point = 1
        if request.POST.get('pt_two'): point = 2
        if request.POST.get('pt_three'): point = 3
        if request.POST.get('pt_four'): point = 4
        if request.POST.get('pt_five'): point = 5
        if request.POST.get('pt_six'): point = 6
        if request.POST.get('pt_seven'): point = 7
        if request.POST.get('pt_eight'): point = 8
        if request.POST.get('pt_nine'): point = 9
        if request.POST.get('pt_ten'): point = 10
        if request.POST.get('pt_minus_five'): point = -5
        if request.POST.get('pt_minus_ten'): point = -10

        for member in members:
            Point.objects.create(points=point, member=member)
            member.total_points = member.total_points + point
            member.save()

        return redirect(reverse('dashboard:get_dashboard', kwargs={'class_time': class_time, 'class_level': class_level}))


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
        if request.POST.get('pt_six'): new_point.points = 6
        if request.POST.get('pt_seven'): new_point.points = 7
        if request.POST.get('pt_eight'): new_point.points = 8
        if request.POST.get('pt_nine'): new_point.points = 9
        if request.POST.get('pt_ten'): new_point.points = 10

        if request.POST.get('pt_minus_five'): new_point.points = -5
        if request.POST.get('pt_minus_ten'): new_point.points = -10

        if request.POST.get('addPoints'):
            new_point.points = float(request.POST.get('addPoints'))
            is_dashboard = False

        new_point.save()

        member.total_points = sum_points(member_id)
        member.save()


        print('new_point.points: ', new_point.points)
        print(member.total_points)

        if is_dashboard:
            return redirect(reverse('dashboard:get_dashboard', kwargs={'class_time': member.mem_time, 'class_level': member.mem_level}))

    return redirect(reverse('members:detail', kwargs={'member_id': member_id}))


def delete_point(request, point_id):
    if request.method == 'POST':
        point = get_object_or_404(Point, id=point_id)
        member = point.member
        if request.method == 'POST':
            point.delete()

        member.total_points = sum_points(member.id)
        member.save()
        print('total_points', member.total_points)

    return redirect(reverse('members:detail', kwargs={'member_id': member.id}))