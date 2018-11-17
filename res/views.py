from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import re

def registrationPage(request):
	return render(request, 'res/registration.html')

def logPage(request):
	return render(request, 'res/vhod.html')

def registrationQuery(request):
	username = request.POST['username']
	password = request.POST['pass']
	email=request.POST['email']
	u = User.objects.create_user(username, email, password)
	u.save()
	return HttpResponseRedirect(reverse('res:logPage'))

def loginin(request):
	username = request.POST['username']
	password = request.POST['pass']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('res:index'))
	else:
		return HttpResponseRedirect(reverse('res:logPage'))

def index(request):
	if request.user.is_authenticated:
		return firstpage(request)
	else:
		return logPage(request)

def firstpage(request):
	return render(request, 'res/firstpage.html', {'categorie_list': Categorie.objects.filter(user=request.user), 'rss_list': RssList.objects.filter(user=request.user)})

def add_rss(request):

	categorie = Categorie.objects.get(pk=request.POST['categorie'])
	t = RssList(title=request.POST['title'], address=request.POST['address'])
	t.categorie = categorie
	t.user = request.user
	t.save()

	return HttpResponseRedirect(reverse('res:firstpage'))

def add_categorie(request):
	c=Categorie(title=request.POST['title'])
	c.user = request.user
	c.save()

	return HttpResponseRedirect(reverse('res:firstpage'))

def logoutQuery(request):
	logout(request)
	return HttpResponseRedirect(reverse('res:logPage'))

def deletee(request, rss_id):
	RssList.objects.get(pk=rss_id).delete()
	return HttpResponseRedirect(reverse('res:firstpage'))

def rssPage(request, rssId):

	r = RssList.objects.filter(user=request.user).get(pk=rssId)

	context = {
		'item_list': getRssItems(r.address)[:25],
		'rssId': r.id
	}

	return render(request, 'res/rsspage.html', context)

def getRssItems(address):
	data = requests.get(address).content.decode("utf-8")
	root = ET.fromstring(data)

	ls = []
	for item in root.findall("./channel/item"):
		ch = item.getchildren()
		o = {}
		o["title"] = item.find("title").text
		o["link"] = item.find("link").text
		o["pubDate"] = datetime.strptime((item.find("pubDate").text)[:-6], '%a, %d %b %Y %H:%M:%S').strftime("%B %d, %Y")
		o["description"] = item.find("description").text
		ls.append(o)

	return ls

def add_rss(request):

	categorie = Categorie.objects.get(pk=request.POST['categorie'])
	t = RssList(title=request.POST['title'], address=request.POST['address'])
	t.categorie = categorie
	t.user = request.user
	t.save()

	return HttpResponseRedirect(reverse('res:firstpage'))

def search(request):
	pettern=request.POST['search_title']
	categorie_list1=Categorie.objects.filter(user=request.user)
	rss_list1=RssList.objects.filter(user=request.user)
	rss_list2=[]
	for rss in rss_list1:
		if re.search(pettern,str(rss)):
			rss_list2.append(rss)
	return render(request, 'res/firstpage.html', {'categorie_list': categorie_list1, 'rss_list': rss_list2})

def search2(request, rssId):
	r = RssList.objects.filter(user=request.user).get(pk=rssId)
	item_list=getRssItems(r.address)[:25]
	print(item_list)
	pettern=request.POST['search_title']
	item_list2=[]
	for item in item_list:
		if re.search(pettern,str(item["title"])):
			item_list2.append(item)
	return render(request, 'res/rsspage.html', {'item_list': item_list2, 'rssId': r.id})