import face_recognition
import cv2
from ament_index_python.packages import get_package_share_directory #用于ROS（Robot Operating System）环境中，用于获取包的共享目录路径。

def main():
    # 获取图片真实路径  /home/dameili/chapt4/chapt4_ws/install/demo_python_service/share/demo_python_service/resource
    default_image_path = get_package_share_directory(
        'demo_python_service') + '/resource/default.jpg'
    # 使用 opencv 加载图像
    image = cv2.imread(default_image_path)
    # 查找图像中的所有人脸
    #调用face_recognition.face_locations函数在图像中查找人脸的位置。
    #参数number_of_times_to_upsample=1表示图像将被放大一次以提高检测精度，model='hog'指定使用HOG（Histogram of Oriented Gradients）模型进行人脸检测。
    face_locations = face_recognition.face_locations(
        image, number_of_times_to_upsample=1, model='hog')
    # 绘制每个人脸的边框
    for top, right, bottom, left in face_locations:
        cv2.rectangle(image, (left, top), (right, bottom), (255, 0, 0), 4)
    # 显示结果图像
    cv2.imshow('Face Detection', image)
    cv2.waitKey(0)