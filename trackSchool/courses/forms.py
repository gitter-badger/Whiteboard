from django import forms
from django.contrib.auth.models import User

from courses.models import (
    Course, School, Section, CourseItem, StudentItem, AssignmentType, Student,
    BetaUser)


class BetaUserForm(forms.ModelForm):

    """docstring for BetaUserForm"""
    class Meta:
        model = BetaUser
        fields = ('edu_email', 'first_name', 'last_name', 'school')


class StudentForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password')
        widgets = {'password': forms.PasswordInput()}

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = True


class StudentSettingsForm(forms.ModelForm):
    school = forms.ModelChoiceField(queryset=School.objects.all())

    class Meta:
        model = Student
        fields = ('school', 'edu_email')


class CourseForm(forms.Form):

    """docstring for CourseForm"""
    model = Course
    title = forms.CharField(max_length=256)
    dept = forms.CharField(max_length=6)
    courseID = forms.CharField(max_length=16)
    credits = forms.IntegerField()

    class Meta:
        model = Course
        fields = ('title', 'dept', 'courseID', 'credits')


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {'password': forms.PasswordInput()}

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(max_length=100)
    class Meta:
        model=User
        fields=('email')       

class JoinSchoolForm(forms.Form):
    email = forms.EmailField(max_length=100)
    school = forms.ModelChoiceField(queryset=School.objects.all())


class CreateSectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ('year', 'term', 'professor', 'id_no', 'course')


class CourseItemForm(forms.Form):
    model = CourseItem

    name = forms.CharField(max_length=256)

    due_date = forms.DateField()

    due_time = forms.TimeField()

    point_value = forms.IntegerField()

    class Meta:
        model = Course
        fields = ('name', 'month', 'day', 'year', 'time', 'assignment_type')


class AssignmentTypeForm(forms.ModelForm):

    class Meta:
        model = AssignmentType
        fields = ('name', 'weight')


class StudentItemForm(forms.ModelForm):
    assignment_type = forms.ModelChoiceField(
        queryset=AssignmentType.objects.all())

    def __init__(self, *args, **kwargs):
        try:
            self.student = kwargs.pop('student')
            try:
                self.section = kwargs.pop('section')
            except KeyError:
                self.section = None
                pass
        except KeyError:
            pass

        super(StudentItemForm, self).__init__(*args, **kwargs)

        self.fields['assignment_type'].queryset = \
            AssignmentType.objects.filter(student=self.student,
                                          sectionInstance=self.section)

    score = forms.IntegerField()

    class Meta():
        model = StudentItem
        fields = ('score', 'state', 'description', 'assignment_type')
