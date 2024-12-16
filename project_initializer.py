import os

# Function to read file content from templates
def read_template(template_name):
    template_path = os.path.join("templates", template_name)
    with open(template_path, "r") as file:
        return file.read()

# Define the project structure
project_structure = {
    "root_files": {
        "docker-compose.yml": "",
        "requirements.txt": "",
        "Makefile": read_template("Makefile"),
        "README.md": "",
        ".gitignore": "*.pyc\n__pycache__/\n.env",
        ".dockerignore": "*.pyc\n__pycache__/",
        ".env": "SECRET_KEY=your_secret_key"
    },
    "folders": {
        "fastapi": {
            "Dockerfile": read_template("Dockerfile"),
            "Makefile": "",
            "requirements.txt": read_template("fastapi.txt"),
            "app.py": read_template("fastapi_app.py")
        },
        "streamlit": {
            "Dockerfile": read_template("Dockerfile"),
            "Makefile": "",
            "requirements.txt": read_template("streamlt.txt"),
            "app.py": read_template("streamlit_app.py")
        },
        "db":{},
        
    }
}

# Remaining code for creating the structure remains the same
def create_project_structure(base_path, structure):
    for file_name, content in structure.get("root_files", {}).items():
        file_path = os.path.join(base_path, file_name)
        with open(file_path, "w") as file:
            file.write(content)

    for folder_name, files in structure.get("folders", {}).items():
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        for file_name, content in files.items():
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "w") as file:
                file.write(content)

# Main project path
base_path = "my_project"

# Create the project structure
os.makedirs(base_path, exist_ok=True)
create_project_structure(base_path, project_structure)

print(f"The project structure has been successfully created at: {base_path}")
