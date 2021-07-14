from django.shortcuts import render
from django.http.response import StreamingHttpResponse,HttpResponse
from interview.video_capture import WebCam

from .models import *
# Create your views here.
from gtts import gTTS
import os
from django.contrib.auth.decorators import login_required
import json

from django.shortcuts import render
from json import dumps
from django.http import JsonResponse
from time import time
from django.views.generic import View

def success_interview(request):
	return render(request, 'interview/sucess.html')




@login_required(login_url='login')
def getQuestionAjaxHandler(request,*args, **kwargs):
	if request.method == 'GET':
		upper = kwargs.get('num_question') #get the number of question : 1 question 
		lower = upper - 1 #0 question
		questions = list(Question.objects.values())[lower:upper]
		questionId = Question.objects.all()
		q = []
		for i in questionId:
			q.append(i.id)
		questions_size = len(Question.objects.all())
		max_size = True if upper > questions_size else False
		return JsonResponse({'data':questions,'max_size':max_size, 'q_ids': q},status=200,safe=False)




@login_required(login_url='login')
def interview_is_finished(request):
	if request.method == 'POST':
		user = request.user
		if Interview.objects.filter(user=user).last():
			Interview.objects.filter(user=user).update(is_finished=True)
			
		else:
			pass


		#return HttpResponse('interview is finished!')
		return render(request, 'interview/success.html')
	else:
		return HttpResponse('ups!')

	

def createInterview(request):
	if request.method == 'POST':
		user = request.user
		profile_type = user.profile.account_type
		Interview.objects.create(user=user)
		question_list = Question.objects.all()
		for question in question_list:
			if question.user == user:
				interview = Interview.objects.filter(user=user).last()
				interview.question.add(question)

		return HttpResponse('interview created!')



@login_required(login_url='bot/login')
def index(request):
	speech()
	questions = Question.objects.all()
	all_files = []
	for i in questions:
		files = str(i.id)
		#files = (str("{% static 'images/")+str(i.id)+".mp3' %}")
		all_files.append(files)

	context={
		'questions': questions,
		
		'files':','.join([str(i) for i in all_files])
	}
	return render(request, 'interview/index.html', context)

def create(camera):
	while True:
		frame= camera.capture()
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n'+ frame+b'\r\n\r\n')


def record(request):
	return StreamingHttpResponse(create(WebCam()), content_type='multipart/x-mixed-replace; boundary=frame')


def speech():
	questions = Question.objects.all()
	for i in questions:
		file = str(i.id)+".mp3"
		tts = gTTS(text=i.question_text, lang='en')
		tts.save("static/images/"+file)
		duration = len(i.question_text.split()) 
		print("the question is: ")
		print("this is the duration of the file "+ str(duration))
		os.system("mpg321 good.mp3")
	"""
	for i in questions:
		tts = gTTS(text=b, lang='en')
		tts.save("static/images/voice.mp3")
		os.system("mpg321 good.mp3")	
		"""