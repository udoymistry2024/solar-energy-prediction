<div align="center">

# ☀️ Solar Energy Prediction Dashboard

### XGBoost মেশিন লার্নিং মডেল দ্বারা চালিত সোলার এনার্জি প্রেডিকশন সিস্টেম

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![XGBoost](https://img.shields.io/badge/XGBoost-3.2-F97316?style=for-the-badge)](https://xgboost.readthedocs.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7-F89939?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

<br>

**আবহাওয়া ইনপুটের ওপর ভিত্তি করে সোলার এনার্জি (Wh) উৎপাদনের পূর্বাভাস দেয়।**
**তিনটি মডেল তুলনা করে সবচেয়ে সঠিক XGBoost মডেলকে ডিপ্লয় করা হয়েছে।**

</div>

---

## 📋 সংক্ষিপ্ত বিবরণ (Overview)

এই প্রজেক্টটি একটি **End-to-End Machine Learning Pipeline** — ডেটা ক্লিনিং থেকে শুরু করে মডেল ট্রেনিং, ইভ্যালুয়েশন এবং Flask ওয়েব অ্যাপ্লিকেশনে ডিপ্লয়মেন্ট পর্যন্ত সম্পূর্ণ প্রক্রিয়া অন্তর্ভুক্ত। সোলার প্যানেলের শক্তি উৎপাদন বিভিন্ন আবহাওয়ার ফ্যাক্টরের (তাপমাত্রা, আর্দ্রতা, বায়ুচাপ, মেঘের পরিমাণ ইত্যাদি) ওপর নির্ভর করে — এই মডেলটি সেই সম্পর্ক শিখে ভবিষ্যতের এনার্জি উৎপাদন প্রেডিক্ট করে।

### 🎯 প্রজেক্টের উদ্দেশ্য

- আবহাওয়ার ডেটা বিশ্লেষণ করে সোলার এনার্জি উৎপাদন প্রেডিক্ট করা
- তিনটি ভিন্ন ML অ্যালগরিদম তুলনা করে সেরাটি নির্বাচন করা
- প্রডাকশন-রেডি ওয়েব ড্যাশবোর্ড তৈরি করা

---

## 🏆 মডেল পারফরম্যান্স (Model Performance)

তিনটি রিগ্রেশন মডেল ট্রেন ও তুলনা করা হয়েছে:

| মডেল | Train Score | Test Score (R²) | RMSE (Wh) | ওভারফিটিং |
|:---|:---:|:---:|:---:|:---:|
| Linear Regression | 85.62% | 85.97% | 393.17 | ❌ নেই |
| Random Forest | — | 93.19% | 273.91 | ❌ নেই |
| **✅ XGBoost (Final)** | **94.74%** | **93.58%** | **266.05** | **❌ নেই (Gap: 1.16%)** |

> **🏅 চূড়ান্ত মডেল:** XGBoost — সর্বোচ্চ accuracy এবং সবচেয়ে কম RMSE-এর কারণে এটিকে ডিপ্লয় করা হয়েছে। Training ও Test Score-এর মধ্যে মাত্র **1.16%** পার্থক্য প্রমাণ করে মডেলটি **overfitting-মুক্ত** ও অত্যন্ত ব্যালেন্সড।

---

## 🚀 ফিচারসমূহ (Features)

- ⚡ **Real-time Prediction** — আবহাওয়ার ডেটা দিয়ে তাৎক্ষণিক সোলার এনার্জি প্রেডিকশন
- 🧠 **XGBoost ML Model** — Hyperparameter-tuned XGBoost Regressor (n_estimators=280, max_depth=6)
- 📊 **Model Performance Dashboard** — ড্যাশবোর্ডে Training/Test Score, RMSE, R² দেখানো হয়
- 🎨 **Premium Dark UI** — Glassmorphism, animated gradients, floating particles সহ আধুনিক ডিজাইন
- 📱 **Fully Responsive** — ডেস্কটপে Full-screen (no scroll), মোবাইলে comfortable scrollable layout
- 🔒 **Input Validation** — সার্ভার-সাইড ইনপুট যাচাই ও error handling

---

## 📂 প্রজেক্ট স্ট্রাকচার (Project Structure)

```
Solar-Energy-Prediction/
│
├── 📄 app.py                      # Flask অ্যাপ্লিকেশন (Main Entry Point)
├── 📓 final_exam.ipynb             # সম্পূর্ণ ML Pipeline (EDA → Model → Evaluation)
├── 📊 solar_weather.csv            # আবহাওয়া ডেটাসেট (~15MB, 14+ features)
├── 🤖 xgboost_solar_model.pkl      # ট্রেনড XGBoost মডেল (Serialized)
├── ⚙️ solar_data_scaler.pkl        # StandardScaler (Feature Scaling)
├── 📋 requirements.txt             # Python Dependencies
├── 📖 README.md                    # এই ফাইল
│
└── templates/
    └── 🌐 index.html               # ওয়েব ড্যাশবোর্ড (Responsive UI)
```

---

## 🛠️ ইনস্টলেশন ও সেটআপ (Installation & Setup)

### পূর্বশর্ত (Prerequisites)

- Python 3.10 বা তার উপরে
- pip (Python Package Manager)
- Git

### ধাপে ধাপে সেটআপ

**1. রিপোজিটরি ক্লোন করুন:**
```bash
git clone https://github.com/<your-username>/Solar-Energy-Prediction.git
cd Solar-Energy-Prediction
```

**2. ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন:**
```bash
python -m venv venv

# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

**3. ডিপেন্ডেন্সি ইনস্টল করুন:**
```bash
pip install -r requirements.txt
```

**4. অ্যাপ্লিকেশন চালু করুন:**
```bash
python app.py
```

**5. ব্রাউজারে যান:**
```
http://127.0.0.1:5000
```

---

## 📊 ML Pipeline বিবরণ (Analysis Pipeline)

`final_exam.ipynb` নোটবুকে নিম্নলিখিত ধাপগুলো সম্পন্ন করা হয়েছে:

### Step 1: Data Loading & Exploration
- `solar_weather.csv` ডেটাসেট লোড করা
- Shape, dtypes, missing values, duplicate check

### Step 2: Data Cleaning & Preprocessing
- Missing values হ্যান্ডেল করা
- Feature selection ও engineering
- `StandardScaler` দিয়ে feature scaling
- Train-Test Split

### Step 3: Model Training & Comparison
তিনটি মডেল ট্রেন ও তুলনা করা হয়েছে:

| # | মডেল | বিবরণ |
|:---:|:---|:---|
| 1 | **Linear Regression** | বেসলাইন মডেল — সরলরৈখিক সম্পর্ক ধরার জন্য |
| 2 | **Random Forest** | Tree-based ensemble — নন-লিনিয়ার প্যাটার্ন ধরতে |
| 3 | **XGBoost** | Gradient Boosting — সবচেয়ে শক্তিশালী ও সঠিক |

### Step 4: Model Evaluation
- R² Score, RMSE দিয়ে মডেল মূল্যায়ন
- Overfitting check (Train vs Test gap analysis)
- চূড়ান্ত মডেল নির্বাচন: **XGBoost**

### Step 5: Model Deployment
- `joblib` দিয়ে মডেল ও scaler সেভ
- Flask API তৈরি ও ওয়েব ইন্টারফেস ডিপ্লয়

---

## 🔧 ইনপুট ফিচারসমূহ (Input Features)

মডেলটি নিম্নলিখিত আবহাওয়ার ফিচারগুলো ইনপুট হিসেবে নেয়:

| ফিচার | বিবরণ |
|:---|:---|
| `GHI` | Global Horizontal Irradiance (সৌর বিকিরণ) |
| `Temp` | তাপমাত্রা (°C) |
| `Pressure` | বায়ুচাপ (hPa) |
| `Humidity` | আপেক্ষিক আর্দ্রতা (%) |
| `Wind_speed` | বাতাসের গতি (m/s) |
| `Rain_1h` | ঘণ্টাপ্রতি বৃষ্টিপাত (mm) |
| `Snow_1h` | ঘণ্টাপ্রতি তুষারপাত (mm) |
| `Clouds_all` | মেঘের পরিমাণ (%) |
| `IsSun` | সূর্যের আলো আছে কিনা (0/1) |
| `SunlightTime` | দিনের সূর্যালোকের সময়কাল |
| `DayLength` | দিনের দৈর্ঘ্য (seconds) |
| `Weather_type` | আবহাওয়ার ধরণ (encoded) |
| `Hour` | ঘণ্টা (0-23) |
| `Month` | মাস (1-12) |
| `Temp_humidity` | তাপমাত্রা × আর্দ্রতা (engineered feature) |
| `Is_peak_hour` | পিক আওয়ার কিনা (0/1) |

---

## 🖥️ প্রযুক্তি স্ট্যাক (Tech Stack)

| ক্যাটাগরি | প্রযুক্তি |
|:---|:---|
| **Language** | Python 3.10+ |
| **ML Framework** | scikit-learn 1.7, XGBoost 3.2 |
| **Web Framework** | Flask 3.1 |
| **Data Processing** | Pandas 2.3, NumPy 2.2 |
| **Visualization** | Matplotlib 3.10, Seaborn 0.13 |
| **Model Serialization** | Joblib |
| **Frontend** | HTML5, CSS3 (Glassmorphism Dark Theme) |
| **Font** | Google Fonts (Inter) |

---

## 📸 স্ক্রিনশট (Screenshots)

> স্ক্রিনশট যোগ করুন — ড্যাশবোর্ডের ডেস্কটপ ও মোবাইল ভিউ দেখাতে।

```
<!-- ডেস্কটপ ভিউ -->
![Dashboard Desktop View](https://drive.google.com/file/d/1Vx_CcaX83DYO_rnnO46pDeRkoWZ-jDb7/view?usp=drive_link)

<!-- মোবাইল ভিউ -->
![Dashboard Mobile View](screenshots/mobile.png)
```

---

## 🤝 অবদান রাখুন (Contributing)

এই প্রজেক্টে অবদান রাখতে চাইলে:

1. রিপোজিটরি **Fork** করুন
2. নতুন ব্রাঞ্চ তৈরি করুন: `git checkout -b feature/your-feature`
3. পরিবর্তন কমিট করুন: `git commit -m "Add your feature"`
4. ব্রাঞ্চে পুশ করুন: `git push origin feature/your-feature`
5. **Pull Request** তৈরি করুন

---

## 📄 লাইসেন্স (License)

এই প্রজেক্টটি [MIT License](LICENSE) এর অধীনে লাইসেন্সকৃত।

---

<div align="center">

**তৈরি করেছেন ❤️ দিয়ে — Solar Energy Prediction Project © 2026**

⭐ যদি এই প্রজেক্টটি ভালো লাগে, তাহলে একটি **Star** দিন!

</div>
