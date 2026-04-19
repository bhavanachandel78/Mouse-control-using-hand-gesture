# 🖐️ AI Virtual Mouse using Hand Gestures

## 📌 Project Overview

This project is an **AI/ML-based Virtual Mouse** that allows users to control their computer using **hand gestures** instead of a physical mouse.
It uses computer vision and machine learning to detect gestures in real-time and perform actions like cursor movement, clicking, and scrolling.

---

## 🚀 Features

* 🖱️ Cursor movement using hand position
* 👆 Click using pinch gesture
* ✌️ Scroll using  thumb-based control)]
* ✊ Idle state detection (no action)
* 📷 Real-time hand tracking using webcam
* ⚡ Smooth and responsive cursor control

---

## 🧠 Technologies Used

* Python
* OpenCV
* MediaPipe
* Scikit-learn
* NumPy
* PyAutoGUI

---

## 🏗️ Project Structure

```
virtual-mouse/
│
├── data/                # Dataset (ignored in GitHub)
├── models/              # Trained ML model
├── scripts/             # Main code files
│   ├── collect_data.py
│   ├── train_model.py
│   ├── main.py
│   └── features.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🎯 How It Works

1. Webcam captures hand movements
2. MediaPipe detects hand landmarks
3. Features are extracted (finger states + distances)
4. ML model predicts gesture
5. PyAutoGUI performs action (move, click, scroll)

---

## 🖐️ Gesture Controls

| Gesture                  | Action      |
| ------------------------ | ----------- |
| ☝️ Index finger up       | Move cursor |
| 🤏 Pinch (thumb + index) | Click       |
| 👍 Thumb up              | Scroll up   |
| 👎 Thumb down            | Scroll down |
| ✊ Fist                   | Idle        |

---

## ⚙️ Installation & Setup

### 1. Clone repository

```
git clone https://github.com/bhavanachandel78/Mouse-control-using-hand-gesture.git
cd Mouse-control-using-hand-gesture
```

### 2. Install dependencies

```
py -3.10 -m pip install -r requirements.txt
```

### 3. Run the project

```
py -3.10 scripts/main.py
```

---

## 📊 Dataset

* Custom dataset created using webcam
* Each gesture recorded with multiple variations
* Features include:

  * Finger states (up/down)
  * Distance between fingers

---

## 🔒 Future Improvements

* User authentication system
* Face recognition for secure access
* Mobile app integration
* Better gesture accuracy using deep learning

---

## 💡 Applications

* Touchless computer control
* Accessibility for disabled users
* Smart home interfaces
* Interactive systems

---

## ⚠️ Notes

* Works best with good lighting
* Keep gestures clear and steady
* Ensure correct Python version (3.10 recommended)

---

## 👩‍💻 Author

Bhavana Chandel

---

## ⭐ Conclusion

This project demonstrates how **AI + Computer Vision** can replace traditional input devices and create more natural human-computer interaction systems.

---
