# import argparse
import numpy as np
import torch
import yolov5
from typing import Union, List, Optional
import norfair
from norfair import Detection, Tracker, Video
max_distance_between_points: int = 30

files = "production ID.mp4"
detector_path = "yolov5m6.pt"
img_size = 720   #"1080"
conf_thres = "0.25"
iou_thresh = "0.45"
classes = 2 # Multipul class 0 2 3
track_points = "centroid"
# device = "None"None


class YOLO:
    def __init__(self, model_path: str, device: Optional[str] = None):
        if device is not None and "cuda" in device and not torch.cuda.is_available():
            raise Exception(
                "Selected device='cuda', but cuda is not available to Pytorch."
            )
        # automatically set device if its None
        elif device is None:
            device = "cuda:0" if torch.cuda.is_available() else "cpu"
        # load model
        self.model = yolov5.load(model_path, device=device)

    def __call__(
            self,
            img: Union[str, np.ndarray],
            conf_threshold: float = 0.25,
            iou_threshold: float = 0.45,
            image_size: int = 720,
            classes: Optional[List[int]] = None
    ) -> torch.tensor:

        self.model.conf = conf_threshold
        self.model.iou = iou_threshold
        if classes is not None:
            self.model.classes = classes
        detections = self.model(img, size=image_size)
        return detections


def euclidean_distance(detection, tracked_object):
    return np.linalg.norm(detection.points - tracked_object.estimate)


def yolo_detections_to_norfair_detections(
        yolo_detections: torch.tensor,
        track_points: str = 'centroid'  # bbox or centroid
) -> List[Detection]:
    """convert detections_as_xywh to norfair detections
    """
    norfair_detections: List[Detection] = []

    if track_points == 'centroid':
        detections_as_xywh = yolo_detections.xywh[0]
        for detection_as_xywh in detections_as_xywh:
            centroid = np.array(
                [
                    detection_as_xywh[0].item(),
                    detection_as_xywh[1].item()
                ]
            )
            scores = np.array([detection_as_xywh[4].item()])
            norfair_detections.append(
                Detection(points=centroid, scores=scores)
            )
    elif track_points == 'bbox':
        detections_as_xyxy = yolo_detections.xyxy[0]
        for detection_as_xyxy in detections_as_xyxy:
            bbox = np.array(
                [
                    [detection_as_xyxy[0].item(), detection_as_xyxy[1].item()],
                    [detection_as_xyxy[2].item(), detection_as_xyxy[3].item()]
                ]
            )
            scores = np.array([detection_as_xyxy[4].item(), detection_as_xyxy[4].item()])
            norfair_detections.append(
                Detection(points=bbox, scores=scores)
            )

    return norfair_detections


model = YOLO(detector_path, device=None)

for input_path in files:
    video = Video(input_path=input_path)
    tracker = Tracker(
        distance_function=euclidean_distance,
        distance_threshold=max_distance_between_points,
    )

    for frame in video:
        yolo_detections = model(
            frame,
            conf_threshold=conf_thres,
            iou_threshold=iou_thresh,
            image_size=img_size,
            classes=classes
        )
        detections = yolo_detections_to_norfair_detections(yolo_detections, track_points=track_points)
        tracked_objects = tracker.update(detections=detections)
        if track_points == 'centroid':
            norfair.draw_points(frame, detections)
        elif track_points == 'bbox':
            norfair.draw_boxes(frame, detections)
        norfair.draw_tracked_objects(frame, tracked_objects)
        video.write(frame)
