# 🏡 Bangalore House Price Prediction

An end-to-end machine learning web application that predicts real estate prices in Bangalore, India — built with Flask, deployed using Gunicorn & NGINX on AWS EC2.

---

## 📌 Table of Contents
- [🔍 Overview](#-overview)
- [📦 Tech Stack](#-tech-stack)
- [⚙️ Project Structure](#️-project-structure)
- [📊 ML Model](#-ml-model)
- [🌐 Deployment Details](#-deployment-details)
- [🚀 Getting Started](#-getting-started)
- [🛠 Features](#-features)
- [📈 Future Enhancements](#-future-enhancements)
- [🙌 Acknowledgements](#-acknowledgements)

---

## 🔍 Overview

This project provides instant house price estimates based on:
- Location (dropdown)
- Total square feet
- Number of bedrooms (BHK)
- Number of bathrooms

Users enter the details via a clean UI, and predictions are returned instantly via a Flask-based REST API powered by a trained regression model.

---

## 📦 Tech Stack

| Layer         | Technology                            |
|---------------|----------------------------------------|
| 📈 ML Model   | scikit-learn, pandas                   |
| 🧠 Backend    | Python, Flask, Gunicorn                |
| 🎨 Frontend   | HTML, CSS, Bootstrap, jQuery, AJAX     |
| 🌍 Deployment | AWS EC2 (Ubuntu), NGINX, systemd       |
| 🔐 Tools      | Postman, Git, Chrome DevTools, SSH     |

---

## ⚙️ Project Structure

BHP/
├── server/                  # Backend
│   ├── server.py            # Flask app 
│   ├── util.py              # Prediction logic
│   └── artifacts/           # Trained model + columns.json
├── client/                  # Frontend
│   ├── app.html             # Front-End main file
│   ├── app.js
│   └── app.css
├── venv/                    # Python virtual environment

BHP/
├── client/                  # Frontend
│   ├── app.html             # Front-End main file ✅
│   ├── app.js
│   └── app.css
├── server/                  # Backend
│   ├── server.py            # Flask app ✅
│   ├── util.py              # Prediction logic
│   └── artifacts/
│       ├── banglore_home_prices_model.pickle
│       └── columns.json
├── requirements.txt
├── render.yaml
├── venv/                    # Python virtual environment

---

## 📊 ML Model

- **Model**: Linear Regression
- **Inputs**: total_sqft, bhk, bath, location
- **Libraries**: scikit-learn, pandas
- **Artifacts**: `bangalore_home_prices_model.pickle`, `columns.json`

---

## 🌐 Deployment Details

| Component       | Stack                                 |
|-----------------|----------------------------------------|
| App Hosting     | AWS EC2 (Ubuntu 22.04)                |
| Backend Server  | Gunicorn (via systemd service)        |
| Web Server      | NGINX (reverse proxy)                 |
| Frontend Path   | `/home/ubuntu/BHP/client/`            |
| Backend Port    | `127.0.0.1:8000` via Gunicorn         |
| Public URL      | `http://<your-ec2-ip>`                |

### 🔁 Route Mapping

| URL Route              | Purpose                        |
|------------------------|--------------------------------|
| `/`                    | Serves `app.html` (homepage)   |
| `/get_location_names` | Returns list of locations      |
| `/predict_home_price` | Returns predicted price        |

---

## 🚀 Getting Started (on EC2)

### 🧰 Install Tools
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx git -y
