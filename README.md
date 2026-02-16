```markdown
# 🇧🇪 AI Study Buddy (Powered by Google Gemini)

This is a Python application that uses Google's Gemini AI to read PDF documents (like school notes or resumes) and answer questions about them.

## 🛠️ Prerequisites (What you need installed)

Before running the app, make sure you have:
1.  **VS Code** installed (The blue editor).
2.  **Python** installed (Check by typing `python --version` in your terminal).
3.  A **Google API Key** (Get it for free here: [Google AI Studio](https://aistudio.google.com/app/apikey)).

---

## 🚀 How to Run the App

### Step 1: Open the Project
1.  Open **VS Code**.
2.  Go to **File > Open Folder**.
3.  Select your `study-buddy` folder on your Desktop.

### Step 2: Install Tools (Only do this ONCE)
If you are on a new computer, run this command in the terminal to install the necessary libraries:
```bash
pip install streamlit google-generativeai PyPDF2

```

### Step 3: Start the App

1. Look at the bottom of VS Code for the **Terminal** (black box).
* *If you don't see it, click **Terminal > New Terminal** at the top.*


2. Type this exact command and press **Enter**:

```bash
python -m streamlit run app.py

```

### Step 4: Use the App

1. A web browser window will open automatically.
2. **Paste your Google API Key** in the sidebar on the left.
3. **Upload a PDF** (drag and drop it into the box).
4. Wait for the green "Success" message.
5. **Type a question** in the box (e.g., "Summarize this document").

---

## 🛑 How to Stop the App

To turn the app off:

1. Go back to the **Terminal** (black box) in VS Code.
2. Click inside the black box.
3. Press `Ctrl + C` on your keyboard.
4. You can now close VS Code.

---

## 📄 Project Details (For CV/Resume)

* **Project Name:** AI Study Buddy
* **Description:** A RAG (Retrieval-Augmented Generation) application that processes PDF documents and allows users to query them using natural language.
* **Tech Stack:** Python, Streamlit, Google Gemini Pro (LLM).

```

```