
# 🧪 Touch and User Classification from Smart Fabric

🎯 Goal: Classify different touch gestures and identify users based on smart fabric sensor data using Random Forest classifiers.

This project focuses on classifying **touch types** and **user identities** using sensor data collected from smart fabrics.  
By applying **Random Forest classifiers**, the project predicts either the type of touch or the user ID based on 3200 sensor features.  
It also provides **feature importance visualizations** and prepares the data for **outlier detection**.

---

## 📌 Project Overview

- **Touch Type Prediction:** Classifies different touch gestures based on sensor data.
- **User Identification:** Detects which user interacted with the fabric.
- **Feature Importance Analysis:** Visualizes the top 100 most significant sensor features.
- **Outlier Detection:** The code structure supports anomaly detection, but this feature is currently not active in the Streamlit interface.


---
## ⚙️ Technologies Used

## ⚙️ Technologies Used

| Technology                | Purpose                                       |
|----------------------------|----------------------------------------------|
| **Python 3.x**             | Core programming language                    |
| **Scikit-learn**           | Random Forest classifier for predictions     |
| **Pandas, NumPy**          | Data preprocessing and manipulation          |
| **Matplotlib**             | Feature importance and result visualizations |
| **Streamlit**              | Interactive web-based interface              |
| **Streamlit-option-menu**  | Sidebar navigation and menu selection within Streamlit |

---


## 📂 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BurakCANKURT/touch-user-classification.git
   cd touch-user-classification
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv

   # For Linux/Mac:
   source venv/bin/activate

   # For Windows:
   venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Run

```bash
streamlit run main.py
```

---

## 🖼️ Demo Screenshots

### 🟢 Menu Page (Project Overview):
![Menu Screenshot](./media/ss1.png)

### 🟡 Touch Parameter Visualization:
![Touch Prediction](./media/ss2.png)

### 🔵 User Parameter Visualization:
![User Prediction](./media/ss3.png)

---

## 📂 Project Structure

```
├── main.py                                # Streamlit app
├── touch_and_user_classification.py       # ML training and feature importance logic (not called in Streamlit)
├── models                                   # Visualizations
├── requirements.txt                      # Dependencies
├── README.md                              # Project description (this file)
├── 03-Touch and User Classification from Smart Fabric.xlsx  # Input data (if shared)                            # Touch Parameter Visualization Demo
└── media                            # Program Visualization Demo
```

---

## ⚠️ Notes

- The **PNG visualizations** are pre-generated and displayed directly.
- The **model training part is not triggered** from the Streamlit app. The app is designed for visualization only.

---

## 📌 What I Learned

- Handling high-dimensional sensor data (3200 features) for classification tasks.
- Applying Random Forest classifiers for multi-class prediction problems.
- Interpreting model results through feature importance visualizations.
- Designing modular ML pipelines by separating training logic from the interactive web interface.
- Using Streamlit and streamlit-option-menu to build user-friendly dashboards for machine learning results.

