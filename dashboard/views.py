from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import QuizForm

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def level(request, course):
    """Render the level page for a specific course."""
    if course.lower() == "ai":
        course = "Artificial Intelligence"
    return render(request, 'level.html', {'course': course})

@login_required
def quiz_view(request, course):
    """Render the quiz page for a specific course."""
    form = QuizForm(course=course)
    if request.method == "POST":
        form = QuizForm(course=course, data=request.POST)
        if form.is_valid():
            score = form.check_answers()
            category = "Beginner" if score <= 5 else "Intermediate" if score <= 8 else "Expert"
            return render(request, 'quiz.html', {'form': form, 'score': score, 'category': category, 'course': course})
    return render(request, 'quiz.html', {'form': form, 'course': course})