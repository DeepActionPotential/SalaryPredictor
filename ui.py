import gradio as gr

def build_ui(model, predict_fn):
    with gr.Blocks() as demo:
        gr.Markdown("## 💼 Employee Salary Prediction")

        with gr.Row():
            gender = gr.Dropdown(choices=["Male", "Female"], label="Gender")
            department = gr.Dropdown(
                choices=["Engineering", "Sales", "Finance", "HR"], 
                label="Department"
            )
            job_title = gr.Dropdown(
                choices=["Engineer", "Executive", "Intern", "Analyst", "Manager"], 
                label="Job Title"
            )
            experience_years = gr.Number(label="Years of Experience")
            education_level = gr.Dropdown(
                choices=["Bachelor", "Master", "PhD"], 
                label="Education Level"
            )
            location = gr.Dropdown(
                choices=["Austin", "Seattle", "New York", "San Francisco"], 
                label="Location"
            )

        predict_btn = gr.Button("Predict Salary")
        output = gr.Textbox(label="Predicted Salary")

        predict_btn.click(
            fn=lambda *args: predict_fn(model, *args),
            inputs=[gender, department, job_title, experience_years, education_level, location],
            outputs=output
        )

    return demo
