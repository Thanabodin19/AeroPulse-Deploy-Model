---
title: Docker Test
emoji: 💻
colorFrom: purple
colorTo: indigo
sdk: docker
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

Run backend
```bash
fastapi dev backend/main.py   
```

Run frontend
```bash
streamlit run frontend/visualizer.py 
```

Running the Docker Container:
After creating your Dockerfile, you can build and run the container:

Build the Docker image:
```bash
docker build -t aeropulse-app .
```
Run the Docker container:
```bash
docker run -p 8501:8501 -p 8000:8000 aeropulse-app
```
This will expose the Streamlit frontend on port 8501 and the FastAPI backend on port 8000.