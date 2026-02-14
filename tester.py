import pytesseract
from pytesseract import Output
import cv2
import matplotlib.pyplot as plt
import numpy as np
import re
plt.rcParams["figure.figsize"] = (20, 30)

img = cv2.imread(
    "/home/student/Documents/Back_end/Personal_Financial_Assistant/needed_img/check3.avif")






d = pytesseract.image_to_data(img, output_type=Output.DICT)


prices = r'\d+[.,]\d+'
things = r'[a-zA-Z\s]+'

n_boxes = len(d['text'])
# for i in range(n_boxes):
#     if int(d['conf'][i]) > 60:
#         if re.match(prices, d['text'][i]):
#             (x, y, w,
#              h) = d["left"][i], d["top"][i], d["width"][i], d["height"][i]
#             img = cv2.rectangle(img, (x, y), (x+w, y+h),
#                                 (0, 255, 0), 2)  # Plotting bounding box
#             print(f"Prices {d['text'][i]}")

        
#         if re.match(things, d['text'][i]):
#             (x, y, w,
#              h) = d["left"][i], d["top"][i], d["width"][i], d["height"][i]
#             img = cv2.rectangle(img, (x, y), (x+w, y+h),
#                                 (0, 255, 0), 2)

#             print(f"Names {d['text'][i]}")

# plt.imshow(img)


float_pattern = r'\d+[.,]\d+'

# Assuming 'd' is your Output.DICT from image_to_data
lines = {}
for i in range(n_boxes):
    text = d['text'][i].strip()
    conf = int(d['conf'][i])

    # Ignore empty text and low confidence
    if text and conf > 30:
        # Create a unique ID for the line using block and line number
        line_id = f"block_{d['block_num'][i]}_line_{d['line_num'][i]}"

        if line_id not in lines:
            lines[line_id] = []

        lines[line_id].append(text)

# Now filter: Only keep lines that contain a float
for line_id, words in lines.items():
    full_line_text = " ".join(words)

    if re.search(float_pattern, full_line_text):
        print(f"💰 Found Row: {full_line_text}")
