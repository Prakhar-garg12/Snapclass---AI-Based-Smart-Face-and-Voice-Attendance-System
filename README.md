<div align="center">

<img src="https://i.ibb.co/YTYGn5qV/logo.png" alt="SnapClass Logo" width="120"/>

# SnapClass — AI-Based Smart Face & Voice Attendance System

**Revolutionizing classroom attendance with next-gen computer vision and voice biometrics.**

[![Live App](https://img.shields.io/badge/🚀%20Live%20App-Streamlit-FF4B4B?style=for-the-badge)](https://snapclass-ai-based-attendance-system.streamlit.app/)
[![Landing Page](https://img.shields.io/badge/🌐%20Landing%20Page-Vercel-000000?style=for-the-badge)](https://snapclass-landing-page-five.vercel.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.io)

</div>

---

## 🔗 Live Links

| Resource | URL |
|---|---|
| 🎯 Main Application | [snapclass-ai-based-attendance-system.streamlit.app](https://snapclass-ai-based-attendance-system.streamlit.app/) |
| 🌐 Landing Page | [snapclass-landing-page-five.vercel.app](https://snapclass-landing-page-five.vercel.app/) |
| 📦 Landing Page Repo | [github.com/Prakhar-garg12/snapclass-landing-page](https://github.com/Prakhar-garg12/snapclass-landing-page) |

> The landing page is directly connected to the main Streamlit app — clicking **"Start AI Attendance"** on the landing page routes users straight into the live system.

---

## 📌 Overview

**SnapClass** is an AI-powered smart attendance system built for modern classrooms. It replaces manual roll-call with two cutting-edge biometric methods:

- **📸 Face Recognition** — Identify every student from a single class photo using deep neural networks.
- **🎙️ Voice Identification** — Students say *"Present"* one-by-one; the system matches their voice against stored embeddings in real-time.

The system supports two roles — **Teacher** and **Student** — each with their own dedicated dashboard and workflow.

---

## ✨ Features

### 👨‍🏫 For Teachers
- 🔐 Secure login with encrypted authentication
- 📊 Unified interactive dashboard to manage all subjects
- 📁 Course management with auto-generated QR codes for student enrollment
- 📸 **FaceID Attendance** — scan the entire room from a single class photo
- 🎙️ **VoiceID Attendance** — sequential voice roll-call with real-time AI matching
- 📋 View historical attendance logs with AI confidence scores
- 📥 Export attendance records as CSV reports

### 👨‍🎓 For Students
- ⚡ Instant course enrollment via unique QR codes or join links
- 🧬 One-time biometric registration (Face + Voice)
- 📱 Personal dashboard to track attendance percentage across all subjects
- 🔔 Real-time attendance status updates

### 🔑 System Highlights
- QR-code-driven roster management — no manual data entry
- Supabase-powered real-time cloud sync
- Fully deployed on Streamlit Cloud — no installation needed for end users

---

## 🏗️ Project Structure

```
Snapclass---AI-Based-Smart-Face-and-Voice-Attendance-System/
│
├── app.py                          # Main entry point — Streamlit app config & role-based routing
├── requirements.txt                # All Python dependencies
├── .gitignore
│
└── src/
    │
    ├── components/                 # Reusable UI dialog components
    │   ├── dialog_add_photo.py         # Dialog for adding/uploading student photos
    │   ├── dialog_attendance_results.py # Dialog to display attendance result summary
    │   ├── dialog_auto_enroll.py       # Auto-enrollment via QR join-code
    │   ├── dialog_create_subject.py    # Dialog for creating a new subject/course
    │   ├── dialog_enroll.py            # Manual student enrollment dialog
    │   ├── dialog_share_subject.py     # Dialog to share subject QR code with students
    │   ├── dialog_voice_attendance.py  # Dialog to handle voice roll-call session
    │   ├── footer.py                   # App-wide footer component
    │   ├── header.py                   # App-wide header / navbar component
    │   └── subject_card.py             # Subject card UI shown on dashboards
    │
    ├── database/                   # Database configuration & query layer
    │   ├── config.py                   # Supabase client setup & credentials
    │   └── db.py                       # All database operations (CRUD)
    │
    ├── pipelines/                  # Core AI inference pipelines
    │   ├── face_pipeline.py            # Face recognition pipeline (dlib + face_recognition)
    │   └── voice_pipeline.py           # Voice identification pipeline (resemblyzer + librosa)
    │
    ├── screens/                    # Full-page screen views
    │   ├── home_screen.py              # Login / role-selection landing screen
    │   ├── student_screen.py           # Student dashboard — enrollment, attendance view
    │   └── teacher_screen.py           # Teacher dashboard — subject & attendance management
    │
    └── ui/                         # Base layout & global UI utilities
        └── base_layout.py              # Shared layout wrapper, styling & page config
```

---

## 🧰 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | Streamlit | Reactive UI framework |
| **Face AI** | `face_recognition` + `dlib` | High-fidelity facial biometrics |
| **Voice AI** | `resemblyzer` + `librosa` | Voice embedding & speaker identification |
| **Database** | Supabase (PostgreSQL) | Real-time cloud storage & auth |
| **Auth** | `bcrypt` | Password hashing & security |
| **QR Codes** | `segno` | Course join-code QR generation |
| **Data** | `numpy`, `pandas`, `scikit-learn` | Data processing & ML utilities |
| **Landing Page** | Flask + Vercel | Static landing layer |

---

## 🚀 Getting Started (Local Setup)

### Prerequisites
- Python 3.10+
- `cmake` and `dlib` build tools installed on your system
- A [Supabase](https://supabase.io) project with the required tables

### 1. Clone the repository

```bash
git clone https://github.com/Prakhar-garg12/Snapclass---AI-Based-Smart-Face-and-Voice-Attendance-System.git
cd Snapclass---AI-Based-Smart-Face-and-Voice-Attendance-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Supabase credentials

Create a `.streamlit/secrets.toml` file:

```toml
SUPABASE_URL = "your-supabase-project-url"
SUPABASE_KEY = "your-supabase-anon-key"
```

### 5. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🔄 How It Works

```
Landing Page (Vercel)
        │
        │  "Start AI Attendance" button
        ▼
Streamlit App (Main System)
        │
        ├─── Teacher Login ──► Dashboard ──► FaceID / VoiceID Attendance
        │                                           │
        │                                     Supabase DB (records saved)
        │
        └─── Student Login ──► Enrollment via QR ──► Biometric Registration
                                                           │
                                                    Dashboard (view attendance)
```

---

## 📸 App Screenshots

> All screenshots are taken from the live SnapClass system.

---

### 🏠 Hero — Overview

<p align="center">
  <img src="https://raw.githubusercontent.com/Prakhar-garg12/snapclass-landing-page/main/static/img/demo/image1.png" width="48%" alt="SnapClass Overview 1"/>
  &nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/Prakhar-garg12/snapclass-landing-page/main/static/img/demo/image2.png" width="48%" alt="SnapClass Overview 2"/>
</p>

---

### 👨‍🏫 Teacher Journey

| Step | Screenshot |
|------|------------|
| **Step 1** — Secure Login & Authentication | <img src="https://raw.githubusercontent.com/Prakhar-garg12/snapclass-landing-page/main/static/img/demo/timage1.png" width="420" alt="Teacher Login"/> |
| **Step 2** — Interactive Dashboard | <img src="https://raw.githubusercontent.com/Prakhar-garg12/snapclass-landing-page/main/static/img/demo/timage2.png" width="420" alt="Teacher Dashboard"/> |
| **Step 3** — Course / Subject Management | <img src="https://raw.githubusercontent.com/Prakhar-garg12/snapclass-landing-page/main/static/img/demo/timage3.png" width="420" alt="Course Management"/> |
| **Step 4** — FaceID Attendance (AI Photo Scan) | <img src="https://raw.githubusercontent.com/Prakhar-garg12/snapclass-landing-page/main/static/img/demo/timage4.png" width="420" alt="FaceID Attendance"/> |
| **Step 5** — VoiceID Attendance (Voice Roll-Call) | <img src="https://raw.githubusercontent.com/Prakhar-garg12/snapclass-landing-page/main/static/img/demo/timage5.png" width="420" alt="VoiceID Attendance"/> |

---

### 👨‍🎓 Student Journey

| Phase | Screenshot |
|-------|------------|
| **Phase 1** — QR-Based Course Enrollment | <img src="https://raw.githubusercontent.com/Prakhar-garg12/snapclass-landing-page/main/static/img/demo/simage1.png" width="420" alt="Student Enrollment"/> |
| **Phase 2** — Biometric Registration (Face + Voice) | <img src="https://raw.githubusercontent.com/Prakhar-garg12/snapclass-landing-page/main/static/img/demo/simage2.png" width="420" alt="Biometric Registration"/> |
| **Phase 3** — Personal Attendance Dashboard | <img src="https://raw.githubusercontent.com/Prakhar-garg12/snapclass-landing-page/main/static/img/demo/simage3.png" width="420" alt="Student Dashboard"/> |

---

## 📦 Dependencies

```txt
streamlit
numpy
pandas
scikit-learn
dlib-bin
face_recognition  (via git)
setuptools<70.0.0
supabase
bcrypt
segno
pillow
librosa
resemblyzer
```

---

## 🌐 Related Repositories

- **Landing Page Source** → [github.com/Prakhar-garg12/snapclass-landing-page](https://github.com/Prakhar-garg12/snapclass-landing-page)
- **Deployed Landing Page** → [snapclass-landing-page-five.vercel.app](https://snapclass-landing-page-five.vercel.app/)

---

## 🙌 Author

**Prakhar Garg**

[![GitHub](https://img.shields.io/badge/GitHub-Prakhar--garg12-181717?style=flat&logo=github)](https://github.com/Prakhar-garg12)

---

## 📄 License

This project is open-source. Feel free to fork, star ⭐, and contribute!

---

<div align="center">
  <b>Built with ❤️ for educators everywhere.</b><br/>
  © 2026 SnapClass AI
</div>
