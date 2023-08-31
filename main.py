# Import necessary libraries
import cv2
import mediapipe as mp
import pyautogui

# Initialize the webcam
cam = cv2.VideoCapture(0)

# Initialize the FaceMesh model
face_mesh= mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Get the screen size using pyautogui
screen_w , screen_h = pyautogui.size()

# Main loop to process frames from the webcam
while True:
    # Read a frame from the webcam
    _ , frame=cam.read()

    # Flip the frame horizontally
    frame = cv2.flip(frame,1)

    # Convert the frame to RGB format
    rgd_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    # Process the frame using the FaceMesh model
    output=face_mesh.process(rgd_frame)

    # Get the landmark points from the processed frame
    landmark_points=output.multi_face_landmarks

    # Get the height and width of the frame
    frame_h , frame_w , _= frame.shape

    # Print the landmark points (for debugging purposes)
    print(landmark_points)

    # Check if there are any detected landmark points
    if landmark_points:
        # Get the landmarks of the first face detected
        landmarks = landmark_points[0].landmark

        # Iterate through specific landmarks of interest
        for id,landmark in enumerate(landmarks[474:478]):
            # Get the x and y coordinates of the landmark in pixel space
            x= int(landmark.x * frame_w)
            y= int(landmark.y * frame_h)

            # Draw a circle at the landmark's position
            cv2.circle(frame,(x,y),3,(0,255,0))

            # If it's the second landmark, calculate screen coordinates and move the mouse
            if id==1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x,screen_y)

            # Get specific landmarks for left eye
            left = [landmarks[145],landmarks[159]]

            # Draw circles at the left eye landmarks' positions
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))

            # Check if the eye is closed based on vertical distance between landmarks
            if (left[0].y - left[1].y) < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)

    # Display the processed frame with landmarks and actions
    cv2.imshow('Eye Controlled Mouse', frame)


    # Wait for a short period and listen for a key press
    # cv2.waitKey(1)  #wait for '1' second
    cv2.waitKey(1)





