import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
print("Press SPACE to capture image...")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1)
    if key % 256 == 32:
        img_name = "sample.jpg"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} saved!")
        break
    elif key % 256 == 27:
        print("Escape hit, closing...")
        break
cap.release()
cv2.destroyAllWindows()