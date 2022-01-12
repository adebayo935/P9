from .forms import *
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from .models import Ticket,Review,UserFollows
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic

User = get_user_model()


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'listings/register.html'


def home(request):

    if request.method == 'POST':
        form = LoginForm()
        if User.objects.filter(login=request.POST['login'], password=request.POST['password']).exists():
            user = User.empAuth_objects.get(username=login)
            return render(request, 'listings/flux.html', {'form': form})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'listings/home.html', context)
    else:
        form = LoginForm()
    return render(request, 'listings/home.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
    else:
        form = CustomUserCreationForm()

    return render(request, 'listings/register.html', {'form':form})


def posts(request):
    reviews = list(Review.objects.filter(user=request.user))
    tickets = list(Ticket.objects.filter(user=request.user))
    total = reviews+tickets
    total.sort()

    paginator = Paginator(total,3)
    page_number =request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'listings/posts.html', {'total': page_obj})


def flux(request):

    following = list(UserFollows.objects.filter(user=request.user))
    reviews = list(Review.objects.all())
    tickets = list(Ticket.objects.all())
    total = reviews+tickets
    total.sort()
    total_user = user_tkt + user_rev
    total_user.sort()
    flux = []
    if following :
        for entry in total:
            for line in following :
                if entry.user == line.followed_user:
                    flux.append(entry)

    paginator = Paginator(flux,3)
    page_number =request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'listings/flux.html', {'total': page_obj})


def subs(request):
    users = UserFollows.objects.all()
    if request.method == "POST":
        form = UsersForm(request.POST, instance=User())
        follows = UserFollows(
            user = request.user,
            followed_user = User.objects.get(id=request.POST['Selection']),
            )
        follows.save()
        return render(request, 'listings/subs.html',{'form': form, 'users': users})
    else:
        form = UsersForm()
        return render(request, 'listings/subs.html', {'form': form, 'users': users})


def make_rev(request):
    if request.method == "POST":
        form_ticket = AskRevForm(request.POST, request.FILES)
        form_rev = MakeRevForm(request.POST, instance=Ticket())
        if form_ticket.is_valid() and form_rev.is_valid():
            ticket = Ticket(
                title=request.POST.get('Titre'),
                description=request.POST.get('Description'),
                user=request.user,
                image=request.FILES.get('image')
            )
            ticket.save()
            review = Review(
                ticket = ticket,
                headline = request.POST.get('Sujet'),
                body = request.POST.get('Commentaire'),
                rating = request.POST.get('Note'),
                user=request.user
            )
            review.save()
        return redirect('posts')
    else:
        form_ticket = AskRevForm()
        form_rev = MakeRevForm()
    return render(request, 'listings/make_rev.html',{'form_ticket':form_ticket,'form_rev':form_rev})


def ask_rev(request):

    if request.method == "POST":
        form = AskRevForm(request.POST, request.FILES)
        titre = request.POST.get('Titre')
        description = request.POST.get('Description')
        image = request.FILES.get('image')
        ticket = Ticket(
            title = titre,
            description = description,
            user = request.user,
            image = image
        )
        ticket.save()
        return redirect('posts')

    else:
        form = AskRevForm()
    return render(request, 'listings/ask_rev.html',{'form':form})


def answer_rev(request, id):
    if request.method == "POST":
        ticket = Ticket.objects.get(id=id)
        form_rev = MakeRevForm(request.POST, instance=Ticket())
        if form_rev.is_valid():
            review = Review(
                ticket = ticket,
                headline = request.POST.get('Sujet'),
                body = request.POST.get('Commentaire'),
                rating = request.POST.get('Note'),
                user=request.user
            )
            review.save()
        return redirect('flux')
    else:
        ticket = Ticket.objects.get(id=id)
        form_rev = MakeRevForm()
    return render(request, 'listings/answer_rev.html',{'ticket':ticket,'form_rev':form_rev})


def update_rev(request, id):
    review = Review.objects.get(id=id)
    ticket = Ticket.objects.get(id=review.ticket.id)
    if request.method == "POST":
        form_rev = MakeRevForm(request.POST, instance=review)
        if form_rev.is_valid():
            clean = form_rev.cleaned_data
            print(request.user)
            review.headline = clean['Sujet']
            review.body = clean['Commentaire']
            review.rating = clean['Note']
            review.save()
        return redirect('posts')
    else:
        form_rev = MakeRevForm(instance=review)

    return render(request, 'listings/update_rev.html',{'ticket':ticket,'form_rev':form_rev})


def update_tkt(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == "POST":
        form_tkt = AskRevForm(request.POST, request.FILES, instance=ticket)
        if form_tkt.is_valid():
            clean = form_tkt.cleaned_data
            print(request.user)
            ticket.title = clean['Titre']
            ticket.description = clean['Description']
            ticket.image = clean['image']
            ticket.save()
        return redirect('posts')
    else:
        form_tkt = AskRevForm(instance=ticket)

    return render(request, 'listings/update_tkt.html',{'form_tkt':form_tkt})


def delete_tkt(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == "POST":
        ticket.delete()
        return redirect('posts')

    return render(request, 'listings/delete_tkt.html',{'ticket':ticket})


def delete_rev(request, id):
    review = Review.objects.get(id=id)
    if request.method == "POST":
        review.delete()
        return redirect('posts')

    return render(request, 'listings/delete_rev.html',{'review':review})


def delete_follow(request, id):
    user = UserFollows.objects.get(user=request.user,followed_user=id)
    if request.method == "POST":
        user.delete()
        return redirect('subs')

    return render(request, 'listings/delete_follow.html',{'d_user':user})