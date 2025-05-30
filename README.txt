# Build the image
docker build -t file-downloader .

# Run the image and mount the volume, exposing on port 5000
docker run -v $(pwd)/shared:/files -p 5000:5000 file-downloader

# Example of calling API
curl http://localhost:5000/api/files

# Test command
python3 -m pytest tests/



# Initializing a local repository
git init

# Connecting local repo to the distant repo
git remote add origin git@github.com:dguasco-git/dockerized_flaskapp.git

# Verifying that connection went good
git remote -v

# First Commit
git add .
git commit -m "First commit"

# Git Push
git push -u origin main

