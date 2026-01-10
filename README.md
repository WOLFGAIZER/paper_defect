
# 📄 Automated Paper Quality Inspection System

## 📌 Project Overview
This repository contains a **Computer Vision-based Quality Inspection System** designed to detect, localize, and classify defects on paper surfaces in real-time. Developed as part of the **Sapien Robotics AI Vision Intern Assignment (Task 2)**.

The system processes images of paper sheets to identify common manufacturing defects, providing precise coordinates and severity assessments to automate quality control.

---

## 🚀 Key Features
- **Defect Detection:** Automatically identifies defect regions using image processing techniques.
- **Multi-Class Classification:** Distinguishes between 3 distinct defect types:
  1.  **Tear / Cut** (Physical damage to the structure)
  2.  **Oil/Ink Stain** (Discoloration)
  3.  **Wrinkle / Fold** (Surface texture irregularity)
- [cite_start]**Precise Localization:** Outputs Bounding Boxes and `(x, y)` centroid coordinates for every detected defect[cite: 221, 223].
- [cite_start]**Severity Assessment:** Calculates defect severity based on area and pixel intensity.

---

## 🛠️ Methodology
The solution leverages **OpenCV** for efficient, offline image analysis without heavy deep learning dependencies, ensuring high-speed processing suitable for manufacturing lines.

1.  **Preprocessing:** Grayscale conversion, Gaussian Blurring, and Adaptive Thresholding to isolate anomalies.
2.  **ROI Extraction:** Contour detection logic filters out noise and identifies potential defect regions.
3.  **Classification Logic:**
    - **Stains:** Detected via color thresholding (HSV analysis).
    - **Tears:** Identified by analyzing contour jaggedness and convexity defects.
    - **Wrinkles:** Detected using Canny edge detection on texture gradients.
4.  **Output Generation:** Draws bounding boxes and overlays data on the final image.

---

## 📂 Repository Structure
```text
paper_defect/
├── input_images/          # Raw images of defective papers
│   ├── defect_tear.jpg
│   ├── defect_stain.jpg
│   └── defect_wrinkle.jpg
├── output_results/        # Processed images with bounding boxes
│   ├── result_tear.jpg
│   └── ...
├── main.py                # Core defect detection script
├── requirements.txt       # Dependencies
└── README.md              # Documentation
