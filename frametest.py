import cv2
import time

cap = cv2.VideoCapture(0)
#print(cap.get(3))
#print(cap.get(4))
ret = cap.set(3,640)
ret = cap.set(4,480)

prevTime = 0

while True:
	ret, frame = cap.read()
	
	curTime = time.time()
	sec = curTime - prevTime
	prevTime = curTime

	fps = 1/(sec)
	str = "FPS: %0.1f" % fps

	cv2.putText(frame, str, (0,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))
	
	cv2.imshow('image', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
