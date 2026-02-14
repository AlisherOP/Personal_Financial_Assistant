import pytesseract
from pytesseract import Output
import cv2
import re

pytesseract.pytesseract.pytesseract_cmd = r'/usr/bin/tesseract'


def extract_receipt_data(image_path):
    """
    Processes a receipt image and extracts merchant and total amount.
    Args:
        image_path (str): The local path to the stored image.
    Returns:
        tuple: (merchant_name, total_amount)
    """
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Could not read image")

        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        float_pattern = r'\d+[.,]\d+'
        lines = {}

        for i in range(len(d['text'])):
            text = d['text'][i].strip()
            if text and int(d['conf'][i]) > 30:
                line_id = f"b{d['block_num'][i]}_l{d['line_num'][i]}"
                lines.setdefault(line_id, []).append(text)

        all_lines = [" ".join(words) for words in lines.values()]


        merchant_name = "Unknown"
        ignore_list = ["WELCOME", "RECEIPT",
                       "INVOICE", "CASHIER", "TEL", "ST#", "DATE"]

        for line in all_lines:
            if any(c.isalpha() for c in line) and not any(x in line.upper() for x in ignore_list):
                if not re.search(float_pattern, line):
                    merchant_name = line
                    break


        total_amount = 0.0
        found_prices = []
        total_keywords = ["TOTAL", "NET", "AMOUNT DUE", "PAYMENT"]

        for line in all_lines:
            line_upper = line.upper()
            matches = re.findall(float_pattern, line)

            for m in matches:
                val = float(m.replace(',', '.'))
                if any(key in line_upper for key in total_keywords):
                    total_amount = max(total_amount, val)
                found_prices.append(val)


        if total_amount == 0.0 and found_prices:
            total_amount = max(found_prices)

        return merchant_name, total_amount

    except Exception as e:
        print(f"Error: {e}")
        return "Unknown", 0.0
