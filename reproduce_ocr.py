import os
import sys

# Add the project root to the python path
sys.path.append('/home/student/Documents/Back_end/Personal_Financial_Assistant')

from assistant.utils import extract_receipt_data

test_images = [
    '/home/student/Documents/Back_end/Personal_Financial_Assistant/needed_img/ReceiptSwiss.jpg',
    '/home/student/Documents/Back_end/Personal_Financial_Assistant/needed_img/check.avif'
]

print("Starting OCR reproduction...")

for img_path in test_images:
    print(f"\nProcessing {img_path}...")
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        continue
        
    try:
        merchant, amount = extract_receipt_data(img_path)
        print(f"Result for {os.path.basename(img_path)}:")
        print(f"Merchant: {merchant}")
        print(f"Amount: {amount}")
    except Exception as e:
        print(f"Error processing {img_path}: {e}")
