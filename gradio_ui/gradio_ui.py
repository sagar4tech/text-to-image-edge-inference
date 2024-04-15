import requests
import gradio as gr

def inference(prompt):
    # Define the URL of the FastAPI server
    api_url = "http://localhost:8000/infer/"

    # Define the input data (prompt) as a dictionary
    data = {"prompt": prompt}

    try:
        # Make a POST request to the FastAPI server
        response = requests.post(api_url, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the result from the response
            result = response.json()
            image_url = result.get("image_url")
            return image_url
        else:
            # If the request was not successful, return an error message
            return "Error: Failed to get result from server"
    except Exception as e:
        # Handle any exceptions that occur during the request
        return f"Error: {str(e)}"

    
    

if __name__ == "__main__":
    # Create and launch the Gradio interface
    iface = gr.Interface(fn=inference, inputs="text", outputs="image", title="Model Inference")
    iface.launch()

