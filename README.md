Text-to-Image Model Inference on Edge Device:

Overview
This project enables users to generate images from text descriptions using a text-to-image generative model called stable-diffusion-v1-5. The model inference is performed locally on the user's machine, utilizing its GPU capability (CUDA or MPS). The application is containerized using Docker for easy deployment and utilizes Python, FastAPI, Gradio, Docker, Git, and Github technologies.
Features
* Local Inference: Run the model locally on your machine, leveraging the GPU for faster processing.
* User-friendly Interface: Access the model through a user-friendly Gradio frontend UI.
* Containerized Deployment: Deploy the application easily using Docker containers.
* Scalable: Can be scaled to handle multiple users concurrently.
* Modular Structure: Clean repository structure with separate backend and frontend components.
Repository Structure
text-to-image-webgpu/
├── compose-dev.yaml
├── docker-compose.yml
├── gradio_ui/
│   ├── Dockerfile.frontend
│   └── gradio_ui.py
├── main/
│   ├── Dockerfile.backend
│   └── main.py
└── requirements.txt


Usage
* 		Clone the Repository: Clone the repository to your local machine.
* 		Install Dependencies: Install the necessary dependencies by running pip install -r requirements.txt.
* 		Build Docker Containers: Use docker-compose to build the Docker containers defined in docker-compose.yml.
* 		Run the Application: Start the Docker containers using docker-compose up.
* 		Access the Application: Access the Gradio frontend UI via the provided URL to interact with the model.
Deployment
* 		Push to Github: Push your repository to Github for version control and easy deployment.
* 		Choose a Hosting Service: Deploy the application using a hosting service of your choice.
* 		Configure Environment Variables: Set any necessary environment variables required for your deployment.
* 		Deploy Containers: Deploy the Docker containers on your hosting service.
* 		Access the Application: Share the URL with users to access the model inference application.
Contributors
* Sagar Gupta
IT License.
