import cv2, glob  # glob help us to access all the file present in the folder 

all_images = glob.glob("*.jpg")
# print(all_images)
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

for image in all_images:
    img = cv2.imread(image)
    img_rs = cv2.resize(img, (700, 700))
    gray_img = cv2.cvtColor(img_rs, cv2.COLOR_BGR2GRAY)
    faces = detect.detectMultiScale(gray_img, 1.1, 5)

    for (x,y,w,h) in faces:
        final_img = cv2.rectangle(img_rs, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow("Face detection", final_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()