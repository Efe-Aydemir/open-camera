import cv2
import time

print("-"*50)
print("Power On--Sadece bilgisayarın 'e' tuşuna basarak kapatabilirsiniz")
print("-"*50)


vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()

    cv2.imshow('Kamera',frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        print("-"*50)
        print("Kamera Kapandı")
        print("-"*50)
        break
        


vid.release()
cv2.destroyAllWindows()

