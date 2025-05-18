from django.shortcuts import render,redirect,get_object_or_404
from .models import moviet
from .forms import movie_form
from django.contrib import messages



# Create your views here.
def index(request):
    x=moviet.objects.all
    return render(request,'index.html',{'value':x})

def adminindex(request):
    x=moviet.objects.all
    return render(request,'adminindex.html',{'value':x})


def about(request):
    return render(request,'about.html')

def e_ticket(request):
    return render(request,'e-ticket.html')

def movies(request):
    return render(request,'movies.html')

def sign_in(request):
    return render(request,'sign_in.html')

def ticket_booking(request):
    return render(request,'ticket-booking.html')



# ///////////////////////admin////////////////////////////




def adminadd(request):
    if request.method == "POST":
        x = request.POST.get("movie_name")
        y = request.POST.get("movie_year")
        z = request.POST.get("movie_duration")
        s = request.POST.get("movie_description")
        p = request.FILES.get("movie_image")  # Use `.get()` to avoid errors

        if x and y and z and s and p:  # Ensure all fields are provided
            user = moviet(movie_name=x, movie_year=y, movie_duration=z, movie_description=s, movie_image=p)
            user.save()
            messages.success(request, "Movie added successfully!")  # Success message
            return redirect('adminadd')  # Redirect to clear form and show message

    return render(request, 'adminadd.html')

def adminpage(request):
    movies = moviet.objects.all()
    return render(request, 'adminpage.html', {'movies': movies})


def adminupdate(request, id):
    m = get_object_or_404(moviet, id=id)  # Safer way to get an object
    form = movie_form(request.POST or None, request.FILES or None, instance=m)

    if form.is_valid():
        form.save()
        return redirect('adminpage')  # ✅ No trailing slash

    return render(request, 'adminupdate.html', {'form': form, 'moviet': m})


def admindelete(request, id):
    if request.method == 'POST':
        p = get_object_or_404(moviet, id=id)
        p.delete()
        return redirect('adminpage')  # ✅ No trailing slash

    return render(request, 'admindelete.html')

def admindetail(request,moviet_id):
    movieee=moviet.objects.get(id=moviet_id)
    return render(request,'admindetail.html',{'valuesss':movieee})