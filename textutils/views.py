# I have created this file - Gaurav
# I am following codewithharry tutorial

from django.http import HttpResponse
from django.shortcuts import render
from .models import team

def index(request):
    return HttpResponse("<h2>Hello people! This is my first django app</h2>")

def about(request):
    return HttpResponse('''
                        <h1>about me!</h1>
                        <a href="#" onclick="history.go(-1)">Go Back</a>
                        ''')

def read_file(request):
    f = open('textutils/one.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")

def fav(request):
    return HttpResponse('''
    <h1>These are my top 5 favourite sites: </h1>
    <a href="https://www.google.com" target="blank">Google</a><br>
    <a href="https://chat.openai.com/" target="blank">ChatGPT</a><br>
    <a href="https://www.porkbun.com" target="blank">Porkbun</a><br>
    <a href="https://www.zomato.com" target="blank">Zomato</a><br>
    <a href="https://www.zwift.com" target="blank">Zwift</a><br>
''')

def mydatarequests(request):
    list_teams = team.objects.filter(team_level__exact="U09")
    context = {'youngest_teams': list_teams}
    return render(request, 'index.html', context)