# VisionAsk 🔍 — Rasmdan Savol-Javob AI

> Amazon Nova AI Hackathon uchun yaratilgan loyiha

## 📌 Loyiha haqida

**VisionAsk** — foydalanuvchi istalgan rasm yuklashi va unga haqida savol berishi mumkin bo'lgan multimodal AI ilovasi. Amazon Nova Pro modeli rasmni tahlil qilib, aniq va batafsil javob beradi.

**Kategoriya:** Multimodal Understanding  
**Model:** Amazon Nova Pro v1 (via AWS Bedrock)

---

## 🚀 O'rnatish va ishga tushirish

### 1. Talablar
- Python 3.9+
- AWS akkaunt (Bedrock bilan)
- Amazon Nova Pro modeli yoqilgan bo'lishi kerak

### 2. O'rnatish

```bash
# Loyihani klonlash
git clone <repo-url>
cd image-qa-app

# Virtual muhit yaratish
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Kutubxonalarni o'rnatish
pip install -r requirements.txt
```

### 3. AWS sozlash

```bash
# AWS credentials sozlash
aws configure
# AWS Access Key ID: <your-key>
# AWS Secret Access Key: <your-secret>
# Default region: us-east-1
```

Yoki environment variables orqali:
```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_REGION=us-east-1
```

### 4. Ilovani ishga tushirish

```bash
python app.py
```

Brauzerda oching: `http://localhost:5000`

---

## 🎯 Ishlatish

1. Rasmni drag & drop qiling yoki bosib tanlang
2. Savolingizni kiriting (o'zbek yoki ingliz tilida)
3. "Tahlil qilish" tugmasini bosing
4. Nova Pro modeli rasmni tahlil qilib javob beradi

### Misol savollar:
- "Bu rasmda nima tasvirlangan?"
- "Rasmdagi matnni o'qib ber"
- "Bu qayerda olingan bo'lishi mumkin?"
- "Rasmni batafsil tasvirla"

---

## 🛠 Texnologiyalar

| Texnologiya | Maqsad |
|---|---|
| Amazon Nova Pro v1 | Multimodal AI tahlil |
| AWS Bedrock | Model hosting |
| Python / Flask | Backend server |
| HTML/CSS/JS | Frontend |
| Boto3 | AWS SDK |

---

## 📁 Loyiha tuzilishi

```
image-qa-app/
├── app.py              # Flask backend
├── requirements.txt    # Python kutubxonalari
├── README.md           # Hujjat
└── templates/
    └── index.html      # Frontend UI
```

---

## 🏆 Hackathon

**Amazon Nova AI Hackathon 2025**  
Kategoriya: Multimodal Understanding  
Deadline: 17 mart 2026

---

## 📄 Litsenziya

MIT License
