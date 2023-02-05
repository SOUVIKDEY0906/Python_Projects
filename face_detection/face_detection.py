from unicodedata import name
import cv2

dtct = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imp_img = cv2.VideoCapture("elon-musk.jpg")

res, img = imp_img.read()
img_rs = cv2.resize(img, (700, 700))
gray = cv2.cvtColor(img_rs, cv2.COLOR_BGR2GRAY) #converting to grayscale image

#detect faces of different sizes in the input image
faces = dtct.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img_rs, (x,y), (x+w, y+h), (255,255,0), 2) # the four parameters are x,y coordinatek, height, width, color, thickn

# cv2.imshow("project1", img)
cv2.imshow("project1", img_rs)

cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()