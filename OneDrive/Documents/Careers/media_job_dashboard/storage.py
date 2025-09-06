import pandas as pd

saved_jobs = []

def save_job(job):
    saved_jobs.append(job)

def export_csv():
    df = pd.DataFrame(saved_jobs)
    df.to_csv("saved_jobs.csv", index=False)
