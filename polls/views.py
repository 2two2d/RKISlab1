from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .models import Question, Choice, User
from django.template import loader
from django.urls import reverse
from django.views import generic
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
def register(request):
    if request.method == 'POST':
         form = UserRegistrationForm(request.POST)
         if form.is_valid():
             new_user = form.save(commit=False)
             new_user.set_password(form.cleaned_data['password'])
             new_user.avatar = form.cleaned_data['avatar']
             new_user.save()
             return render(request, 'usermanagment/register_done.html', {'new_user':new_user})
    else:
         form = UserRegistrationForm()

    return render(request, 'usermanagment/register.html', {'form':form})



def login(request):

    if request.method == 'POST':
        user = request.POST['name']

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'usermanagment/login.html'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


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
