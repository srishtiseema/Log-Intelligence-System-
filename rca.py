def perform_rca(df, preds):
    df["anomaly"] = preds
    
    anomalies = df[df["anomaly"] == -1]
    
    causes = anomalies["message"].value_counts()
    
    return causes