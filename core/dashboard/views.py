from django.shortcuts import render
from django.shortcuts import render
from django.contrib import messages

from .graphs.graphs import *


# Create your views here.




# Create your views here.
def homepage(request):
	if request.method == "GET":

		
		context={'plot1':player_salaries(),
				 'plot2':team_wins(),	
				 'plot3':team_wins_over()

				 					}
		return render(request, 'website/homepage.html', context)

	else:

		context={}
		return render(request, 'website/homepage.html', context)


def dashboard(request):
	if request.method == "GET":

		
		context={}
		return render(request, 'website/index.html', context)

	else:

		context={}
		return render(request, 'website/index.html', context)