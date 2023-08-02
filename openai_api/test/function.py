import cv2
import os

def capture_faces(output_folder, num_samples=30):
    # 使用OpenCV创建一个人脸检测器
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 打开摄像头
    camera = cv2.VideoCapture(0)

    # 用于计数已捕获的人脸图像数量
    count = 0

    while count < num_samples:
        # 读取摄像头的帧
        ret, frame = camera.read()

        # 将帧转换为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 使用人脸检测器检测人脸
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # 绘制矩形框在检测到的人脸上
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # 保存截取的人脸图像
            face_img = frame[y:y+h, x:x+w]
            file_name = os.path.join(output_folder, f"face_{count}.png")
            cv2.imwrite(file_name, face_img)

            count += 1

        # 显示实时摄像头画面
        cv2.imshow('Capture Faces', frame)

        # 按'q'键退出捕获
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 关闭摄像头和销毁窗口
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    output_folder = "faces"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    capture_faces(output_folder, num_samples=5)  # 设置num_samples为所需捕获的人脸图像数量
