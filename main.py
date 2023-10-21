import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = 0
while True:
    success, img = cap.read()
    fileName = f'./generated/frame_{frame_count:03d}.jpg'
    cv2.imwrite(fileName, img)
    if success:
        cv2.imshow('capturing', img)
    frame_count += 1
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
