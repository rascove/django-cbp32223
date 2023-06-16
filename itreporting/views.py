from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import ContactForm
from .models import Issue
import requests

# Create your views here.
def home(request):
	url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}'
	api_key = 'c3585aab49fd664d43ac3cda44ca1170'
	cities = [('Sheffield', 'UK'), ('Melaka', 'Malaysia'), ('Bandung', 'Indonesia')]
	weather_data = []

	for city in cities:
		city_weather = requests.get(url.format(city[0], city[1], api_key)).json() # Request the API data and convert the JSON to Python data types, replace X, Y, and Z with actual city name, country code, and API key
		weather = {
			'city': city_weather['name'] + ', ' + city_weather['sys']['country'],
			'temperature': city_weather['main']['temp'],
			'description': city_weather['weather'][0]['description'],
		}

		weather_data.append(weather) # Add the data for the current city into our list

	return render(request, 'itreporting/home.html', {'title': 'Homepage', 'weather_data': weather_data})

def about(request):
	return render(request, 'itreporting/about.html', {'title': 'About Us'})

def report(request):
	daily_report = {'issues': Issue.objects.all(), 'title': 'Issues Reported'}
	return render(request, 'itreporting/report.html', daily_report)

class ContactFormView(FormView):
	template_name = 'itreporting/contact.html'
	form_class = ContactForm
	
	def get_context_data(self, **kwargs):
		context = super(ContactFormView, self).get_context_data(**kwargs)
		context.update({'title': 'Contact Us'})
		return context
	
	def form_valid(self, form):
		form.send_mail()
		messages.success(self.request, 'Successfully sent the enquiry')
		return super().form_valid(form)

	def form_invalid(self, form):
		messages.warning(self.request, 'Unable to send the enquiry')
		return super().form_invalid(form)
	
	def get_success_url(self):
		return self.request.path

class PostListView(ListView):
	model = Issue
	template_name = 'itreporting/report.html'
	context_object_name = 'issues'
	ordering = ['-date_submitted']
	paginate_by = 5

class PostDetailView(DetailView):
	model = Issue

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Issue
	fields = ['type', 'room', 'urgent', 'details']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Issue
	fields = ['type', 'room', 'details']

	def test_func(self):
		issue = self.get_object()
		return self.request.user == issue.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Issue
	success_url = '/report'

	def test_func(self):
		issue = self.get_object()
		return self.request.user == issue.author
	
class UserPostListView(ListView):
	model = Issue
	template_name = 'itreporting/user_issues.html'
	context_object_name = 'issues'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username = self.kwargs.get('username'))
		return Issue.objects.filter(author = user).order_by('-date_submitted')