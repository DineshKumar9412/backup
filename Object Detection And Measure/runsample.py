from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2

image = cv2.imread("second.jpeg")
# image = cv2.resize(image, (0, 0), None, 0.5, 0.5)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
# perform edge detection + dilation + erosion to close gaps bt edges
edge_detect = cv2.Canny(gray, 100, 100) #play w/min and maxvalues to finetune edges (2nd n 3rd params)
edge_detect = cv2.dilate(edge_detect, None, iterations=1)
edge_detect = cv2.erode(edge_detect, None, iterations=1)

cntours = cv2.findContours(edge_detect.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cntours = imutils.grab_contours(cntours)

(cntours, _) = contours.sort_contours(cntours)


pixel_to_size = None

def mdpt(A, B):
    return ((A[0] + B[0]) * 0.5, (A[1] + B[1]) * 0.5)

# loop over the contours individually
for c in cntours:
    if cv2.contourArea(c) < 100:#ignore/fly through contours that are not big enough
        continue
# compute the rotated bounding box of the contour; should handle cv2 or cv3..
    orig = image.copy()
    bbox = cv2.minAreaRect(c)
    bbox = cv2.cv.boxPoints(bbox) if imutils.is_cv2() else cv2.boxPoints(bbox)
    bbox = np.array(bbox, dtype="int") #order the contours and draw bounding box
    bbox = perspective.order_points(bbox)
    cv2.drawContours(orig, [bbox.astype("int")], -1, (0, 255, 0), 2)

    # loop over the original points in bbox and draw them; 5p red dots
    for (x, y) in bbox:
        cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
        # unpack the ordered bounding bbox; find midpoints
    (tl, tr, br, bl) = bbox
    print(tl,tr, br, bl)
    # (tltrX, tltrY) = mdpt(tl, tr)
    # (blbrX, blbrY) = mdpt(bl, br)
    # (tlblX, tlblY) = mdpt(tl, bl)
    # (trbrX, trbrY) = mdpt(tr, br)
    #
    # cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
    # cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
    # cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
    # cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
    # cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (0, 255, 255), 2)
    # cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (0, 255, 255), 2)
    #
    # dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
    # dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
    # # print(dA  ,   dB)
    # # use pixel_to_size ratio to compute object size
    # if pixel_to_size is None:
    #     pixel_to_size = dB / 0.75
    #     distA = dA / pixel_to_size
    #     distB = dB / pixel_to_size
    #
    #     # draw the object sizes on the image
    #     cv2.putText(orig, "{:.1f}in".format(distA),
    #                 (int(tltrX - 10), int(tltrY - 10)), cv2.FONT_HERSHEY_DUPLEX, 0.55, (255, 255, 255), 2)
    #     cv2.putText(orig, "{:.1f}in".format(distB),
    #                 (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_DUPLEX, 0.55, (255, 255, 255), 2)
    #     # show the output image
    #     cv2.imshow("Image", orig)
    #     cv2.waitKey(0)
