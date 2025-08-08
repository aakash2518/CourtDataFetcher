# Court Data Fetcher

A Python-based project for fetching case data from Indian court portals, storing it in a MySQL database, and displaying metadata.  
Currently configured for the Delhi High Court portal.

## 🎥 Project Demo
<video width="100%" controls>
  <source src="https://1drv.ms/v/c/12a8e1eb17907f73/IQSgvc65KOgAQ7l6IXVoV3hNARFK08qZ66a3jGkhPb3z1FQ?width=1920&height=1080" type="video/mp4">
  Your browser does not support the video tag.
</video>

> If the video doesn't play on GitHub, [click here to watch it directly](https://1drv.ms/v/c/12a8e1eb17907f73/IQSgvc65KOgAQ7l6IXVoV3hNARFK08qZ66a3jGkhPb3z1FQ?width=1920&height=1080).

---

## 📌 Features
- MySQL database connection via SQLAlchemy ORM.
- Customizable court target URL (currently set to Delhi High Court).
- Configurable Flask app settings for development.

## 🛠 Requirements
- Python 3.8+
- MySQL Server
- Required Python libraries:
  - `mysql-connector-python`
  - `SQLAlchemy`

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/court-data-fetcher.git
   cd court-data-fetcher
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure database**
   - Update `config.py` with your MySQL credentials.
   - Ensure the database exists.

4. **Run the app** (depending on your main script)
   ```bash
   python app.py
   ```

---

## ⚙ Configuration
`config.py` includes:
- **DB_CONFIG**: MySQL connection settings.
- **SQLALCHEMY_DATABASE_URI**: SQLAlchemy database URI.
- **COURT_URL**: Target court data URL.
- **DEBUG / SECRET_KEY**: Flask development settings.

---

## 📜 License
MIT License 
