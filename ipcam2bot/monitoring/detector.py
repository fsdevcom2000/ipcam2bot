from ultralytics import YOLO


class HumanDetector:
    def __init__(self, model: str = "yolov8n.pt", conf: float = 0.4):
        self.model = YOLO(model)
        self.conf = conf

    def detect(self, frame) -> bool:
        results = self.model(frame, conf=self.conf, verbose=False)
        for r in results:
            if r.boxes is None:
                continue
            for cls in r.boxes.cls:
                if int(cls) == 0:  # person
                    return True
        return False
