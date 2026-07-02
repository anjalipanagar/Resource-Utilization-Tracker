# Resource Utilization Tracker

A lightweight Streamlit application for real-time system monitoring and OS memory management simulation.

## Features

* Live CPU, Memory, and Disk Usage Monitoring
* Real-Time Performance Charts
* High Resource Usage Alerts
* Top Running Processes Analysis
* FIFO Page Replacement Simulator
* LRU Page Replacement Simulator
* Auto Refresh Every 2 Seconds

## Tech Stack

* Python 3
* Streamlit
* psutil
* pandas
* matplotlib

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/anjalipanagar/Resource-Utilization-Tracker.git
cd System_Resource_Monitor
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is unavailable:

```bash
pip install streamlit psutil pandas matplotlib
```

### 5. Run the Application

```bash
streamlit run app.py
```

Open the URL displayed in the terminal (usually `http://localhost:8501`).

## Project Structure

```text
System_Resource_Monitor/
├── app.py
├── requirements.txt
└── README.md
```

## Author

Anjali S Panagar
