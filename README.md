# Face Recognition Attendance System

## Overview

The Face Recognition Attendance System is an AI-powered attendance management application that automatically detects and recognizes faces using computer vision techniques. The system identifies students in real time through a webcam feed and marks attendance automatically.

The project uses facial recognition technology to reduce manual attendance processes and improve accuracy.

---

## Features

- Real-time face detection
- Face recognition using AI
- Automated attendance marking
- Live webcam integration
- Firebase Realtime Database integration
- Student information display
- Attendance tracking system
- Local image processing
- Interactive graphical interface

---

## Tech Stack

### Programming Language
- Python

### Libraries & Frameworks
- OpenCV
- face_recognition
- NumPy
- cvzone
- Pickle

### Database
- Firebase Realtime Database

### Tools
- PyCharm
- Git & GitHub

---

## Project Workflow

```text
Webcam Feed
      ↓
Face Detection
      ↓
Face Encoding
      ↓
Face Matching
      ↓
Student Identification
      ↓
Attendance Update
      ↓
Display Student Information
```

---

## Folder Structure

```text
project/
│
├── images/
├── Resources/
├── EncodeFile.p
├── EncoderGenerator.py
├── main.py
├── requirements.txt
└── README.md
```

---

## How It Works

1. The webcam captures live video frames.
2. The system detects faces from the video stream.
3. Face encodings are generated using facial recognition algorithms.
4. Encodings are compared with stored student encodings.
5. If a match is found, student information is fetched from Firebase.
6. Attendance is automatically updated and displayed.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Salikkhan01/face-recognition-attendance-system.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Encoder Generator

```bash
python EncoderGenerator.py
```

### Run Main Application

```bash
python main.py
```

---

## Future Scope

- Multi-face attendance support
- Cloud deployment
- Mobile application integration
- Advanced deep learning models
- Real-time analytics dashboard
- CCTV camera integration

---

## Advantages

- Saves time
- Reduces manual errors
- Improves attendance accuracy
- Contactless attendance system
- Automated student identification

---


## Contributors

### Salik Khan

AI/ML Engineering Student

---

## License

This project is developed for educational and learning purposes.
