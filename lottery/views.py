from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.regex_helper import Choice

from forms import MemForm
from lottery.models import Member


def index(request):
    member_list = Member.objects.order_by("-name")
    context = {
        "member_list": member_list,
    }
    return render(request, "index.html", context)


def create_member_form(request):
    # POST라면 입력한 내용을 form을 이용하여 데이터베이스에 저장
    if request.method == 'POST' or request.method == 'FILES':
        group = request.POST.get('group_time_mode') + request.POST.get('group_level_mode')
        form = MemForm(request.POST, request.FILES)

        # 유효성 검사
        if form.is_valid():
            print("group test: " + form.cleaned_data['group'])

            # form.cleaned_data['group'] = group
            record = form.save(commit=False)
            record.group = group
            record.save()
            print("group: " + form.cleaned_data['group'])

            return redirect('lottery:index')

    # GET이라면 입력값을 받을 수 있는 html을 가져다 줘야함
    else:
        form = MemForm()

    return render(request, 'create_member_form.html', {'form': form})


def add_points(request, member_id):
    if request.method == 'POST':
        add_points = request.POST.get('addPoints')
        print(add_points)

    member = get_object_or_404(Member, id=member_id)

    prev_points = member.points
    new_points = prev_points + int(request.POST.get('addPoints'))

    member.points = new_points
    member.save()

    return redirect(reverse('lottery:index'))



def detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, "detail.html", {"member": member})


def results(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, "lottery/results.html", {"member": member})


def vote(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    try:
        selected_choice = member.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "lottery/detail.html",
            {
                "member": member,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(member.id,)))
