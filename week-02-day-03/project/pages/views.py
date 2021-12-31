from django.http.response import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("Hello from home of pages app.")
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")


def send(request):
    return render(request, "pages/send.html")


def receive(request):
    if request.method == "GET":
        # Normal HTTP request (eg. when a URL typed in the browser - in this case /receive)
        html = f"You didn't fill any form. You just typed in the URL in the browser."

        return HttpResponse(html)

    if request.method == "POST":
        # Form submission
        request_obj = request.POST

        email = request_obj.get("email")
        text = request_obj.get("text")
        password = request_obj.get("password")

        html = (f"Hey there! You were redirected here because you filled in a form."
                f"<p>Details you provided:<br>{email = }<br>{text = }<br>{password = }</p>")

        return HttpResponse(html)
