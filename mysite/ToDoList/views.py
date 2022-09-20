from django.shortcuts import render
from .models import List

# Create your views here.
def index(request: object):
	items=List.objects.all()
	if request.method == "POST":
		if request.POST.get("save"):
			for item in items:
				if "clicked" == request.POST.get("c"+str(item.id)):
					item.completed = True
					item.save()
				else:
					item.completed = False
					item.save()
				if "text" + str(item.id) in request.POST:
					item.task = request.POST.get("text" + str(item.id))

		elif request.POST.get("add"):
			newItem = request.POST.get("new")
			if newItem != "":
				List(task=newItem).save()
			else:
				print("invalid")
		elif request.POST.get("delete"):
					items.delete()

	return render (request, "ToDoList/index.html", {"items":items})