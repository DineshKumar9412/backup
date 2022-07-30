# import argparse
import cv2
import numpy as np
import torch
import yolov5
from typing import Union, List, Optional
import norfair
from norfair import Detection, Tracker, Video
# from datetime import datetime
import time
max_distance_between_points: int = 30

track_points = "bbox"
devices = "cpu"

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
        conf_threshold: float = 0.55,
        iou_threshold: float = 0.45,
        image_size: int = 480,
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
#
# vid = "traffic4.mp4"
#
# model = YOLO("yolov5s6.pt", device=devices)
#
# # area = [(300, 800), (600, 400), (1350, 400), (1650, 800)]
#
# area = [(180, 1020), (500, 500), (1400, 500), (1800, 1020)]
#
# video = Video(input_path=vid)
# tracker = Tracker(
#     distance_function=euclidean_distance,
#     distance_threshold=max_distance_between_points,
# )
#
# for frame in video:
#     # frame = frames[500:1000, 500:1500]
#     col, row = 900,800
#     co, ro = 920,300
#     # cv2.circle(frame, (col, row), 10, (0, 255, 0), -1)
#     # cv2.circle(frame, (co, ro), 10, (0, 255, 0), -1)
#
#
#     # yolo_detections = model(
#     #     frame,
#     #     conf_threshold=0.50,
#     #     iou_threshold=0.45,
#     #     image_size= 480,
#     #     classes= 2
#     # )
#     # detections = yolo_detections_to_norfair_detections(yolo_detections, track_points=track_points)
#     # tracked_objects = tracker.update(detections=detections)
#     # if tracked_objects != 0:
#     #     for fg in tracked_objects:
#     #        tim1 = time.time()  # Initial time
#     #        print("Car Entered.")
#     # for det in detections:
#     #     sd = det.points[0][0]
#     #     sf = det.points[0][1]
#     #     if (sd >= coord[0][0] and y == coord[0][1]):
#         # for df in tracked_objects:
#         #     if df.id == 2:
#         #         end = datetime.now()
#         #         print('Duration: {}'.format(end - st_tm))
#     #     times.append(["1", st_tm])
#     # print(times)
#
#     #     for df in tracked_objects:
#     #         times.append([df.id, st_tm])
#     #
#     # print(times)
#
#     #
#     # if track_points == 'centroid':
#     #     norfair.draw_points(frame, detections)
#     # elif track_points == 'bbox':
#     #     norfair.draw_boxes(frame, detections,None,5)
#     # norfair.draw_tracked_objects(frame, tracked_objects,None,None,2,6)
#     # cv2.polylines(frames, [np.array(area, np.int32)], True, (15, 220, 10), 8)
#     # cv2.line(frames, (150, 1000), (1850, 1000), (0, 0, 255), 10)
# #     # cv2.line(frames, (150, 900), (1800, 900), (0, 0, 255), 10)
# #     # cv2.line(frames, (480, 600), (1450, 600), (0, 0, 255), 10)
# #     cv2.line(frames, (500, 500), (1400, 500), (0, 0, 255), 10)
# #         cv2.line(frames, (341, 499), (348, 570), (0, 0, 255), 10)
#     cv2.imshow("hfdghgx", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # vid.release()
# cv2.destroyAllWindows()
