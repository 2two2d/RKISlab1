from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, User
from django.template import loader
from django.urls import reverse
from django.views import generic
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.set_password(form.cleaned_data['password'])
#             new_user.avatar = form.cleaned_data['avatar']
#             new_user.save()
#             return render(request, 'registration/register_done.html', {'new_user':new_user})
#     else:
#         form = UserRegistrationForm()
#
#     return render(request, 'registration/register.html', {'form':form})

class register(generic.CreateView):
    model = User
    template_name = 'registration/register.html'
    fields = ()
    form = UserRegistrationForm()
    success_url = reverse_lazy('index')

    def form_valid(self):
        form = UserRegistrationForm()
        fields = form.save(commit=True)
        fields.save()
        return super().form_valid(form)


def logged_out(request):
    return render(request, 'registration/logged_out.html')

def login(request):
    return render(request, 'registration/login.html')


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

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
