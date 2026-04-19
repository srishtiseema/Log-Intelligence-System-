import streamlit as st
from parser_1 import parse_logs
from model import train_model, detect_anomalies
from rca import perform_rca

st.title("Log Intelligence System")

df = parse_logs("logs/system.log")

model, vectorizer = train_model(df["message"])
preds = detect_anomalies(model, vectorizer, df["message"])

df["anomaly"] = preds

st.subheader("Log Data")
st.write(df)

st.subheader("Anomalies Detected")
st.write(df[df["anomaly"] == -1])
st.subheader("Root Cause Analysis")
rca = perform_rca(df, preds)
st.write(rca)