import cv2


class CameraManager:
    @staticmethod
    def get_frame(url: str):
        cap = cv2.VideoCapture(url)
        if not cap.isOpened():
            cap.release()
            return None
        ret, frame = cap.read()
        cap.release()
        if not ret:
            return None
        return frame