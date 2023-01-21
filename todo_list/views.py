import json
from django.http import JsonResponse, HttpResponseRedirect, HttpRequest, HttpResponse, request, response
from django.shortcuts import render
import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = conn.cursor()


# conn = sqlite3.connect('db.sqlite3')
# Create your views here.

def creat(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        date = request.POST.get("date")
        print(title, desc,date)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO todo_list_task( title, desc, date) VALUES  (?, ?, ?)''', [title, desc, date])
        conn.commit()
        return render(request, 'index.html')

def get_item(request, id):
    cursor.execute('''select * from todo_list_task  where id =  ?''', [id])
    result = cursor.fetchone()
    print(result)
    if len(result) == 0:
        return render (request, 'error.html', {'context': 'id__not_exist'})
    else:
        return render (request, 'data.html', {'context': result})
        




# def creat(request):
#     return render(request, '')
