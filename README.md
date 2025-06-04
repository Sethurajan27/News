# 📰 News Site Login Automation

Automates login for news websites using Selenium WebDriver.

## 🛠 Setup
1. Clone repository:
   ```bash
   git clone https://github.com/yourusername/news.git
   cd news
   ```

2. Configure environment:
   ```bash
   cp .env.example .env
   nano .env  # Add your actual credentials
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage
```bash
python -m src.news_login
```

## 📸 Screenshots
- Success: `screenshots/login_success.png`
- Failure: `screenshots/login_failed.png`

## ⚙️ GitHub Actions
Automatically runs on push:
1. Installs Chrome
2. Runs login test
3. Uploads screenshots as artifacts
