from django.shortcuts import redirect, render
from firstapp.models import StoriesStory
from datetime import date
from django.core.paginator import Paginator
from . forms import ContactForm, StoriesStoryForm
from django.core.mail import EmailMessage
#Create your views here.
     
def index(request):
    data = StoriesStory.objects.all()
    top = StoriesStory.objects.all()[:4]
    Young = StoriesStory.objects.filter(category=1)
    new = StoriesStory.objects.all()[:4]
    OlderChildren = StoriesStory.objects.filter(category=2)
    paginator = Paginator(data, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'firstapp/index.html', {
        'data': data,
        'top': top,
        'Young': Young,
        'OlderChildren': OlderChildren,
        'new': new,
        'page_obj': page_obj
    })

def Ngay_thang_nam(request):
    today = date.today()
    return render(request, 'firstapp/masterbase.html', {'today': today})

def contact(request):
    forms = ContactForm()
    data = StoriesStory.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form['subject'].value()
            message = form['message'].value()
            notifier = f'Name:\t{form["name"].value()}\nmessage:\t{form["message"].value()}\nemail:\t{form["email"].value()}'
            form.save()
            email = EmailMessage(subject,notifier, to=['huynhhonda57@gmail.com'])
            email.send()
            return redirect('contact_ok')
        else:
            form = ContactForm()
        context = {
            "form":forms,
        }
    return render(request, 'firstapp/Contact_us.html', {'form':forms})

def contact_ok(request):
        return render(request, 'firstapp/contact_ok.html')

def Blog(request):
    contact_list = StoriesStory.objects.all().filter(category=1)
    paginator = Paginator(contact_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'firstapp/blog.html', {'page_obj': page_obj, 'contact_list':contact_list})

def Blogdetails(request, id):
    data = StoriesStory.objects.get(id=id)
    data2 = StoriesStory.objects.all()
    return render(request, 'firstapp/single.html', {'data': data, 'data2': data2})

def Acticle(request):
    contact_list = StoriesStory.objects.all().filter(category=2)
    paginator = Paginator(contact_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'firstapp/acticle.html', {'page_obj': page_obj, 'contact_list':contact_list})

def quanTriduLieu(request):
    quantridulieu = StoriesStory.objects.all()
    return render(request, 'firstapp/quantridulieu.html', {'quantridulieu': quantridulieu})

def addStoriesStory(request):
    forms = StoriesStoryForm()
    if request.method == 'POST':
        form = StoriesStoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('quanTriduLieu')
    else:
        form = StoriesStoryForm()
    context = {
        "form":forms
    }
    return render(request, 'firstapp/addStoriesStory.html', context)

def editStoriesStory(request, pk):
    storiesstory = StoriesStory.objects.get(id=pk)
    forms = StoriesStoryForm(instance=storiesstory)
    if request.method == 'POST':
        form = StoriesStoryForm(request.POST, request.FILES, instance=storiesstory)
        if form.is_valid():
            form.save()
            return redirect('quanTriduLieu')
    else:
        form = StoriesStoryForm()
    context = {
        "form":forms
    }
    return render(request, 'firstapp/editStoriesStory.html', context)

def deleteStoriesStory(request, pk):
    storiesstory = StoriesStory.objects.get(id=pk)
    storiesstory.delete()
    return redirect("quanTriduLieu")

# def deleteStoriesStory(request, pk):
#     storiesstory = StoriesStory.objects.get(id=pk)
#     if request.method == "POST":
#         storiesstory.delete()
#         return redirect('quanTriduLieu')
#     return render(request, 'firstapp/deleteStoriesStory.html', {'storiesstory':storiesstory})





