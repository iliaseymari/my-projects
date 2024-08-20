import cv2

# بارگذاری مدل دیتکتور چهره
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# بارگذاری ویدیو از دوربین
cap = cv2.VideoCapture(0)

while True:
    # خواندن فریم از دوربین
    ret, frame = cap.read()
    
    # تبدیل تصویر به گریسکیل برای بهبود عملکرد دیتکتور
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # استفاده از دیتکتور برای یافتن چهره‌ها
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # رسم مربع دور هر چهره‌ی شناسایی شده
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # نمایش فریم با چهره‌هایی که شناسایی شده‌اند
    cv2.imshow('ilia', frame)
    
    # خروج از حلقه در صورتی که 'q' فشار داده شود
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# آزاد کردن منابع و بستن پنجره نمایش
cap.release()
cv2.destroyAllWindows()
