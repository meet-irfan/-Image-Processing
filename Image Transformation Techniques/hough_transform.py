# -*- coding: utf-8 -*-
"""Hough Transform

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F-aFTdZHDXwZ4k9bS8YCAwvXZQfXLbil
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('/content/image25.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Canny Edge Detector
edges = cv2.Canny(image, 50, 150)

# Apply Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

# Draw lines on the original image
line_image = image.copy()
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 2)

# Display the original, edges, and Hough Line images
plt.figure(figsize=(15, 10))

# Original Image
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

# Edges Detected
plt.subplot(1, 3, 2)
plt.title('Edge Detection (Canny)')
plt.imshow(edges, cmap='gray')

# Lines Detected
plt.subplot(1, 3, 3)
plt.title('Hough Line Transform')
plt.imshow(line_image, cmap='gray')

plt.show()

!pip install PyWavelets

import pywt
print("PyWavelets installed and ready to use!")