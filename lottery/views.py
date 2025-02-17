from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from forms import MemForm
from lottery.models import Point
from members.models import Member


def index(request):
    member_list = Member.objects.order_by("-name")
    context = {
        "member_list": member_list,
    }
    return render(request, "index.html", context)

def add_points(request, member_id):
    if request.method == 'POST':
        add_points = request.POST.get('addPoints')
        print(add_points)

    member = get_object_or_404(Member, id=member_id)
    points = Point.objects.filter(member_id=member_id)
    points.order_by('-date')

    new_point = Point.objects.create(member=member)
    new_point.points = points.first().points + int(add_points)
    new_point.date = datetime.now()
    new_point.save()

    member.total_points = sum_points(member_id)

    print('total_points', member.total_points)
    member.save()

    print(new_point.points)

    new_point.save()
    return redirect(reverse('lottery:index'))

def sum_points(member_id):
    member = Member.objects.get(id=member_id)
    points = Point.objects.filter(member=member)
    total_points = 0
    for point in points:
        total_points += point.points

    return total_points

def results(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, "lottery/results.html", {"member": member})

