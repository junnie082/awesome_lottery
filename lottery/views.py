from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from lottery.functions.sum_points import sum_points
from lottery.models import Point
from members.models import Member


def index(request):
    member_list = Member.objects.order_by("-name")
    context = {
        "member_list": member_list,
    }
    return render(request, "index.html", context)

def add_point(request, member_id):
    if request.method == 'POST':
        add_points = request.POST.get('addPoints')

        if not add_points:
            add_points = 0
            print('add_points: ' + str(add_points))

        member = get_object_or_404(Member, id=member_id)
        points = Point.objects.filter(member_id=member_id)
        points.order_by('-date')

        new_point = Point.objects.create(member=member)
        new_point.points = int(add_points)
        new_point.date = datetime.now()
        new_point.save()

        member.total_points = sum_points(member_id)

        print('total_points', member.total_points)
        member.save()

        print(new_point.points)

        new_point.save()
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