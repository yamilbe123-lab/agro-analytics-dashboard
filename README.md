# AgroAnalytics Dashboard 🌱

Interactive agro-climatic monitoring and telemetry dashboard built with **Python**, **Streamlit**, and **Plotly**. Designed to consume telemetry data from the `agro-monitoring-core` RESTful backend and present real-time operational metrics.

## 🚀 Key Features

- **Live Sensor Telemetry:** Real-time data visualization for ambient temperature, relative humidity, and soil moisture.
- **RESTful Integration:** Communicates with Spring Boot backend endpoints via HTTP requests.
- **Data Persistence & Simulation:** Resilient fallback logic providing mock data streams if the backend service is offline.
- **Interactive Visualizations:** Built-in dynamic time-series charts powered by Plotly.

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Frontend / Dashboard Framework:** Streamlit
- **Data Processing & Visualization:** Pandas, Plotly Express
- **API Client:** Requests

## ⚙️ Local Setup

1. **Clone the repository:**
   \`\`\`bash
   git clone https://github.com/yamilbe123-lab/agro-analytics-dashboard.git
   cd agro-analytics-dashboard
   \`\`\`

2. **Create and activate a virtual environment:**
   \`\`\`bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\Activate.ps1
   \`\`\`

3. **Install dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run the dashboard:**
   \`\`\`bash
   streamlit run app.py
   \`\`\`