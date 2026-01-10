import os
import sys
# Ensure the src directory is in the path so imports work on Hugging Face Spaces
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import gradio as gr
from mobile_selector.crew import MobileSelector
from dotenv import load_dotenv

# Load environment variables (API keys)
load_dotenv()

def compare_mobiles(mobile1, mobile2):
    """
    Runs the MobileSelector crew to compare two mobile phones.
    """
    inputs = {
        "mobile_1": mobile1,
        "mobile_2": mobile2
    }
    
    # Log the usage to the console (visible in Hugging Face Logs tab)
    print(f"🚀 USAGE TRACKER: User is comparing '{mobile1}' vs '{mobile2}'")

    try:
        # Run the crew
        # kickoff() returns a CrewOutput object
        crew_output = MobileSelector().crew().kickoff(inputs=inputs)

        # Access the outputs of specific tasks.
        # Based on tasks.yaml and crew.py order:
        # Task 1: collect_specs_task (Index 0) -> Comparison Table
        # Task 2: select_best_mobile_task (Index 1) -> Final Recommendation
        
        # We use .raw to get the raw string output of the task
        comparison_result = crew_output.tasks_output[0].raw
        selection_result = crew_output.tasks_output[1].raw

        return comparison_result, selection_result

    except Exception as e:
        return f"Error: {str(e)}", ""

# Define the Gradio Interface
with gr.Blocks(title="Mobile Selector Agent") as iface:
    gr.Markdown("# Mobile Selector Agent")
    gr.Markdown("Enter two mobile phone models to generate a technical comparison and a buying recommendation.")
    
    with gr.Row():
        mobile1 = gr.Textbox(label="Mobile 1", placeholder="e.g. Samsung Galaxy S23 Ultra")
        mobile2 = gr.Textbox(label="Mobile 2", placeholder="e.g. iPhone 15 Pro Max")
    
    compare_btn = gr.Button("Compare Mobiles", variant="primary")
    
    gr.Markdown("### <u>Comparison Table</u>")
    output_comparison = gr.Markdown()
    gr.Markdown("### <u>Final Recommendation</u>")
    output_recommendation = gr.Markdown()

    #compare_btn.click(fn=compare_mobiles, inputs=[mobile1, mobile2], outputs=[output_comparison, output_recommendation])

    compare_btn.click(
        fn=lambda: gr.update(interactive=False),
        outputs=compare_btn,
        queue=False
    ).then(
        fn=compare_mobiles, 
        inputs=[mobile1, mobile2], 
        outputs=[output_comparison, output_recommendation]
    ).then(
        fn=lambda: gr.update(interactive=True),
        outputs=compare_btn
    )

if __name__ == "__main__":
    iface.launch()