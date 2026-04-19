import cv2
import mediapipe as mp
import csv
from features import extract_features

# Setup camera
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Ask user gesture label
label = input("Enter gesture name (click/move/scroll_up/scroll_down/idle): ")

# Open CSV file
file = open("../data/gestures.csv", "a", newline="")
writer = csv.writer(file)

print("Press 's' to save data, 'q' to quit")

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    features = extract_features(lmList)

    cv2.imshow("Collecting Data", img)

    key = cv2.waitKey(1)

    # Press 's' to save sample
    if key == ord('s') and features:
        writer.writerow([label] + features)
        print("Saved:", [label] + features)

    # Press 'q' to quit
    if key == ord('q'):
        break

file.close()
cap.release()
cv2.destroyAllWindows()