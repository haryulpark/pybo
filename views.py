from audioop import reverse
import imp
from re import template
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.http.response import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# 화면 표시를 담당하는 함수, 클래스 
# 목록 표시함수
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output =",".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # 템플릿을 읽어서 모델을 바인딩 시켜서 결과 html 생성
    return render(request, 'polls/index.html',{
        "latest_question_list": latest_question_list
    })
def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',{"question": question})
# 질문 상세 내용표시
# 투표 폼 
def detail(request, question_id):

    # return HttpResponse("%s번 질문을 출력합니다."% question_id)
    # 질문 데이터
    try : question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("없는 질문입니다.")
        
    return render(request, 'polls/detail.html', {'question':question})
# 투표 결과 표시 함수
# def result(request, question_id):
#     return HttpResponse("%s번 질문에 응답하였습니다."%question_id)

#투표함수
def vote(request, question_id):
    # return HttpResponse("%s번 질문에 투표하였습니다."% question_id)
    question = get_object_or_404(Question, pk=question_id)
    # 투표 기능
    # request.GET -> GET 방식의 파라미터를 전달 받을 수 있고
    # request.POST -> POST 방식의 파라미터를 전달 받을 수 있다.
    
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 다시 투표 폼을 표시
        return render(request, 'polls/detail.html',{
            "question" : question,
            "error_message" : "투표하지 않았습니다.",
        })



    else: #예외가 없을 때
        # 투표 수 증가
        selected_choice.votes += 1
        # 업데이트
        selected_choice.save()
        # 결과 페이지로 이동
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))
        # reverse : urls.py에 설정할 url의 name, view의 name을 통해서 url을 찾아내는 방법

