class DetectedFrame:
    def __init__(self,dilated_image,detected_image,annotations):
        self.dilated_image = dilated_image
        self.detected_image = detected_image
        self.annotations = annotations