#!/bin/bash
pip install -r requirements.txt
streamlit run dashboard.py --server.port $PORT --server.enableCORS false
