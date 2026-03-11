# VisionAsk 🔍 — Image Question-Answering AI

> Project created for the Amazon Nova AI Hackathon

---

## 📌 About the Project

**VisionAsk** is a multimodal AI application that allows users to upload any image and ask questions about it. The Amazon Nova Pro model analyzes the image and provides accurate and detailed answers.

**Category:** Multimodal Understanding  
**Model:** Amazon Nova Pro v1 (via AWS Bedrock)

---

## 🚀 Installation and Running

### 1. Requirements

- Python 3.9+
- AWS account (with Bedrock enabled)
- Amazon Nova Pro model access enabled

---

### 2. Installation

```bash
# Clone the project
git clone <repo-url>
cd image-qa-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
````

---

### 3. AWS Configuration

```bash
# Configure AWS credentials
aws configure
# AWS Access Key ID: <your-key>
# AWS Secret Access Key: <your-secret>
# Default region: us-east-1
```

Or using environment variables:

```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_REGION=us-east-1
```

---

### 4. Run the Application

```bash
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

## 🎯 Usage

1. Drag & drop an image or click to upload it
2. Enter your question (Uzbek or English)
3. Click the **Analyze** button
4. The Nova Pro model will analyze the image and return an answer

### Example questions

* What is shown in this image?
* Read the text in the image.
* Where might this photo have been taken?
* Describe the image in detail.

---

## 🛠 Technologies

| Technology              | Purpose                |
| ----------------------- | ---------------------- |
| Amazon Nova Pro v1      | Multimodal AI analysis |
| AWS Bedrock             | Model hosting          |
| Python / Flask          | Backend server         |
| HTML / CSS / JavaScript | Frontend               |
| Boto3                   | AWS SDK                |

---

## 📁 Project Structure

```
image-qa-app/
├── app.py              # Flask backend
├── requirements.txt    # Python dependencies
├── README.md           # Documentation
└── templates/
    └── index.html      # Frontend UI
```

---

## 🏆 Hackathon

**Amazon Nova AI Hackathon 2025**
Category: Multimodal Understanding
Deadline: **March 17, 2026**

---

## 📄 License

MIT License

```

Agar xohlasangiz, men yana **GitHub uchun kuchliroq README (badge, screenshot, demo GIF, architecture diagram bilan)** ham tayyorlab beraman. Bu hackathon va Devpost’da loyihani ancha professional ko‘rsatadi. 🚀
```
