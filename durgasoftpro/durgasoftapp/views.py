from django.shortcuts import render
from .models import FeedbackData
from .models import ServicesData
from .forms import FeedbackForm
from django.http.response import HttpResponse
import datetime
date1 = datetime.datetime.now()


# Create your views here.
def home_view(request):

    return render(request,'durgasoft_home.html')


def services_view(request):
    data=ServicesData.objects.all()

    return render(request,'durgasoft_services.html',{'data':data})

def contact_view(request):
    return render(request,'durgasoft_contact.html')

def gallery_view(request):
    return render(request,'durgasoft_gallery.html')

def feedback_view(request):
    if request.method == 'POST':
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')

            data = FeedbackData(
                name=name,
                rating=rating,
                date=date1,
                feedback=feedback,
            )
            data.save()
            fform=FeedbackForm()
            feedbacks = FeedbackData.objects.all()
            return render(request,'durgasoft_feedback.html',{'ffrom':fform,'feedbacks':feedbacks})
        else:
            return HttpResponse(' No data Available Right Now !')
    else:
        fform = FeedbackForm()
        feedbacks = FeedbackData.objects.all()
        return render(request,'durgasoft_feedback.html',{'fform':fform,'feedbacks':feedbacks})
