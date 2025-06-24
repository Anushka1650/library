# 📚 Library Management System

A web-based Library Management System built using **Python (Flask)** and deployed on **Vercel**. This project allows users to browse, borrow, donate, and return books efficiently using a simple and clean interface.

---

## ✨ Features

- 🏠 Home page with navigation
- 📖 View all available books
- ➕ Donate books to the library
- 🧾 Borrow and return books
- 🔍 Track borrowed books
- 🗃️ SQLite database to manage book records
- 🎨 Responsive frontend using HTML & CSS
- 🌐 Deployable on Vercel (with `vercel.json`)

---

## 🔧 Tech Stack

| Layer        | Technology        |
|--------------|-------------------|
| Backend      | Python (Flask)    |
| Frontend     | HTML, CSS, Jinja2 |
| Database     | SQLite            |
| Deployment   | Vercel            |

---

## 🛠️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Anushka1650/library.git
   cd library


Create a Virtual Environment

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Application Locally

bash
Copy
Edit
python app.py
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000/
📁 Project Structure
pgsql
Copy
Edit
library/
├── app.py
├── library.db
├── requirements.txt
├── .gitignore
├── vercel.json
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── books.html
│   ├── borrow.html
│   ├── donate.html
│   ├── return.html
│   ├── track.html
│   └── add.html
├── static/
│   └── styles.css
└── .vercel/
    ├── README.txt
    └── project.json
🖼️ Screenshots
You can add screenshots here after running the app locally to show off the UI.

🚀 Deployment (Vercel)
Make sure your vercel.json is present in the root.

Connect your GitHub repo to Vercel.

Set the build command (if needed):

bash
Copy
Edit
pip install -r requirements.txt && python app.py
Set FLASK_APP=app.py in environment variables (if required).

Deploy and go live!

📜 License
This project is licensed under the MIT License – feel free to use, modify, and distribute.

👩‍💻 Author
Anushka
🔗 GitHub

🌟 Show Your Support
If you like this project, give it a ⭐ on GitHub!

yaml
Copy
Edit

---

Let me know if you'd like me to add:
- Badges (build, license, last commit, etc.)
- A contributor section
- An API documentation table  
or convert it to **FastAPI** version later.








