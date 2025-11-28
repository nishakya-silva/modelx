# 🇱🇰 ModelX: Strategic Situational Awareness Platform

> *Real-time business intelligence for the Sri Lankan economic landscape.*

## Overview
**ModelX** is a real-time situational awareness platform designed to help Sri Lankan businesses navigate volatility. By aggregating signals from local news and social media, the system identifies operational risks (e.g., fuel shortages, strikes, regulatory changes) and automatically maps them to specific industries and actionable business strategies.

### The Problem
Sri Lankan businesses operate in a highly dynamic environment where events like power cuts, policy shifts, or public unrest can disrupt operations overnight. [cite_start]Decision-makers often lack a single, consolidated view of these emerging threats[cite: 26, 27].

### The Solution
ModelX filters the noise of the internet to provide:
1.  **Risk Detection:** Instantly flags high-impact keywords (e.g., "Strike", "Curfew").
2.  **Industry Tagging:** Categorizes news into 14 sectors (Agriculture, Logistics, Tech, etc.).
3.  **Actionable Advice:** Provides strategic recommendations (e.g., "Activate WFH protocols") based on detected risks.

---

## Key Features
* **Real-Time News Scraping:** Monitors major local news portals for breaking headlines.
* **Social Sentiment Analysis:** Tracks trending public discussions on platforms like Reddit (r/srilanka) to gauge public sentiment.
* **Smart Signal Processor:** Uses keyword logic to classify events by **Industry**, **Location**, and **Timeline** (Past/Future).
* **Decision Support System:** Automatically suggests mitigation strategies (e.g., securing diesel backup during fuel alerts).
* **Interactive Dashboard:** A clean, scannable interface built with Streamlit for immediate insight.

---

## Technology Stack
* **Frontend:** Streamlit (Python)
* **Data Acquisition:** BeautifulSoup4 (Web Scraping), Feedparser (RSS)
* **Data Processing:** Python (Pandas, RegEx)
* **Compatibility:** Windows/Linux/macOS

---

### Prerequisites
* Python 3.8 or higher installed.


