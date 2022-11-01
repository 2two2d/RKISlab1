from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from .models import Question, Choice, User
from django.template import loader
from django.urls import reverse
from django.views import generic
from .forms import UserRegistrationForm, UserUpdateForm, add_qForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
def register(request):
    if request.method == 'POST':
         form = UserRegistrationForm(request.POST, request.FILES)
         if form.is_valid():
             new_user = form.save(commit=False)
             new_user.set_password(form.cleaned_data['password'])
             new_user.avatar = form.cleaned_data['avatar']
             new_user.save()
             return render(request, 'usermanagment/register_done.html', {'new_user':new_user})
    else:
         form = UserRegistrationForm()

    return render(request, 'usermanagment/register.html', {'form':form})

def update_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            if form.password_check == request.user.password:
                form.save()
                return render(request, 'usermanagment/register_done.html')
    else:
        form = UserUpdateForm(initial={'full_name': request.user.full_name, 'username': request.user.username, 'email': request.user.email})
    return render(request, 'usermanagment/user_update.html', {'form': form})


@login_required
def my_profile(request):
    current_user = request.user
    return render(request, 'usermanagment/my_profile.html', {'user':current_user})
@login_required
def UserDelete(request):
    request.user.delete()
    return render(request, 'usermanagment/user_deleted.html')

def all_q(request):
    questions = Question.objects.all()

    return render(request, 'polls/all_q.html', context={'questions':questions})

def my_q(request):
    questions = Question.objects.filter()

    return render(request, 'polls/my_q.html', context={'questions':questions})

def add_q(request):
    if request.method == 'POST':
        form = add_qForm(request.POST, request.FILES)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.author = request.user
            choice.img = form.cleaned_data['img']
            choice.save()
            return reverse_lazy('my_q')
    else:
        form = add_qForm()

    return render(request, 'polls/add_q.html', {'form':form})


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'вы не сделали выбор'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
