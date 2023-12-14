import cv2

class Face:
    def __init__(self, path):
        self.path = path
        self.photo = None
        self.video = None

    def preprocess(self):
        if self.path.endswith('.jpg') or self.path.endswith('.png'):
            self.photo = cv2.imread(self.path)
        elif self.path.endswith('.mp4'):
            self.video = cv2.VideoCapture(self.path)

    def detect(self):
        # Реализация метода детекта лиц
        pass

    def inference(self):
        # Реализация метода инференса для обработки лиц
        pass

    def display(self, width=None, height=None):
        if self.photo is not None:
            if width is not None and height is not None:
                self.photo = cv2.resize(self.photo, (width, height))
            cv2.imshow('Face Photo', self.photo)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif self.video is not None:
            if width is not None and height is not None:
                self.video.set(cv2.CAP_PROP_FRAME_WIDTH, width)
                self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
            while True:
                ret, frame = self.video.read()
                if not ret:
                    break
                cv2.imshow('Face Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            self.video.release()
            cv2.destroyAllWindows()

# Пример использования класса Face
face = Face('photo.jpg')
face.preprocess()
face.display(width=500, height=500)