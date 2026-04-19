import cv2
import mediapipe as mp
import numpy as np
import pickle
import pyautogui
import time
from features import extract_features

# Load trained model
model = pickle.load(open("../models/gesture_model.pkl", "rb"))

# Camera setup
cap = cv2.VideoCapture(0)

# Screen size
screenW, screenH = pyautogui.size()

# Hand tracking setup
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Smoothing variables
prevX, prevY = 0, 0
alpha = 0.2   # smoothing factor

# Click control
last_click_time = 0
click_delay = 0.8

# FPS
prevTime = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)   # mirror view
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    h, w, c = img.shape
    lmList = []

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    features = extract_features(lmList)

    prediction = "idle"

    if features:
        # Confidence check
        probs = model.predict_proba([features])[0]
        confidence = max(probs)

        if confidence > 0.7:
            prediction = model.predict([features])[0]

    # ---------------- CURSOR CONTROL ----------------
    if prediction == "move" and len(lmList) != 0:

        x1, y1 = lmList[8][1], lmList[8][2]

        # Map coordinates
        frameR = 100
        screenX = np.interp(x1, (frameR, w-frameR), (0, screenW))
        screenY = np.interp(y1, (frameR, h-frameR), (0, screenH))

        # Smooth movement
        currX = prevX + alpha * (screenX - prevX)
        currY = prevY + alpha * (screenY - prevY)

        # Dead zone (remove small jitters)
        if abs(currX - prevX) < 5:
            currX = prevX
        if abs(currY - prevY) < 5:
            currY = prevY

        pyautogui.moveTo(currX, currY)

        prevX, prevY = currX, currY

    # ---------------- CLICK ----------------
    current_time = time.time()

    if prediction == "click":
        if current_time - last_click_time > click_delay:
            pyautogui.click()
            last_click_time = current_time

    # ---------------- SCROLL ----------------
    if prediction == "scroll_up":
        pyautogui.scroll(30)

    elif prediction == "scroll_down":
        pyautogui.scroll(-30)

    # ---------------- DISPLAY ----------------
    cv2.putText(img, f'Gesture: {prediction}', (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    # FPS
    currTime = time.time()
    fps = 1 / (currTime - prevTime) if currTime != prevTime else 0
    prevTime = currTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow("Virtual Mouse", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()