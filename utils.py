import pandas as pd

def predict_salary(model, gender, department, job_title, experience_years, education_level, location):
    """
    Take user inputs, build a DataFrame, and run through the pipeline.
    """
    input_df = pd.DataFrame([{
        "Gender": gender,
        "Department": department,
        "Job_Title": job_title,
        "Experience_Years": experience_years,
        "Education_Level": education_level,
        "Location": location
    }])

    prediction = model.predict(input_df)[0]
    return round(prediction, 2)
