# 🖐️ Finger Counter using MediaPipe & OpenCV

This project uses **MediaPipe** and **OpenCV** in Python to count how many fingers you are holding up in front of your webcam — all in real time!

Perfect for beginners in computer vision who want to experiment with hand tracking and gesture recognition.

---

## 📸 Demo

![Finger Counter Demo](finger_counter.gif)

---

## 🛠️ Features

- ✅ Real-time finger detection using webcam
- ✅ Tracks thumb and four fingers separately
- ✅ Works offline
- ✅ Uses Google’s MediaPipe for accurate hand landmark detection

---

## 📦 Requirements

- Python 3.7–3.11 (✅ Python 3.10 is recommended)
- `mediapipe`
- `opencv-python`

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/manindra-bollam/finger-counter.git
cd finger-counter
```

### 2. (Important) Use Python 3.10

MediaPipe is **not compatible with Python 3.13+**. Install Python 3.10 from [python.org](https://www.python.org/downloads/release/python-3100/) if needed.

### 3. Create a Virtual Environment

```bash
python3.10 -m venv venv
# Activate it:
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

```

### 4. Install Dependencies

Make sure you're inside the virtual environment (you should see `(venv)` at the beginning of your terminal prompt).

```bash
pip install --upgrade pip
pip install mediapipe==0.10.9 opencv-python

```

# ⚠️ Common MediaPipe Errors & Fixes

---

### ❌ `ImportError: DLL load failed while importing _framework_bindings`

This means MediaPipe failed to load its internal native binaries (DLLs).

**✅ Fix:**

Install the required Microsoft Visual C++ Runtime:

- **[Download Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)**

After installing, restart your computer and try again.

---

### ❌ `Could not find a version that satisfies the requirement mediapipe`

This happens if you're using an unsupported Python version (e.g., Python 3.12+).

**✅ Fix:**

MediaPipe officially supports **Python 3.8 – 3.11**.

1.  Uninstall your current Python version if needed.
2.  Install a compatible version like Python 3.10 from the official website:
    - **[https://www.python.org/downloads/release/python-3100/](https://www.python.org/downloads/release/python-3100/)**

---

### ❌ `ModuleNotFoundError: No module named 'cv2'`

You probably typed `pip install cv2`, which is incorrect.

**✅ Fix:**

The correct package name is `opencv-python`:

```bash
pip install opencv-python

```

### ❌ MediaPipe works on one Python version but fails on another

This happens when you're not running the script in the same environment where you installed the packages.

✅ **Fix:**

Ensure you're using the same Python version where MediaPipe was installed. Always activate your virtual environment before running the script:

**Windows:**

```bash
venv\Scripts\activate
```

**macOs/Linux:**

```bash
source venv/bin/activate
```
