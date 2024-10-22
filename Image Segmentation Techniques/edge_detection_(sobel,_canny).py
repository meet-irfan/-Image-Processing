# -*- coding: utf-8 -*-
"""Edge Detection (Sobel, Canny)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XwZDOb-nI2O9NMhV_kPz1xx7TBtgBf3_
"""

import cv2
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('/content/345.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel edge detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)  # Horizontal edges
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)  # Vertical edges

# Display Sobel images
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

# Sobel X
plt.subplot(1, 3, 2)
plt.title('Sobel X')
plt.imshow(sobel_x, cmap='gray')

# Sobel Y
plt.subplot(1, 3, 3)
plt.title('Sobel Y')
plt.imshow(sobel_y, cmap='gray')

plt.show()