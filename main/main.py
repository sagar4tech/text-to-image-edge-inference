# main.py (FastAPI server)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline
import torch

app = FastAPI()

# Load pretrained model
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id)

#pipe = pipe.to("cuda")
#pipe = pipe.to("mps")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/infer/")
async def infer(prompt_request: PromptRequest):
    prompt = prompt_request.prompt

    # Run model inference
    image = pipe(prompt).images[0]

    # Save the image locally (optional)
    image.save("output.png")

    # Return result
    return {"result": "Model inference successful", "image_url": "output.png"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)