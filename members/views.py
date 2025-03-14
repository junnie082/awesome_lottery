from enum import member

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from dashboard.models import Dashboard
from forms import MemForm
from lottery.functions.sum_points import sum_points
from lottery.models import Point
from members.models import Member, Level


# Create your views here.
def index(request):
    member_list = Member.objects.order_by("-name")
    context = {
        "member_list": member_list,
    }
    return render(request, "index.html", context)

def get_create_member_form(request, class_time, class_level):
    if request.method == "GET":
        context = {
            'class_time': class_time,
            'class_level': class_level,
        }
        return render(request, "create_member_form.html", context)


def create_member(request, class_time, class_level):
    # POST라면 입력한 내용을 form을 이용하여 데이터베이스에 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = MemForm(request.POST, request.FILES)

        # 유효성 검사
        if form.is_valid():
            member = form.save(commit=False)
            member.mem_time = class_time
            member.mem_level = class_level
            member.lottos = ''

            point = request.POST.get('total_points')

            if point is None or point == '':
                point = 0

            point = int(point)

            member.total_points = point
            member.save()

            if point != 0:
                obj_point = Point.objects.create(member=member, points=point)
                obj_point.save()

            level = str(member.mem_time) + str(member.mem_level)

            obj_level = Level.objects.create(member=member, level=level)
            obj_level.save()

            return redirect('dashboard:get_dashboard', class_time=class_time, class_level=class_level)

    # GET이라면 입력값을 받을 수 있는 html을 가져다 줘야함
    else:
        form = MemForm()

    return redirect(reverse('members:get_create_member_form', kwargs={'class_time': class_time, 'class_level': class_level}))


def detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    page = request.GET.get('page', '1')  # 페이지
    point_list = Point.objects.order_by('-date').filter(member=member)

    for point in point_list:
        point.points = int(point.points)

    paginator = Paginator(point_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    total_points = member.total_points
    stamps = int(total_points / 5)
    chances = int(stamps / 30)
    remaining_stamps = stamps - chances * 30

    member.stamps = stamps
    member.chances = chances
    member.remaining_stamps = remaining_stamps

    member.save()

    dashboard = Dashboard.objects.reverse().first()

    context = {
        "total_points": total_points,
        "stamps": stamps,
        "chances": chances,
        "remaining_stamps": remaining_stamps,
        "member": member,
        "point_list": page_obj,
        "dashboard": dashboard,
    }

    return render(request, "detail.html", context)

def delete_member(request, member_id):

    if request.method == 'POST':
        member = get_object_or_404(Member, pk=member_id)
        class_time = member.mem_time
        class_level = member.mem_level

        member.delete()

        return redirect('dashboard:get_dashboard', class_time=class_time, class_level=class_level)

