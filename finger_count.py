import cv2
import mediapipe as mp

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Finger tip landmark IDs (thumb to pinky)
finger_tips_ids = [4, 8, 12, 16, 20]

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip and convert to RGB
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to find hands
    results = hands.process(rgb)

    count = 0
    h, w, _ = frame.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []

            # Extract landmark positions
            for id, lm in enumerate(hand_landmarks.landmark):
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            # Count fingers
            # Thumb (check left vs right based on x axis)
            if lm_list[4][0] > lm_list[3][0]:  # For right hand
                count += 1

            # Fingers (index to pinky)
            for tip_id in finger_tips_ids[1:]:
                if lm_list[tip_id][1] < lm_list[tip_id - 2][1]:
                    count += 1

            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show count
    cv2.rectangle(frame, (0, 0), (150, 100), (0, 0, 0), -1)
    cv2.putText(frame, f'Fingers: {count}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                1.8, (0, 255, 0), 3)

    # Display
    cv2.imshow("Finger Counter", frame)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
