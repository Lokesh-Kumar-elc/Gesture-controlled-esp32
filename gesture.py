import cv2
import mediapipe as mp
import requests

# ESP32 IP address
ESP32_IP = "192.168.29.112"   # <-- CHANGE THIS

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

last_number = -1

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    number = 0

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]
        lm = hand.landmark

        # Index
        if lm[8].y < lm[6].y:
            number += 1

        # Middle
        if lm[12].y < lm[10].y:
            number += 1

        # Ring
        if lm[16].y < lm[14].y:
            number += 1

        # Pinky
        if lm[20].y < lm[18].y:
            number += 1

        # Thumb
        if lm[4].x < lm[3].x:
            number += 1

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

    # Send only when number changes
    if number != last_number:

        try:
            url = f"http://{ESP32_IP}/set?leds={number}"
            requests.get(url, timeout=0.2)

            print("Fingers:", number)

            last_number = number

        except requests.exceptions.RequestException:
            print("ESP32 connection failed")

    # Show number
    cv2.putText(
        frame,
        str(number),
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        3,
        (0, 255, 0),
        5
    )

    cv2.imshow("Gesture + ESP32", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()