from django.contrib import auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from courses.forms import CourseForm

def create_course(request):
	"""
	form for creating a new course
	"""
	if request.method == 'POST':
		data = {'title': request.POST['title'],
				 'dept': request.POST['dept'],
				 'courseID': request.POST['courseID'],
				 'course_unique': request.POST['course_unique']}

		course_form = CourseForm(data)
		if len(Course.objects.filter(title=course_form.cleaned_data['title'])) != 0:
			clean_form = CourseForm()

			errors = ['Error: Already have a class called that']
		return render_to_response('Course/create_course.html', RequestContext(request))

	else:
		# clean_form = 
		errors = []

		return render_to_response('Course/create_course.html', RequestContext(request))

def show_student_dashboard(request):
	"""
	show the dashboard with an overview of courses the user is in
	"""

	return render_to_response('Course/student_dashboard.html', RequestContext(request))