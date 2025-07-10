# AI Software Solutions Assignment
# 🚀 AI in Software Engineering Assignment – Week 4

**Theme:** Building Intelligent Software Solutions  
**Course:** AI Tools and Applications  
**Author:** Alex Mwangi Mwaniki  
**Date:** July 2025

---

## 📌 Overview

This project showcases how AI tools can be integrated into modern software engineering workflows. It includes:

- ✅ AI-assisted code completion using GitHub Copilot
- 🔍 Automated testing with Selenium
- 📊 Predictive analytics using Random Forest
- 🧠 Ethical reflection using fairness principles

---

## 📂 Project Structure

```bash
AI_Software_Solutions_Assignment/
│
├── part1_theory/                     # Theoretical questions and DevOps case study
│   └── theory_answers.pdf
│
├── part2_implementation/            # Practical tasks
│   ├── task1_code_completion/       # Copilot vs manual sorting
│   ├── task2_automated_testing/     # Selenium login test script
│   └── task3_predictive_model/      # RandomForest on breast cancer data
│
├── part3_ethics/                    # Ethical reflection on model fairness
│   └── ethical_reflection.md
│
├── presentation/                    # 3-minute video demo and slides
│   ├── ai_demo_video.mp4
│   └── slides.pdf
│
├── requirements.txt                 # Python packages
├── LICENSE                          # MIT License
└── README.md                        # This file
🧪 How to Run the Code
▶️ Task 1: Code Completion
bash
Copy
Edit
cd part2_implementation/task1_code_completion
python sort_manual.py
python sort_copilot.py
🧪 Task 2: Automated Testing
Requires Chrome and Selenium installed

bash
Copy
Edit
cd part2_implementation/task2_automated_testing
python login_test.py
📈 Task 3: Predictive Model
bash
Copy
Edit
cd part2_implementation/task3_predictive_model
python breast_cancer_model.py
# or open breast_cancer_model.ipynb in Jupyter
📌 Make sure the breast_cancer.csv dataset is placed in this folder.

📦 Requirements
Install dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
Included Libraries:

pandas

scikit-learn

selenium

jupyter (optional for notebooks)

🤖 Ethical Considerations
The model is evaluated for fairness and potential bias using principles from IBM AI Fairness 360. Reflection and mitigation strategies are included in part3_ethics.