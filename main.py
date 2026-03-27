from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import uvicorn

app = FastAPI(title="Cyber Security Fundamentals Course")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Course data structure
COURSE_DATA = {
    "title": "Cyber Security Fundamentals For Beginners",
    "description": "Master the fundamentals of cybersecurity with hands-on learning",
    "modules": [
        {
            "id": 1,
            "title": "Introduction to Cybersecurity",
            "description": "Learn the basics of cybersecurity, network fundamentals, and core concepts",
            "duration": "2h 30min",
            "videos": 8,
            "status": "completed",
            "progress": 100,
            "content": {
                "lessons": [
                    {
                        "id": 1,
                        "title": "What is Cyber Security?",
                        "description": "Introduction to cybersecurity fundamentals",
                        "video_url": "https://www.youtube.com/watch?v=ULGILG-ZhO0&pp=ygUqSW50cm9kdWN0aW9uIHRvIGN5YmVyc2VjdXJpdHkgZnVuZGFtZW50YWxz",
                        "notes": [
                            "Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks",
                            "It aims to prevent unauthorized access, data damage, or disruption",
                            "Key pillars: Confidentiality, Integrity, Availability (CIA triad)"
                        ],
                        "activities": [
                            "Read chapter on cybersecurity fundamentals",
                            "Complete basic security assessment",
                            "Watch supplementary video on threat landscape"
                        ]
                    },
                    {
                        "id": 2,
                        "title": "Network Security Basics",
                        "description": "Understanding network fundamentals and security",
                        "video_url": "https://www.youtube.com/watch?v=1zVZ9cWFnCc&pp=ygUXTmV0d29yayBTZWN1cml0eSBCYXNpY3M%3D",
                        "notes": [
                            "Network security is the practice of preventing and protecting against unauthorized intrusion into networks",
                            "A firewall is a network security device that monitors and filters incoming and outgoing network traffic",
                            "VPNs create secure, encrypted connections over public networks"
                        ],
                        "activities": [
                            "Read chapter on network protocols",
                            "Complete firewall configuration lab",
                            "Watch supplementary video on VPN setup"
                        ]
                    }
                ],
                "quiz": {
                    "title": "Introduction to Cybersecurity Quiz",
                    "questions": [
                        {
                            "id": 1,
                            "question": "What is the primary purpose of a firewall in network security?",
                            "options": [
                                "To encrypt all network traffic",
                                "To filter incoming and outgoing network traffic based on security rules",
                                "To speed up internet connection",
                                "To store passwords securely"
                            ],
                            "correct": 1
                        },
                        {
                            "id": 2,
                            "question": "What does VPN stand for?",
                            "options": [
                                "Virtual Private Network",
                                "Virus Protection Network",
                                "Video Processing Network",
                                "Virtual Public Network"
                            ],
                            "correct": 0
                        }
                    ]
                }
            }
        },
        {
            "id": 2,
            "title": "Network Security Fundamentals",
            "description": "Deep dive into network protocols, IP addressing, and security mechanisms",
            "duration": "3h 15min",
            "videos": 12,
            "status": "in_progress",
            "progress": 85,
            "content": {
                "lessons": [
                    {
                        "id": 1,
                        "title": "What is a Network & How It Works",
                        "description": "Understanding computer networks and data transmission",
                        "video_url": "https://www.youtube.com/watch?v=7_LPdttKXPc&pp=ygUgV2hhdCBpcyBhIE5ldHdvcmsgJiBIb3cgSXQgV29ya3M%3D",
                        "notes": [
                            "Computer network is a collection of nodes connected by communication links",
                            "Data is split into small pieces called packets",
                            "Packets travel through devices like routers and switches",
                            "The destination receives and reassembles the packets"
                        ],
                        "activities": [
                            "Demo: Using ping command",
                            "Trace website visit process",
                            "Basic packet inspection exercise"
                        ]
                    },
                    {
                        "id": 2,
                        "title": "Phishing Attacks",
                        "description": "Understanding and identifying phishing attacks",
                        "video_url": "https://www.youtube.com/watch?v=XBkzBrXlle0&pp=ygUuVW5kZXJzdGFuZGluZyBhbmQgaWRlbnRpZnlpbmcgcGhpc2hpbmcgYXR0YWNrc9IHCQnXCgGHKiGM7w%3D%3D",
                        "notes": [
                            "Phishing is a cybercrime where attackers pretend to be trusted entities",
                            "Common methods: Fake emails, fake login websites, suspicious links",
                            "Carried out through internet/network, usually via email or websites"
                        ],
                        "activities": [
                            "Identify phishing email examples",
                            "Create phishing awareness guidelines",
                            "Practice safe email handling"
                        ]
                    }
                ],
                "quiz": {
                    "title": "Network Security Quiz",
                    "questions": [
                        {
                            "id": 1,
                            "question": "What is the purpose of DNS?",
                            "options": [
                                "To encrypt data",
                                "To translate domain names to IP addresses",
                                "To filter network traffic",
                                "To store passwords"
                            ],
                            "correct": 1
                        }
                    ]
                }
            }
        },
        {
            "id": 3,
            "title": "Common Cyber Threats",
            "description": "Explore malware, social engineering, and common attack vectors",
            "duration": "2h 45min",
            "videos": 10,
            "status": "in_progress",
            "progress": 30,
            "content": {
                "lessons": [
                    {
                        "id": 1,
                        "title": "Malware Programs",
                        "description": "Understanding different types of malicious software",
                        "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ",
                        "notes": [
                            "Malware refers to intrusive software developed by cybercriminals",
                            "Types: Viruses, Worms, Trojans, Ransomware, Spyware, Adware, Bots",
                            "Fileless malware operates without traditional executable files"
                        ],
                        "activities": [
                            "Analyze malware case studies",
                            "Identify malware symptoms",
                            "Create malware response plan"
                        ]
                    }
                ],
                "quiz": {
                    "title": "Cyber Threats Quiz",
                    "questions": [
                        {
                            "id": 1,
                            "question": "What is the main difference between a virus and a worm?",
                            "options": [
                                "Viruses are more dangerous",
                                "Worms can self-replicate and spread across networks",
                                "Viruses encrypt files",
                                "Worms require user interaction"
                            ],
                            "correct": 1
                        }
                    ]
                }
            }
        },
        {
            "id": 4,
            "title": "Cryptography Essentials",
            "description": "Learn encryption, hashing, and cryptographic fundamentals",
            "duration": "3h 00min",
            "videos": 15,
            "status": "locked",
            "progress": 0,
            "content": {
                "lessons": [
                    {
                        "id": 1,
                        "title": "Introduction to Encryption",
                        "description": "Understanding encryption fundamentals",
                        "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ",
                        "notes": [
                            "Encryption is scrambling information so only someone with the right key can understand it",
                            "Strong encryption uses complex algorithms like AES-256",
                            "Symmetric vs Asymmetric encryption"
                        ],
                        "activities": [
                            "Caesar Cipher implementation",
                            "Hashing demonstration",
                            "Digital signature exercise"
                        ]
                    }
                ],
                "quiz": {
                    "title": "Cryptography Quiz",
                    "questions": [
                        {
                            "id": 1,
                            "question": "What is the main purpose of hashing?",
                            "options": [
                                "To encrypt data",
                                "To ensure data integrity",
                                "To compress files",
                                "To speed up networks"
                            ],
                            "correct": 1
                        }
                    ]
                }
            }
        },
        {
            "id": 5,
            "title": "Personal Security Best Practices",
            "description": "Master password management, MFA, and personal security hygiene",
            "duration": "2h 20min",
            "videos": 9,
            "status": "locked",
            "progress": 0,
            "content": {
                "lessons": [
                    {
                        "id": 1,
                        "title": "Strong Passwords and MFA",
                        "description": "Creating secure passwords and implementing multi-factor authentication",
                        "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ",
                        "notes": [
                            "Strong passwords require length and mix of characters",
                            "Multi-factor authentication adds extra security layer",
                            "Software updates patch security vulnerabilities"
                        ],
                        "activities": [
                            "Password strength checker exercise",
                            "Set up MFA demonstration",
                            "Security audit checklist"
                        ]
                    }
                ],
                "quiz": {
                    "title": "Personal Security Quiz",
                    "questions": [
                        {
                            "id": 1,
                            "question": "What makes a password strong?",
                            "options": [
                                "Only letters",
                            "Short and simple",
                            "Long with mixed characters",
                            "Common words"
                        ],
                            "correct": 2
                        }
                    ]
                }
            }
        },
        {
            "id": 6,
            "title": "Ethics, Careers & Mini Project",
            "description": "Explore cybersecurity ethics, career paths, and complete a final project",
            "duration": "2h 50min",
            "videos": 11,
            "status": "locked",
            "progress": 0,
            "content": {
                "lessons": [
                    {
                        "id": 1,
                        "title": "Cybersecurity Ethics",
                        "description": "Understanding ethical hacking and responsible disclosure",
                        "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ",
                        "notes": [
                            "Cybersecurity ethics involves protecting data according to moral principles",
                            "Ethical hacking vs illegal hacking",
                            "Responsible disclosure process"
                        ],
                        "activities": [
                            "Ethics scenario analysis",
                            "Career path research",
                            "Mini project development"
                        ]
                    }
                ],
                "quiz": {
                    "title": "Ethics & Careers Quiz",
                    "questions": [
                        {
                            "id": 1,
                            "question": "What is responsible disclosure?",
                            "options": [
                                "Hacking without permission",
                                "Reporting vulnerabilities to organizations",
                                "Publishing exploits publicly",
                                "Keeping vulnerabilities secret"
                            ],
                            "correct": 1
                        }
                    ]
                }
            }
        }
    ]
}

