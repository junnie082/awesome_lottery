from datetime import datetime
import json

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from dashboard.models import Dashboard
from lottery.functions.sum_points import sum_points
from lottery.models import Point
from members.models import Member


def index(request):
    page = request.GET.get('page', 1)
    member_list = Member.objects.order_by("-name")

    for member in member_list:
        member.total_points = int(member.total_points)

    paginator = Paginator(member_list, 5)
    page_obj = paginator.get_page(page)
    dashboard = Dashboard.objects.reverse().first()

    context = {
        "member_list": page_obj,
        "dashboard": dashboard,
    }
    return render(request, "index.html", context)

def use_lotto(request, member_id, index):
    member = get_object_or_404(Member, pk=member_id)
    if len(member.lottos) == 1:
        lotto = ''
    else:
        lotto = member.lottos[:index] + member.lottos[index+1:]
    print('index ', index)
    print("popped lotto", lotto)
    member.lottos = lotto
    member.save()
    return redirect(reverse('members:detail', kwargs={'member_id': member_id}))

# Global counter (resets when the server restarts)
lotto = 1

def start_lottery(request, member_id):
    if request.method == "GET":
        member = get_object_or_404(Member, id=member_id)
        global lotto
        lotto = 1 if lotto == 5 else lotto + 1  # If i is 5, reset to 1, else increment
        # return JsonResponse({"i": i})
        context = {'lotto': lotto, 'member': member}
        return render(request, 'lottery.html', context)

def stop_lottery(request, member_id, lotto):
    member = Member.objects.get(pk=member_id)
    member.lottos = str(member.lottos) + str(lotto)
    member.total_points = member.total_points - 5 * 30
    member.chances = member.chances - 1
    member.stamps = member.stamps - 30
    member.save()

    print('member.lottos ', member.lottos)

    return render(request, 'lottery_result.html', {'lotto': lotto, 'member': member})

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

        member.total_points = member.total_points + new_point.points
        member.save()


        if is_dashboard:
            return redirect('{}#member_{}'.format(
                resolve_url('dashboard:get_dashboard', class_time=member.mem_time, class_level=member.mem_level),
                member_id
            ))

    return redirect(reverse('members:detail', kwargs={'member_id': member_id}))


def delete_point(request, point_id):
    if request.method == 'POST':
        point = get_object_or_404(Point, id=point_id)
        member = point.member
        point.delete()

        member.total_points = member.total_points - point.points
        member.save()