from django.shortcuts import render
import markdown2
from django.http import HttpResponseRedirect
import re
import random

from . import util


"""Route for homepage"""
def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})



"""Route for each entry"""
def entry(request, title):

    # Get markdown content of requested entry
    page = util.get_entry(title)

    # If entry wasn't found
    if page is None:
        return render(request, "encyclopedia/error.html")

    #  Decode to html
    else:
        page = markdown2.markdown(util.get_entry(title))


    # Render html file of the requested entry
    return render(request, "encyclopedia/entry.html", {"page": page, "title": title})



"""Route for getting a searched entry"""
def search(request):

    if request.method == "POST":

        # Get entry that was submitted
        search = request.POST
        # If search field was submitted empty
        if not search["q"]:
            return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})

        # Get list of all entries
        entries = util.list_entries()

        # If entry exists in list of available entries
        if search["q"] in entries:
            # Render the page for that entry
            return HttpResponseRedirect(f"/wiki/{search['q']}")

        # If entry was not in list of available entries
        else:
            # An empty list
            results = []

            for entry in entries:
                # If pattern matching an existing entry is found
                if entry.lower().find(search["q"].lower()) != -1:

                    # Add the existing entry to list
                    results.append(entry)

            return render(request, "encyclopedia/search_results.html", {"results": results})

    else:
        return render(request, "encyclopedia/error.html", {"message": "Request method not allowed"})


"""Route for creating a new entry"""
def create(request):

    # If request method is GET:
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")
    #  If request method is POST:
    else:

        # Get data that was sumbitted
        data = request.POST

        # Existing entries
        entries = util.list_entries()

        for entry in entries:
            # Check if page for new entry already exists
            if data["title"].lower() == entry.lower():

                return render(request, "encyclopedia/error.html", {"message": "Entry already exists"})

        # If page for new entry deosn't already exist, save new entry:
        util.save_entry(data["title"], data["content"])
        # Redirect to new entry page
        return HttpResponseRedirect(f"wiki/{data['title']}")

"""Route for a random page"""
def random_page(request):
    # Get list all entries
    entries = util.list_entries()

    # Try and get a random entry from list
    try:
        rand = random.choice(entries)
    # If list is empty
    except IndexError:
        return render(request, "encyclopedia/error.html", {"message": "No available entries"})

    # Redirect user to random entry page
    return  HttpResponseRedirect(f"wiki/{rand}")



"""Route for editting an existing entry"""
def edit(request, entry):

    if request.method == "GET":

        page = util.get_entry(entry)

        if page == None:
            return render(request, "encyclopedia/error.html")

        return render(request, "encyclopedia/create.html", {"page": page, "title": entry})

    else:

        data = request.POST

        util.save_entry(data["title"], data["content"])

        # Redirect to new entry page
        return HttpResponseRedirect(f"/wiki/{data['title']}")










