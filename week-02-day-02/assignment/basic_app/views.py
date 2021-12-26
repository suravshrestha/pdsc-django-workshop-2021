from django.shortcuts import render

from basic_app.forms import FormAverage

# Create your views here.


def average(request):
    form = FormAverage()

    if request.method == "POST":
        form = FormAverage(request.POST)

        if form.is_valid():
            num1 = form.cleaned_data["first_number"]
            num2 = form.cleaned_data["second_number"]

            average = num2 + (num1 - num2) / 2

            context_dict = {"num1": num1, "num2": num2, "average": average}

            return render(request, "basic_app/render_average.html", context=context_dict)

    context_dict = {"form": form}

    return render(request, "basic_app/form_average.html", context_dict)
