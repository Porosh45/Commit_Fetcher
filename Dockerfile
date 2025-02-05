# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the script into the container
COPY github_commit_checker.py /app/script.py

# Install required Python packages
RUN pip install requests

# Set environment variables (optional, can be overridden at runtime)
ENV GITHUB_REPO=torvalds/linux

# Run the script when the container starts
CMD ["python", "script.py"]
