import cv2
import numpy as np

# تعليق فقط للمعلومة، ما يأثر على الكود
# [التاريخ: 19/1/47 - الساعة 5:29 مساءً]

def detect_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # اللون الأحمر له نطاقين في HSV، نحددهم
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # دمج النطاقين مع بعض
    mask = mask1 + mask2
    result = cv2.bitwise_and(frame, frame, mask=mask)
    return result

# تفعيل الكاميرا
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ لم يتم التعرف على الكاميرا.")
        break

    red_detected = detect_color(frame)

    cv2.imshow("Original", frame)
    cv2.imshow("Red Detected", red_detected)

    # الخروج عند الضغط على Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
