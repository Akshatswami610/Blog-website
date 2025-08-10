# 📝 Django Blog Website
A fully-featured, production-ready **blog platform** built with **Django 5.2**, designed for speed, scalability, and simplicity.  
Deployed seamlessly on **Render**, using **AWS S3** for media storage and **WhiteNoise** for static files.

---

## 🌐 Live Demo
🔗 **[Visit the live site](https://blog-website-3wu2.onrender.com)**

---

## ✨ Features
- 📰 **Dynamic Blog Management** — Create, edit, and delete posts from the admin panel.
- 🔑 **User Authentication** — Secure login, signup, and logout.
- 📱 **Responsive UI** — Optimized for desktop, tablet, and mobile.
- ☁ **Cloud Storage** — Media files stored on AWS S3.
- ⚡ **Fast Static File Delivery** — Served via WhiteNoise in production.
- 🔒 **Secure Configuration** — Environment variables handled with `python-decouple`.
- 🛠 **Production Ready** — Configured with Gunicorn for deployment.

---

## 🛠 Tech Stack
**Backend:** Django 5.2, Python 3.12  
**Database:** SQLite (development) / PostgreSQL (production-ready)  
**Cloud Storage:** AWS S3 with `django-storages`  
**Static Serving:** WhiteNoise  
**Image Processing:** Pillow  
**Deployment:** Render  

---

## 📦 Installation

### 1️⃣ Clone the Repository
    git clone https://github.com/yourusername/your-blog-repo.git
    cd your-blog-repo
    
### 2️⃣ Create and Activate Virtual Environment
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
    
### 3️⃣ Install Dependencies
    pip install -r requirements.txt
    
### 4️⃣ Environment Variables
### Create a .env file in the root directory:
    DEBUG=True
    SECRET_KEY=your_secret_key
    ALLOWED_HOSTS=localhost,127.0.0.1
    AWS_ACCESS_KEY_ID=your_aws_access_key
    AWS_SECRET_ACCESS_KEY=your_aws_secret_key
    AWS_STORAGE_BUCKET_NAME=your_bucket_name
    
### 5️⃣ Apply Database Migrations
    python manage.py migrate
    
### 6️⃣ Create Superuser
    python manage.py createsuperuser
    
### 7️⃣ Run Development Server
    python manage.py runserver
    
Your blog is now live at http://127.0.0.1:8000/ 🎉

---

## 🚀 Deployment on Render
Render runs these steps automatically:

### Build Command
    pip install -r requirements.txt
    
### Start Command
    python manage.py migrate && gunicorn Blog.wsgi:application --bind 0.0.0.0:$PORT
    
## Static & Media Files

- Static files served with WhiteNoise

- Media files stored on AWS S3

---

## 📂 Project Structure
<pre>
Blog/
│── blog/             # Main app with models, views, templates
│── Blog/             # Project settings, URLs, WSGI
│── static/           # Static assets
│── templates/        # HTML templates
│── manage.py         # Django CLI entry point
│── requirements.txt  # Python dependencies
│── .env              # Environment variables (not committed)
</pre>  

---

## 🤝 Contributing
1. Fork this repository
2. Create a new branch: git checkout -b feature-name
3. Make your changes and commit: git commit -m "Description of changes"
Push to your branch: git push origin feature-name
Open a Pull Request

---

## 📜 License
This project is licensed under the MIT License.




