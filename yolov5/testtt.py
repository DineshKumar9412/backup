import cv2
import torch
from PIL import Image
import numpy as np
import ssl
import math
ssl._create_default_https_context = ssl._create_unverified_context

# model = torch.hub.load('ultralytics/yolov5', 'custom', path='pt_files/Aadhar.pt')  # custom model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
CUDA_VISIBLE_DEVICES = "0"

model.conf = 0.50  # confidence threshold (0-1)
model.iou = 0.5  # NMS IoU threshold (0-1)
model.classes = [2]

count = 0
center_points_prev_frame = []
tracking_objects = {}
track_id = 0

vid = cv2.VideoCapture("traffic4.mp4")

while (True):

    ret, frame = vid.read()
    count += 1
    center_points_cur_frame = []
    img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # img2 = cv2.imread(frame)[:, :, ::-1]
    imgs = [img2]
    # print(img2)
    results = model(imgs, size=640)
    results.print()

    a = results.pandas().xyxy[0]
    name = a['name']
    s = a.values.tolist()
    h = name.values.tolist()

    for f,j in zip(s,h):
        a = (f[0:4])
        start_point = (int(a[2]), int(a[1]))
        end_point = (int(a[0]), int(a[3]))
        cx = int((int(a[0]) + int(a[2])) / 2)
        cy = int((int(a[1]) + int(a[3])) / 2)

        center_points_cur_frame.append((cx, cy))

        area = [(300, 800), (600, 400), (1350, 400), (1650, 800)]
        res = cv2.pointPolygonTest(np.array(area, np.int32), (int(cx), int(cy)), False)

    if res >= 0:
        if count <= 2:
            for pt in center_points_cur_frame:
                for pt2 in center_points_prev_frame:
                    distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

                    if distance < 150:
                        tracking_objects[track_id] = pt
                        print(tracking_objects)
                        track_id += 1
        else:
            tracking_objects_copy = tracking_objects.copy()
            center_points_cur_frame_copy = center_points_cur_frame.copy()

            for object_id, pt2 in tracking_objects_copy.items():
                object_exists = False
                for pt in center_points_cur_frame_copy:
                    distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

                    # Update IDs position
                    if distance < 150:
                        tracking_objects[object_id] = pt
                        object_exists = True
                        if pt in center_points_cur_frame:
                            center_points_cur_frame.remove(pt)
                        continue

                # Remove IDs lost
                if not object_exists:
                    tracking_objects.pop(object_id)

            # Add new IDs found
            for pt in center_points_cur_frame:
                tracking_objects[track_id] = pt
                track_id += 1

        for object_id, pt in tracking_objects.items():
            cv2.circle(frame, pt, 5, (0, 0, 255), -1)
            cv2.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0, 1, (0, 0, 255), 2)
            # cv2.rectangle(frame, start_point, end_point, (0, 0, 255), 6)
            # print(object_id)




    #     area = [(300, 800), (600, 400), (1350, 400), (1650, 800)]
    #     res = cv2.pointPolygonTest(np.array(area, np.int32), (int(cx), int(cy)), False)
    #
    #     # if res >= 0:
    #
    # # if count <= 2:
    # #     for pt in center_points_cur_frame:
    # #         for pt2 in center_points_prev_frame:
    # #             distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])
    # #             if distance < 200:
    # #                 tracking_objects[track_id] = pt
    # #                 print(tracking_objects)
    # #                 track_id += 1
    # # else:
    # #     tracking_objects_copy = tracking_objects.copy()
    # #     center_points_cur_frame_copy = center_points_cur_frame.copy()
    # #
    # #     for object_id, pt2 in tracking_objects_copy.items():
    # #         object_exists = False
    # #         for pt in center_points_cur_frame_copy:
    # #             distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])
    # #
    # #             # Update IDs position
    # #             if distance < 200:
    # #                 tracking_objects[object_id] = pt
    # #                 object_exists = True
    # #                 if pt in center_points_cur_frame:
    # #                     center_points_cur_frame.remove(pt)
    # #                 continue
    # #
    # #         # Remove IDs lost
    # #         if not object_exists:
    # #             tracking_objects.pop(object_id)
    # #
    # #     # Add new IDs found
    # #     for pt in center_points_cur_frame:
    # #         tracking_objects[track_id] = pt
    # #         track_id += 1
    # # for object_id, pt in tracking_objects.items():
    # #     cv2.rectangle(frame, start_point, end_point, (0, 0, 255), 6)
    # #     cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
    # #     cv2.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0, 1, (0, 0, 255), 2)

    cv2.polylines(frame, [np.array(area, np.int32)], True, (15, 220, 10), 8)
    cv2.imshow("Test", frame)


    center_points_cur_frame = center_points_prev_frame.copy()

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
