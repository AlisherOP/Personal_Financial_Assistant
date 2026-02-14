# Personal Financial Assistant (OCR Expense Tracker)

An AI-powered Django application that automates expense tracking by extracting merchant names and total amounts from uploaded receipt images using Tesseract OCR and OpenCV.

## 🚀 Features
* **OCR Extraction:** Automated data entry from `.jpg`, `.png`, and `.webp` receipts.
* **Image Processing:** Uses OpenCV for thresholding and grayscale conversion to improve OCR accuracy.
* **User Dashboard:** Visual summary of spending habits and history.
* **Authentication:** Secure user accounts and private data storage.

## 🛠️ Tech Stack
* **Backend:** Django 6.0
* **Computer Vision:** OpenCV, PyTesseract (Tesseract OCR)
* **Database:** SQLite (Development)
* **Frontend:** Bootstrap 5

## 📦 Installation
1. Install Tesseract OCR on your system:
   `sudo apt install tesseract-ocr`
2. Clone the repo:
   `git clone https://github.com/yourusername/project-name.git`
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run migrations and start:
   `python manage.py migrate && python manage.py runserver`