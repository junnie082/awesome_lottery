from django.shortcuts import render

from .api.api_call import call_api
from .models import SpeakingBook


def generate_progress(request):
    num_progress = SpeakingBook.objects.all().count()

    if (num_progress != 0):
        progresses = SpeakingBook.objects.all()
        for progress in progresses:
            progress.delete()

    tables = call_api()

    for progress in tables:
        speaking_progress = SpeakingBook.objects.create(dailyProgress=progress)

    context = {
        'tables': tables,
    }
    return render(request, 'speaking_list.html', context)

# Create your views here.
def get_SpeakingC(request):
    speaking_progress = SpeakingBook.objects.all()
    tables = []
    for progress in speaking_progress:
        print('progress', progress.dailyProgress)
        tables.append(progress.dailyProgress)
    print('tables', tables)
    context = {
        'tables': tables,
    }
    return render(request, 'speaking_list.html', context)