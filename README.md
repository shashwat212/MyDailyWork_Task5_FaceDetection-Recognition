# 👤 MyDailyWork_Task5: FaceDetection-Recognition-System

A **real-time face detection-based security system** built using **Python** and **OpenCV**.  
This project simulates a **face-based access mechanism** similar to real-world biometric systems.

---

## 📌 Features

- 🎥 Real-time face detection using webcam  
- 🔒 Locked system state when no face is detected  
- ⏱️ Countdown timer when a face appears  
- 🔓 Automatic unlock when face remains visible  
- 🔒 Re-locks immediately when face disappears  
- 🟢🟡🔴 Clear visual status indicators (Green, Yellow, Red)  

---

## 🛠️ Technologies Used

- **Python 3.11**  
- **OpenCV (Haar Cascade Classifier)**  
- **Computer Vision**  

---

## ⚙️ How It Works

1. System starts in **locked state**  
2. Detects a human face using **Haar Cascade**  
3. Starts a **countdown timer** when a face appears  
4. Unlocks system after the face remains visible for a few seconds  
5. Locks again when the face disappears  

---

## 📂 Files Included

- `face_detection.py`  
- `haarcascade_frontalface_default.xml`  

---

## ▶️ How to Run

### Step 1: Install dependencies
```bash
pip install opencv-python
```

### Step 2: Run the program
```bash
python face_detection.py
```

### Step 3: Exit the program  
Press **`q`** to quit.

---

## 🎥 Demo

A demo video of this project has been uploaded on **LinkedIn** as part of *MyDailyWork AI Internship Task 5*.
