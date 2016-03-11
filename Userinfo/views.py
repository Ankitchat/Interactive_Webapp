from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .models import UserInfo, QuestionInfo, Poll
from .forms import Userform
from django.shortcuts import redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
import csv
from config.settings.common import ROOT_DIR

# Create your views here.


class UserInfodetail(FormView):
    form_class = Userform
    template_name = 'User/add.html'
    success_url = '/user/survey'

    def form_valid(self, form):
        form.save()
        return super(UserInfodetail, self).form_valid(form)


class DisplayQuestion(ListView):
    model = QuestionInfo
    template_name = 'User/ask.html'

    def get_context_data(self, **kwargs):
        context = super(DisplayQuestion, self).get_context_data(**kwargs)
        context['question'] = QuestionInfo.objects.all()
        context['choice'] = Poll.objects.all()
        return context

    @csrf_exempt
    def post(self, request):
        for every in QuestionInfo.objects.all():
            choice = request.POST.get(str(every.QId))
            poll = Poll.objects.get(answerto_id=every.QId, Choice=choice)
            poll.Score = poll.Score + 1
            poll.save()
        return render(request,
                      "User/Confirm.html",
                      {}
                      )


class CreateCsv(View):

    def get(self, request):
        user = []
        pollscore = []
        question = []
        userfile = open(
            str(ROOT_DIR)+"/Users.csv", 'w')
        Surveyfile = open(
            str(ROOT_DIR)+"/Survey.csv", 'w')
        for each in UserInfo.objects.all():
            user.append(each.UserId)
            user.append(each.FullName)
            user.append(each.Email)
            user.append(each.Zip)
            wr = csv.writer(userfile, quoting=csv.QUOTE_ALL)
            wr.writerow(user)
            user = []
        for each in QuestionInfo.objects.all():
            question.append(each.Question)
            wr = csv.writer(Surveyfile, quoting=csv.QUOTE_ALL)
            wr.writerow(question)
            for choice in Poll.objects.filter(answerto_id=each.QId):
                pollscore.append(choice.Choice)
                pollscore.append(choice.Score)
                wr = csv.writer(Surveyfile, quoting=csv.QUOTE_ALL)
                wr.writerow(pollscore)
                pollscore = []
            question = []
        return redirect('/user/add')
