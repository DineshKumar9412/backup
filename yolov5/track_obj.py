import cv2
import torch
import ssl
import math
ssl._create_default_https_context = ssl._create_unverified_context


# model = torch.hub.load('ultralytics/yolov5', 'custom', path='pt_files/Aadhar.pt')  # custom model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
CUDA_VISIBLE_DEVICES = "0"

model.conf = 0.50  # confidence threshold (0-1)
model.iou = 0.5  # NMS IoU threshold (0-1)
model.classes = [2]

vid = cv2.VideoCapture("pexels-rodnae-productions-5617905 (online-video-cutter.com).mp4")

count = 0
center_points_cur_frame = []

while (True):
    ret, frame = vid.read()
    count += 1
    img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # img2 = cv2.imread(frame)[:, :, ::-1]
    imgs = [img2]

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

        color = (0, 0, 255)
        thickness = 6
        fontScale = 3
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        image = cv2.rectangle(frame, start_point, end_point, color, thickness)

    for pt in center_points_cur_frame:
        cv2.circle(frame, pt, 5, (0, 0, 255), -1)

    cv2.imshow("Test", frame)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()