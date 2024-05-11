import cv2
import numpy as np

def detect_lanes(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply Canny edge detection to the blurred image
    edges = cv2.Canny(blurred_image, 50, 150)

    # Apply a perspective transform to the edges image
    transformed_edges = perspective_transform(edges)

    # Identify the lane pixels and fit a polynomial to each lane
    left_lane_pixels, right_lane_pixels, left_fit, right_fit = identify_lanes(transformed_edges)

    # Draw the lane lines on the image
    image = draw_lanes(image, left_lane_pixels, right_lane_pixels, left_fit, right_fit)

    return image

def perspective_transform(image):
    # Define the source and destination points for the perspective transform
    source_points = np.float32([[200, 700], [550, 450], [700, 450], [1050, 700]])
    destination_points = np.float32([[250, 700], [250, 0], [1000, 0], [1000, 700]])

    # Apply the perspective transform to the image
    matrix = cv2.getPerspectiveTransform(source_points, destination_points)
    transformed_image = cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))

    return transformed_image

def identify_lanes(edges):
    # Identify the lane pixels and fit a polynomial to each lane
    left_lane_pixels = []
    right_lane_pixels = []

    for i in range(edges.shape[0]):
        row = edges[i]
        for j in range(row.shape[0]):
            if row[j] == 255:
                y = i
                x = j

                if len(left_lane_pixels) == 0:
                    left_lane_pixels.append((x, y))
                elif len(right_lane_pixels) == 0:
                    right_lane_pixels.append((x, y))
                else:
                    left_x, left_y = left_lane_pixels[-1]
                    right_x, right_y = right_lane_pixels[-1]

                    if x < (left_x + right_x) / 2:
                        left_lane_pixels.append((x, y))
                    else:
                        right_lane_pixels.append((x, y))

    left_fit = np.polyfit(left_lane_pixels[:, 1], left_lane_pixels[:, 0], 2)
    right_fit = np.polyfit(right_lane_pixels[:, 1], right_lane_pixels[:, 0], 2)

    return left_lane_pixels, right_lane_pixels, left_fit, right_fit

def draw_lanes(image, left_lane_pixels, right_lane_pixels, left_fit, right_fit):
    # Draw the lane lines on the image
    left_line_image = np.zeros_like(image)
    right_line_image = np.zeros_like(image)

    for i in range(image.shape[0]):
        if len(left_lane_pixels) == 0:
            continue

        left_y = i
        left_x = int(left_fit[0] * left_y ** 2 + left_fit[1] * left_y + left_fit[2])

        if left_x < 0 or left_x > image.shape[1]:
            continue

        cv2.line(left_line_image, (left_x, left_y), (left_x, i), (0, 255, 0), 10)

    for i in range(image.shape[0]):
        if len(right_lane_pixels) == 0:
            continue

        right_y = i
        right_x = int(right_fit[0] * right_y ** 2 + right_fit[1] * right_y + right_fit[2])

        if right_x < 0 or right_x > image.shape[1]:
            continue

        cv2.line(right_line_image, (right_x, right_y), (right_x, i), (0, 255, 0), 10)

    result = cv2.addWeighted(image, 0.8, left_line_image, 1.0, 0.0)
    result = cv2.addWeighted(result, 0.8, right_line_image, 1.0, 0.0)

    return result
