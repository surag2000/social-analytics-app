# 📊 Social Media Analytics Dashboard

A web app that tracks and visualizes social media performance across LinkedIn, Instagram, Twitter/X, and Facebook — built with Python and Streamlit.

**Live App:** [social-analytics-app.streamlit.app](https://surag2000-social-analytics-app.streamlit.app)  
**Built by:** Surag V V — BCA Data Science Final Year Project

---

## What It Does

Upload your social media CSV data and instantly get:

- Summary metrics — total posts, likes, reach, and average engagement rate
- Likes by platform bar chart
- Engagement trends over time line chart
- Reach vs impressions scatter plot
- Engagement rate calculated automatically for every post
- Best performing post highlighted
- Best day to post analysis

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Core language |
| Pandas | Data processing |
| Plotly | Interactive charts |
| Streamlit | Web app framework |
| GitHub | Version control |
| Streamlit Cloud | Deployment |

---

## Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/surag2000/social-analytics-app.git
cd social-analytics-app
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

---

## CSV Format

Upload a CSV file with these columns:

```
date, platform, post_type, likes, comments, shares, reach, impressions
```

Example:
```
2024-01-01,LinkedIn,image,130,15,30,1500,2000
2024-01-02,Instagram,reel,340,45,80,4500,6000
```

If no file is uploaded, the app loads built-in sample data automatically.

---

## Features

- **CSV Upload** — upload any platform's exported data (max 5MB)
- **Platform Filter** — sidebar filter updates all charts instantly
- **Engagement Rate** — auto-calculated as `(likes + comments + shares) / reach × 100`
- **Best Post** — highlights the post with the highest engagement rate
- **Best Day** — shows which day of the week drives most engagement
- **File Validation** — checks required columns and file size before processing

---

## Project Structure

```
social-analytics-app/
├── app.py               # Main application
├── sample_data.csv      # Built-in sample dataset
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## Real World Use

This app was built to solve a real problem — managing social media reporting for [STYAVA.dev](https://styava.dev), a developer community with 87,000+ members across India and APAC. Instead of logging into each platform separately and calculating metrics manually in Excel, this app does it in seconds.

---

## Author

**Surag V V**  
Community Manager @ STYAVA.dev  