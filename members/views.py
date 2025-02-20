from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

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

def create_member(request):
    # POST라면 입력한 내용을 form을 이용하여 데이터베이스에 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = MemForm(request.POST, request.FILES)

        # 유효성 검사
        if form.is_valid():
            form.cleaned_data['total_points'] = request.POST.get('total_points')
            form.save()
            # form.cleaned_data['group'] = group
            # record = form.save(commit=False)
            # record.group = level
            # record.save()
            # print("group: " + form.cleaned_data['group'])

            return redirect('lottery:index')

    # GET이라면 입력값을 받을 수 있는 html을 가져다 줘야함
    else:
        form = MemForm()

    return render(request, 'create_member_form.html', {'form': form})


def detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    point_list = Point.objects.order_by('-date').filter(member=member)

    total_points = sum_points(member_id)
    num_chances = total_points / 30
    remaining_points = total_points % 30
    print("num_chans", num_chances)
    print("remaining_points", remaining_points)

    context = {
        "num_chances": num_chances,
        "remaining_points": remaining_points,
        "member": member,
        "point_list": point_list
    }

    return render(request, "detail.html", context)


def delete_member(request, member_id):

    if request.method == 'POST':
        member = get_object_or_404(Member, pk=member_id)
        member.delete()

    return redirect(reverse('members:index'))

