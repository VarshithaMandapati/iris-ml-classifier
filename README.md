# 🌸 Iris Flower Classification (Python + C + scikit-learn)

## 📌 Overview
This project demonstrates a **basic Machine Learning model** using the Iris dataset with **Python (scikit-learn)**, and integrates a simple **C program** for reading the model output.  
It is designed for beginners to understand how ML works while also showcasing cross-language integration.

## ⚙️ Tech Used
- **Python** (basic syntax, file handling)
- **scikit-learn** (ML library)
- **C** (basic file handling & display)

## 🚀 Workflow
1. Load and split the Iris dataset.
2. Train a **Decision Tree Classifier**.
3. Evaluate model accuracy.
4. Predict flower species from sample input.
5. Save results to a text file.
6. Use **C program** to read and display results.

## 📂 Project Structure
```
iris-ml-classifier/
│── iris_classifier.py     # ML model in Python
│── iris_display.c         # C program to read results
│── iris_output.txt        # Generated output file (created after running Python script)
│── requirements.txt       # Python dependency
│── .gitignore             # Ignore venv and cache
│── README.md              # Documentation
```

## ▶️ How to Run (Local)

### 1) Setup Python
- Install Python 3.9+
- Create a virtual environment:
  - Windows (PowerShell):
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```
  - macOS / Linux (bash):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
- Install dependency:
  ```bash
  pip install -r requirements.txt
  ```

### 2) Run the ML script
```bash
python iris_classifier.py
```
This will create `iris_output.txt` in the same folder.

### 3) Compile & run the C program
- Ensure you have a C compiler installed (e.g., `gcc`):
  - Windows: Install **MSYS2** or **MinGW-w64** for `gcc`
  - macOS: `xcode-select --install` (for `clang`, compatible with `gcc` commands)
  - Linux: `sudo apt-get install build-essential` (Debian/Ubuntu)
- Compile and execute:
  ```bash
  gcc iris_display.c -o iris_display
  ./iris_display
  ```

## ✅ Sample Output
```
=== Iris Classification Result ===
Model Accuracy: 1.0000
Predicted species: setosa
```

## 📤 Uploading to GitHub (Quick)
1. Create a new repository named `iris-ml-classifier`.
2. Click **Add file → Upload files**.
3. Drag and drop all the files from this folder, then **Commit changes**.
4. (Optional) Upload the provided ZIP directly and click **Extract** locally before pushing via Git.

## 📝 Notes
- If you only want to run the ML part, Python alone is enough.
- The C program is just to demonstrate basic file I/O and cross-language integration.
- Feel free to modify the sample input in `iris_classifier.py`.
