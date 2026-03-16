from django.shortcuts import render
from django.shortcuts import redirect
import random
import markdown2

from . import util

def index(request):
    query = request.GET.get("q")
    if query:
        entries = util.list_entries()
        for entry in entries:
            if(entry.lower() == query.lower()):
                return redirect("name" , title = entry)
        results = []
        for entry in entries:
            if(query.lower() in entry.lower()):
                results.append(entry)
        return render(request, "encyclopedia/search.html", {
                "entries": results
            })

    else:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
        })         

def name(request, title):
    match = None
    entries = util.list_entries()
    for entry in entries:
        if(title.lower() == entry.lower()):
            match = entry
            break
    if match is None:
        return render(request, "encyclopedia/title.html", {
            "entry": None,
            "title": title
        })
    entry_text = markdown2.markdown(util.get_entry(match))

    return render(request, "encyclopedia/title.html", {
        "entry": entry_text,
        "title": title
    })

def create(request):
    return render(request, "encyclopedia/create.html")

def new_entry(request):
    if(request.method == "POST"):
        entry_title = request.POST.get("title")
        content = request.POST.get("markdown_text")
        entries = util.list_entries()
        for entry in entries:
            if(entry.lower() == entry_title.lower()):
                return render(request, "encyclopedia/new_entry.html", {
                    "error" : "Entry already exists"
                })
        util.save_entry(entry_title, content)
        return redirect("name", title = entry_title)
    return redirect("index")
def edit(request, title):
    entry = util.get_entry(title)
    return render(request, "encyclopedia/edit.html",{
        "entry": entry,
        "title": title
    })

def edited(request):
    if(request.method == "POST"):
        entry_title = request.POST.get("entry_title")
        content = request.POST.get("edited_text")
        util.save_entry(entry_title, content)
    return redirect("name", title = entry_title)


def random_page(request):
    text = random.choice(util.list_entries())
    return redirect("name", title = text)