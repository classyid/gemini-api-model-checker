# 🔍 Gemini API Model Checker

> **Tool lengkap untuk mengecek dan menggunakan Google AI API (Gemini, Veo2, Imagen) dengan panduan bahasa Indonesia**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Indonesian](https://img.shields.io/badge/Docs-Bahasa%20Indonesia-red.svg)](#)

## 🎯 Apa itu Gemini API Model Checker?

Tool ini membantu Anda:
- ✅ **Mengecek model mana saja** yang bisa diakses dengan API key Google AI Anda
- 🎬 **Generate video dengan Veo2** (model video AI terbaru Google)
- 📝 **Membuat script video** dengan Gemini untuk berbagai keperluan
- 💳 **Panduan setup billing** GCP untuk akses model premium
- 🔧 **Troubleshooting** masalah API dan quota

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install google-genai>=1.10.0
```

### 2. Dapatkan API Key
1. Kunjungi [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Login dengan akun Google
3. Buat API key baru
4. Copy API key tersebut

### 3. Jalankan Model Checker
```bash
git clone https://github.com/username/gemini-api-model-checker.git
cd gemini-api-model-checker
python3 api_model_checker.py
```

### 4. Masukkan API Key
Edit file `api_model_checker.py` dan ganti:
```python
os.environ['GOOGLE_API_KEY'] = "MASUKKAN_API_KEY_ANDA_DISINI"
```

## 📁 Struktur File

```
gemini-api-model-checker/
├── api_model_checker.py     # Script utama untuk cek model
├── veo2_video_generator.py  # Generator video dengan Veo2
├── gemini_script_maker.py   # Pembuat script video dengan Gemini
├── templates/               # Template offline
│   ├── video_script_template.md
│   └── storyboard_template.md
├── docs/                    # Dokumentasi lengkap
│   ├── setup_gcp_billing.md
│   ├── troubleshooting.md
│   └── tutorial_lengkap.md
└── README.md               # File ini
```

## 🔧 Fitur Utama

### 1. 🔍 Model Checker
Cek model apa saja yang bisa diakses:
```bash
python3 api_model_checker.py
```

**Output yang diharapkan:**
```
🎯 QUICK CHECK: POPULAR MODELS
========================================
🧪 gemini-1.5-flash
   📝 Most common free text model
   ✅ AVAILABLE

🧪 veo-2.0-generate-001
   📝 Latest video generation
   💳 NEEDS BILLING
```

### 2. 🎬 Veo2 Video Generator
Generate video AI dengan Veo2:
```bash
python3 veo2_video_generator.py
```

**Contoh prompt:**
```
"Close-up shot kucing lucu bermain dengan benang wol, pencahayaan hangat, style cinematic"
```

### 3. 📝 Gemini Script Generator
Buat script video dengan Gemini:
```bash
python3 gemini_script_maker.py
```

## 📊 Model yang Didukung

| Model | Jenis | Status | Kebutuhan |
|-------|--------|---------|-----------|
| `gemini-1.5-flash` | Text | ✅ Gratis | API Key |
| `gemini-2.0-flash` | Multimodal | ✅ Gratis | API Key |
| `imagen-3.0-generate-002` | Image | 💳 Berbayar | GCP Billing |
| `veo-2.0-generate-001` | Video | 💳 Berbayar | GCP Billing |
| `gemini-2.5-pro-preview` | Advanced | 💳 Berbayar | GCP Billing |

## 💳 Setup GCP Billing (untuk Model Premium)

Untuk mengakses Veo2 dan Imagen, perlu setup billing:

1. **Buka Google Cloud Console:** https://console.cloud.google.com/
2. **Setup Billing Account:** Menu Billing → Create billing account
3. **Masukkan kartu kredit** (dapat free credit $300 untuk akun baru)
4. **Link project** dengan billing account
5. **Enable Vertex AI API**

📖 **Panduan lengkap:** [docs/setup_gcp_billing.md](docs/setup_gcp_billing.md)

## 🎬 Contoh Penggunaan Veo2

```python
from veo2_generator import generate_video_from_text

# Generate video kucing lucu
result = generate_video_from_text(
    "Close-up shot seekor kucing orange bermain dengan bola benang, pencahayaan hangat, style cinematic",
    "kucing_lucu.mp4"
)

if result:
    print(f"✅ Video berhasil: {result}")
```

## 🔧 Troubleshooting

### Error "NEEDS BILLING"
**Solusi:** Setup GCP billing untuk akses model premium
- [Panduan setup billing](docs/setup_gcp_billing.md)

### Error "QUOTA LIMITED"  
**Solusi:** Tunggu 24 jam untuk reset quota, atau setup billing
- Free tier: 15 requests/menit
- Dengan billing: Quota lebih besar

### Error "API KEY INVALID"
**Solusi:** 
1. Cek API key sudah benar
2. Pastikan project memiliki akses Gemini API
3. Enable APIs yang diperlukan

📖 **Troubleshooting lengkap:** [docs/troubleshooting.md](docs/troubleshooting.md)

## 📋 Requirements

- **Python:** 3.7 atau lebih baru
- **Library:** `google-genai>=1.10.0`
- **API Key:** Google AI Studio API key
- **Billing:** GCP billing (untuk model premium)

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -am 'Tambah fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## 📄 Lisensi

MIT License - lihat file [LICENSE](LICENSE) untuk detail.

## 🙏 Kredit

- **Google AI** untuk Gemini API dan Veo2
- **Komunitas Indonesia** untuk feedback dan testing
- **Contributors** yang membantu pengembangan

## 📞 Kontak & Support

- 🐛 **Bug Report:** [Issues](https://github.com/username/gemini-api-model-checker/issues)
- 💬 **Diskusi:** [Discussions](https://github.com/username/gemini-api-model-checker/discussions)
- 📧 **Email:** your.email@example.com

## ⭐ Star Repository

Jika tool ini bermanfaat, jangan lupa star repository ini! ⭐

---

**Made with ❤️ untuk komunitas AI Indonesia**
