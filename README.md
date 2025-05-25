# 🔍 Gemini API Model Checker

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Google AI](https://img.shields.io/badge/Google%20AI-Gemini-orange.svg)

Tool sederhana untuk mengecek kompatibilitas API key Google AI dengan berbagai model terbaru seperti **Gemini 2.5**, **Imagen 3**, **Veo 2**, dan lainnya.

## ✨ Fitur

- 🚀 **Quick Check** - Test model populer dalam hitungan detik
- 📊 **Comprehensive Check** - Test semua model yang tersedia
- 💳 **Billing Detection** - Deteksi model mana yang perlu GCP billing
- ⏳ **Quota Status** - Cek apakah quota sudah habis
- 📝 **Detailed Report** - Generate laporan lengkap dengan timestamp
- 🎯 **Model Categories** - Text, Image, Video, Audio & Embedding

## 🔧 Model yang Didukung

### 📝 Text Models
- ✅ Gemini 2.5 Flash/Pro (Terbaru)
- ✅ Gemini 2.0 Flash/Lite
- ✅ Gemini 1.5 Flash/Pro
- ✅ Legacy models

### 🖼️ Image Models  
- ✅ Imagen 3.0 (Terbaru)
- ✅ Gemini 2.0 Flash Image Generation
- ✅ Legacy Imagen models

### 🎬 Video Models
- ✅ Veo 2.0 (Terbaru)
- ✅ Legacy video models

### 🔊 Audio & Embedding
- ✅ Gemini Embedding
- ✅ Gemini 2.0 Flash Live
- ✅ Text embeddings

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install google-genai>=1.10.0
```

### 2. Setup API Key
Dapatkan API key dari [Google AI Studio](https://aistudio.google.com/app/apikey), lalu edit script:
```python
os.environ['GOOGLE_API_KEY'] = "YOUR_API_KEY_HERE"
```

### 3. Jalankan Script
```bash
python api_model_checker.py
```

### 4. Pilih Mode Testing
```
Select testing mode:
1. Quick check (popular models only)    # Cepat, test 5 model utama
2. Comprehensive check (all models)     # Lengkap, test semua model
```

## 📊 Sample Output

### Quick Check Mode
```
🎯 QUICK CHECK: POPULAR MODELS
========================================
🧪 gemini-1.5-flash
   📝 Most common free text model
   ✅ AVAILABLE

🧪 gemini-2.0-flash
   📝 Latest multimodal model
   ⏳ QUOTA LIMITED

🧪 imagen-3.0-generate-002
   📝 Latest image generation
   💳 NEEDS BILLING

🧪 veo-2.0-generate-001
   📝 Latest video generation
   💳 NEEDS BILLING

📊 QUICK SUMMARY:
✅ Available: 1
💳 Need billing: 2
⏳ Quota limited: 1
```

## 🔍 Status Legend

| Status | Keterangan |
|--------|------------|
| ✅ **AVAILABLE** | Model bisa digunakan langsung |
| 💳 **NEEDS BILLING** | Perlu setup GCP billing |
| ⏳ **QUOTA LIMITED** | Kena rate limit, tunggu reset |
| ❌ **ERROR/NOT FOUND** | Model tidak ditemukan atau error |

## 💡 Troubleshooting

### Problem: "NEEDS BILLING"
**Solution:** Setup Google Cloud Platform billing
1. Buka [Google Cloud Console](https://console.cloud.google.com/billing)
2. Create billing account dengan kartu kredit
3. Link project ke billing account
4. Dapatkan $300 free credit untuk akun baru

### Problem: "QUOTA LIMITED"  
**Solution:** 
- Tunggu 24 jam untuk quota reset
- Atau setup billing untuk quota lebih besar

### Problem: API Key Invalid
**Solution:**
- Pastikan API key dari [Google AI Studio](https://aistudio.google.com/app/apikey)
- Enable Gemini API di project
- Cek API key belum expired

## 📋 Requirements

- Python 3.7+
- google-genai>=1.10.0
- Google AI API key
- Internet connection

## 🤝 Contributing

1. Fork repository ini
2. Create feature branch (`git checkout -b feature/nama-fitur`)
3. Commit changes (`git commit -am 'Tambah fitur baru'`)
4. Push ke branch (`git push origin feature/nama-fitur`)
5. Create Pull Request

## 📄 License

MIT License - Silakan gunakan dan modifikasi sesuai kebutuhan.

## 🙏 Acknowledgments

- Google AI Team untuk Gemini API
- Community Python Indonesia
- Contributors dan testers

## 📞 Support

Jika ada pertanyaan atau masalah:
- 🐛 **Bug reports:** Create GitHub issue
- 💬 **Diskusi:** GitHub Discussions
- 📧 **Email:** [kontak@classy.id]

---

⭐ **Jika tool ini membantu, jangan lupa kasih star!** ⭐
