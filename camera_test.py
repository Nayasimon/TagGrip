import cv2

CAMERA_INDEX = 1  # Change to the number that worked for you

CUBE_TAG_IDS = {0, 1, 2, 3, 4, 5}
HAND_TAG_ID = 6

dictionary = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_APRILTAG_36h11
)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

camera = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

if not camera.isOpened():
    raise RuntimeError("Could not open the camera. Check CAMERA_INDEX.")

try:
    while True:
        success, frame = camera.read()
        if not success:
            print("Could not read a camera frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = detector.detectMarkers(gray)

        if ids is not None:
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)
            found = set(int(tag_id) for tag_id in ids.flatten())
            cube_ids = sorted(found & CUBE_TAG_IDS)
            hand_seen = HAND_TAG_ID in found
            message = "Cube: " + (
                ", ".join(str(tag_id) for tag_id in cube_ids) if cube_ids else "-"
            )
            message += "   Hand: " + ("yes" if hand_seen else "no")
        else:
            message = "No tags detected"

        cv2.putText(
            frame,
            message,
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )

        cv2.imshow("TagGrip - press Q to quit", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()