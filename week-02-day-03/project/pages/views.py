from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    # return HttpResponse("Hello from home of pages app.")
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")


def todo(request):
    if request.method == "POST":
        # Add todo
        todo = request.POST.get("todo")

        if not todo.strip():
            # Empty todo
            return render(request, "pages/empty-todo.html")

        with open("data.txt", "a+") as file:
            file.write(todo + "\n")

    # Display todos
    todos = open("data.txt", "r").readlines()
    context_dict = {"todos": enumerate(todos)}

    return render(request, "pages/todo.html", context=context_dict)


def remove_todo(request, pk):
    line_num = pk + 1
    lines = open("data.txt", "r").readlines()

    line_ptr = 1
    with open("data.txt", "w") as f:
        for line in lines:
            if line_ptr != line_num:
                f.write(line)

            line_ptr += 1

    return redirect("todos")
