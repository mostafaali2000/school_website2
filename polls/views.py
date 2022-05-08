from django.shortcuts import render
def index(request):
 return render(request, 'index.html')


def pageAnnouncement(request):
 return render(request,'Announcement.html')


def pageBus(request):
 return render(request,'bus.html')


def pageWhyUs(request):
 return render(request,'Why_us.html')