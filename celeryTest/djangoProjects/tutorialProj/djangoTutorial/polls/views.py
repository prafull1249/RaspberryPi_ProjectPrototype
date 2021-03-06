from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Question,Choice
from django.template import loader
from django.shortcuts import get_object_or_404, render

def index(request):
    latest_questions = Question.objects.order_by('pub_date')[:5]
    output = ', '.join(q.question_text for q in latest_questions)
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_questions,}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

#def results(request, question_id):`
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def getRequest(request, question_id):
        temp = request.POST['health']
        temp = request.POST['temp']
        return HttpResponse(reverse("Ok"))

