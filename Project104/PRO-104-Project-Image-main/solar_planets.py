import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Display the original image
cv2.imshow("output", img)
cv2.waitKey(0)

# Add text to each planet
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
font_thickness = 2
font_color = (255, 255, 255)  # White color

# Mercury
mercury_text = "Mercury"
mercury_position = (100, 100)
cv2.putText(img, mercury_text, mercury_position, font, font_scale, font_color, font_thickness)

# Venus
venus_text = "Venus"
venus_position = (250, 100)
cv2.putText(img, venus_text, venus_position, font, font_scale, font_color, font_thickness)

# Earth
earth_text = "Earth"
earth_position = (400, 100)
cv2.putText(img, earth_text, earth_position, font, font_scale, font_color, font_thickness)

# Add text for other planets...

# Display the image with text
cv2.imshow("output", img)
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_system_with_name.jpg", img)

# Close all windows
cv2.destroyAllWindows()