# Calculate overall progress
def calculate_overall_progress():
    total_progress = sum(module["progress"] for module in COURSE_DATA["modules"])
    return total_progress // len(COURSE_DATA["modules"])

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    overall_progress = calculate_overall_progress()
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "course": COURSE_DATA,
        "overall_progress": overall_progress
    })

@app.get("/module/{module_id}", response_class=HTMLResponse)
async def module_detail(request: Request, module_id: int):
    module = next((m for m in COURSE_DATA["modules"] if m["id"] == module_id), None)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    
    return templates.TemplateResponse("module.html", {
        "request": request,
        "module": module,
        "course": COURSE_DATA
    })

@app.get("/lesson/{module_id}/{lesson_id}", response_class=HTMLResponse)
async def lesson_detail(request: Request, module_id: int, lesson_id: int):
    module = next((m for m in COURSE_DATA["modules"] if m["id"] == module_id), None)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    
    lesson = next((l for l in module["content"]["lessons"] if l["id"] == lesson_id), None)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    
    # Calculate lesson index
    lesson_index = next((i for i, l in enumerate(module["content"]["lessons"], 1) if l["id"] == lesson_id), 1)
    
    return templates.TemplateResponse("lesson.html", {
        "request": request,
        "module": module,
        "lesson": lesson,
        "lesson_index": lesson_index,
        "course": COURSE_DATA
    })

@app.get("/quiz/{module_id}", response_class=HTMLResponse)
async def quiz_page(request: Request, module_id: int):
    module = next((m for m in COURSE_DATA["modules"] if m["id"] == module_id), None)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    
    return templates.TemplateResponse("quiz.html", {
        "request": request,
        "module": module,
        "quiz": module["content"]["quiz"]
    })

@app.post("/quiz/{module_id}/submit")
async def submit_quiz(request: Request, module_id: int, answers: dict = Form(...)):
    module = next((m for m in COURSE_DATA["modules"] if m["id"] == module_id), None)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    
    quiz = module["content"]["quiz"]
    score = 0
    total = len(quiz["questions"])
    
    for question in quiz["questions"]:
        if str(question["id"]) in answers and int(answers[str(question["id"])]) == question["correct"]:
            score += 1
    
    percentage = (score / total) * 100
    passed = percentage >= 70
    
    return templates.TemplateResponse("quiz_result.html", {
        "request": request,
        "module": module,
        "score": score,
        "total": total,
        "percentage": percentage,
        "passed": passed
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
