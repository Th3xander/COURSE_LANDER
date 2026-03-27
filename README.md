# Cyber Security Fundamentals Course

A comprehensive web application for learning cybersecurity fundamentals, built with Python FastAPI and modern web technologies.

## Features

- **Interactive Course Dashboard**: Track your progress through 6 comprehensive modules
- **Video Integration**: Embedded YouTube videos for multimedia learning
- **Interactive Quizzes**: Test your knowledge with immediate feedback
- **Progress Tracking**: Monitor your learning journey with visual progress indicators
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional interface with smooth animations

## Course Modules

1. **Introduction to Cybersecurity** - Learn the basics and core concepts
2. **Network Security Fundamentals** - Deep dive into networks and protocols
3. **Common Cyber Threats** - Explore malware, social engineering, and attacks
4. **Cryptography Essentials** - Master encryption and hashing fundamentals
5. **Personal Security Best Practices** - Learn password management and MFA
6. **Ethics, Careers & Mini Project** - Explore career paths and complete a final project

## Project Structure

```
cybersecurity_course/
├── main.py                 # FastAPI application main file
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── templates/             # HTML templates
│   ├── base.html          # Base template with navigation
│   ├── dashboard.html     # Main course dashboard
│   ├── module.html        # Individual module pages
│   ├── lesson.html        # Lesson content pages
│   ├── quiz.html          # Quiz interface
│   └── quiz_result.html   # Quiz results page
└── static/                # Static assets
    ├── css/
    │   └── style.css       # Custom CSS styles
    └── js/
        └── main.js         # JavaScript functionality
```

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

```bash
python main.py
```

The application will start on `http://localhost:8000`

### Alternative: Using uvicorn directly

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Usage

1. **Open the Course**: Navigate to `http://localhost:8000` in your web browser
2. **View Dashboard**: See all available modules and your overall progress
3. **Select a Module**: Click on any unlocked module to begin learning
4. **Complete Lessons**: Watch videos, read notes, and complete activities
5. **Take Quizzes**: Test your knowledge after completing module content
6. **Track Progress**: Monitor your completion status across all modules

## Features Details

### Dashboard
- Overview of all 6 course modules
- Overall progress indicator
- Module status (Completed, In Progress, Locked)
- Quick access to continue learning

### Module Pages
- Three main activities per module:
  - Module Notes & Videos
  - Module Quiz
  - Practical Activities
- Lesson listing with metadata
- Progress tracking

### Lesson Pages
- Embedded YouTube video player
- Comprehensive lesson notes
- Interactive activities checklist
- Quiz preparation section
- Navigation between lessons

### Quiz System
- Multiple choice questions
- Question-by-question navigation
- Progress tracking
- Immediate results and feedback
- 70% passing requirement
- Retake options

## Technology Stack

- **Backend**: FastAPI (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome 6
- **Templating**: Jinja2
- **Video**: YouTube Embedded Player API

## Customization

### Adding New Modules
1. Update the `COURSE_DATA` dictionary in `main.py`
2. Add corresponding content and lessons
3. Create additional templates if needed

### Modifying Styles
- Edit `static/css/style.css` for custom styling
- Variables are defined at the top for easy color scheme changes

### Adding JavaScript Features
- Extend `static/js/main.js` with new functionality
- Use the provided `CourseApp` object for consistent API

## Deployment

### Local Development
```bash
uvicorn main:app --reload
```

### Production (using Gunicorn)
```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Docker Deployment
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t cybersecurity-course .
docker run -p 8000:8000 cybersecurity-course
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or feature requests, please create an issue in the project repository.

---

**Happy Learning!** 🛡️🔐
