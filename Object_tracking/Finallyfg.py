import cv2
import numpy as np
import torch
import yolov5
from typing import Union, List, Optional
import norfair
import time
from norfair import Detection, Tracker, Video
from finnalk import euclidean_distance,YOLO,yolo_detections_to_norfair_detections


max_distance_between_points: int = 30
track_points = "bbox"
model = YOLO("yolov5s6.pt", device=None)

video = Video(input_path="traffic4.mp4")

tracker = Tracker(
        distance_function=euclidean_distance,
        distance_threshold=max_distance_between_points,
    )

for frames in video:
    frame = frames[300:1200, 420:1500]
    yolo_detections = model(
                        frame,
                        conf_threshold=0.25,
                        iou_threshold=0.25,
                        image_size=360,
                        classes=2
                    )

    detections = yolo_detections_to_norfair_detections(yolo_detections, track_points=track_points)
    tracked_objects = tracker.update(detections=detections)
    if track_points == 'centroid':
        norfair.draw_points(frame, detections)
    elif track_points == 'bbox':
        norfair.draw_boxes(frame, detections, None, 5)
    norfair.draw_tracked_objects(frame, tracked_objects, None, None, 2, 6)

    for ff in detections:
        p = ff.points
        x,y,w,h = p[0][0],p[0][1],p[1][0],p[1][1]
         #p[0][0] =x [0][1] =y [1][0] =w [1][1]=h

        if y >= 500 and (h >= 730 and h <= 740):
            start_time = time.time()

        if y >= 300 and (h >= 530 and h <= 540):
            end_time = time.time()
            distance = 200 / (end_time - start_time)
            distance = int(distance)
            na= str(distance)
            print(na)
        # if y < 200:
        #     for ffg in tracked_objects:
        #         id = ffg.id
        #         print(id, na)

            # cv2.putText(frame, ("ID :"+ str(ffg.id) + " " + "Speed :"+na), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            #                     (0, 255, 0),
            #                     thickness=2)
    cv2.imshow("Final_Output", frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
