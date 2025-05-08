# ✉️ Cover Letter Generator (Streamlit + Azure OpenAI)

A smart, AI-powered tool to generate personalized and impactful cover letters using your uploaded resume and job details. Built using Streamlit and Azure OpenAI.

---

## 🚀 Features

- Upload your **PDF resume**
- Auto-extract education, skills, work experience, projects, and certifications
- Customize tone, job role, and target company
- Instantly generate a well-structured, professional cover letter
- Built with `Streamlit`, `AzureOpenAI`, and `PyMuPDF`

---

## 🛠️ Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/your-username/cover-letter-generator.git
cd cover-letter-generator
```

### 2. (Optional but recommended) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate
```

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Copy the example environment file:
```bash
cp .env.example .env
```
Then edit the .env file and add your Azure OpenAI credentials:
```env
AZURE_OPENAI_API_KEY=your-real-api-key
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
OPENAI_API_VERSION=2023-12-01-preview
DEPLOYMENT_NAME=your-deployment-name
```

### ▶️ Run the Application
```bash
streamlit run main.py
```
This will launch the app in your browser.

### 📁 Project Structure
```bash
.
├── main.py              # Streamlit front-end for user input and UI
├── backend.py           # PDF parsing + Azure OpenAI communication
├── requirements.txt     # Python dependencies
├── .env.example         # Sample environment variable file
├── .gitignore           # Git ignore rules for sensitive files
```

---

## ✍️ Author
- Created by [Aiman Zaharin](linkedin.com/in/aimanzaharin)





