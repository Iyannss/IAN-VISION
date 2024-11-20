import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Ubahin ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Bikin efek blurnya
    gray = cv2.medianBlur(gray, 5)
    # Deteksi tepi
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Ubah ke warna
    color = cv2.bilateralFilter(frame, 9, 300, 300)
    # Gabungan warna sama tepi
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Output
    cv2.imshow("Cartoon Filter", cartoon)

    # Keluar dari program jika menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
