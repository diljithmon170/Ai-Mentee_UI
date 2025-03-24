from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import QuizForm
from django.conf import settings
from django.templatetags.static import static  # ✅ Import static
import os



# Course Mapping Dictionary
COURSE_MAPPING = {
    "ai": "Artificial Intelligence",
    "dbms": "Database Management System",
    "ml": "Machine Learning",
    "python": "Python",
    "java": "Java"
}

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def level(request, course):
    """Render the level page for a specific course."""
    course_display_name = course  # Default to the original course name
    if course.lower() == "ai":
        course_display_name = "Artificial Intelligence"
    if course.lower() == "dbms":
        course_display_name = "Database Management System"
    if course.lower() == "ml":
        course_display_name = "Machine Learning"
    if course.lower() == "python":
        course_display_name = "Python"
    if course.lower() == "java":
        course_display_name = "Java"
    return render(request, 'level.html', {'course': course, 'course_display_name': course_display_name})

@login_required
def quiz_view(request, course):
    """Render the quiz page for a specific course."""
    course_display_name = course  # Default to the original course name
    if course.lower() == "ai":
        course_display_name = "Artificial Intelligence"
    if course.lower() == "dbms":
        course_display_name = "Database Management System"
    if course.lower() == "ml":
        course_display_name = "Machine Learning"
    if course.lower() == "python":
        course_display_name = "Python"
    if course.lower() == "java":
        course_display_name = "Java"
        
    form = QuizForm(course=course)
    if request.method == "POST":
        form = QuizForm(course=course, data=request.POST)
        if form.is_valid():
            score = form.check_answers()
            category = "Beginner" if score <= 5 else "Intermediate" if score <= 8 else "Expert"
            return render(request, 'quiz.html', {
                'form': form,
                'score': score,
                'category': category,
                'course': course,
                'course_display_name': course_display_name
            })
    return render(request, 'quiz.html', {
        'form': form,
        'course': course,
        'course_display_name': course_display_name
    })

@login_required
def text_view(request, course, level, file_number=1):
    """Render the text content dynamically for a specific course and level."""
    
    base_dir = os.path.join('dashboard', 'templates', 'interfaces', 'text_files')
    file_name = f"{course}_{level}{file_number}.txt"
    file_path = os.path.join(base_dir, file_name)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content_lines = file.readlines()
        error = None
    except FileNotFoundError:
        content_lines = []
        error = f"The file {file_name} could not be found."

    # Check for next and previous file availability
    next_file = os.path.exists(os.path.join(base_dir, f"{course}_{level}{file_number + 1}.txt"))
    prev_file = file_number > 1 and os.path.exists(os.path.join(base_dir, f"{course}_{level}{file_number - 1}.txt"))

    return render(request, 'interfaces/text.html',
 {
        'course': course,
        'level': level,
        'content_lines': content_lines,
        'error': error,
        'file_number': file_number,
        'next_file': next_file,
        'prev_file': prev_file,
    })





@login_required
def content_view(request, course, level):
    """Render the content page for the selected course and level."""
    return render(request, 'content.html', {
        'course': course,
        'level': level,
        'course_display_name': course.capitalize(),  # Capitalize course name for display
    })



# @login_required
# def text_view(request, level):
#     """Render the text content page."""
#     return render(request, 'interfaces/text.html', {'level': level})

@login_required
def video_view(request, course, level, file_number=1):
    # ✅ Construct the correct video filename (e.g., python_beginner1.mp4)
    video_filename = f"{course.lower()}_{level.lower()}{file_number}.mp4"

    # ✅ Correct path to video files inside `dashboard/static/video/`
    video_url = f"/static/video/{video_filename}"

    # ✅ Check if the file exists
    video_file_path = os.path.join(settings.BASE_DIR, "dashboard", "static", "video", video_filename)

    if not os.path.exists(video_file_path):
        return render(request, "interfaces/video.html", {
            "error": "Video file not found",
            "course": course,
            "level": level
        })

    # ✅ Check if the next file exists
    next_file = file_number + 1
    next_video_filename = f"{course.lower()}_{level.lower()}{next_file}.mp4"
    next_video_path = os.path.join(settings.BASE_DIR, "dashboard", "static", "video", next_video_filename)
    next_exists = os.path.exists(next_video_path)

    context = {
        "course": course,
        "level": level,
        "video_url": video_url,  # ✅ Ensure correct static URL
        "prev_file": file_number - 1 if file_number > 1 else None,
        "next_file": next_file if next_exists else None,
    }

    return render(request, "interfaces/video.html", context)


@login_required
def audio_view(request, course, level, file_number=1):
    # ✅ Construct the correct audio filename
    audio_filename = f"{course.lower()}_{level.lower()}{file_number}.mp3"

    audio_url = f"/static/audio/{audio_filename}"
    # ✅ Define the actual file path to check existence (not needed for the frontend)
    audio_file_path = os.path.join(settings.STATICFILES_DIRS[2], "audio", audio_filename)

    # ✅ Check if the next file exists
    next_file = file_number + 1
    next_audio_filename = f"{course.lower()}_{level.lower()}{next_file}.mp3"
    next_audio_path = os.path.join(settings.STATICFILES_DIRS[2], "audio", next_audio_filename)
    next_exists = os.path.exists(next_audio_path)

    context = {
        "course": course.title(),
        "level": level.title(),
        "audio_url": audio_url,  # ✅ Correct audio URL for template
        "prev_file": file_number - 1 if file_number > 1 else None,  # Enable back button
        "next_file": next_file if next_exists else None,  # Enable next button only if file exists
    }

    return render(request, "interfaces/audio.html", context)  # ✅ Correct template path
