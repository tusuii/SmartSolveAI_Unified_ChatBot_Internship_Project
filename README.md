# SmartSolveAI Unified ChatBot Internship Project

<center>
<img src="https://github.com/tusuii/SmartSolveAI_Unified_ChatBot_Internship_Project/blob/main/ngrok/WhatsApp-BOT-Image-2_2.gif" width="200" height="150">
</center>

---
## demo on actual devices

![gif video](https://github.com/tusuii/SmartSolveAI_Unified_ChatBot_Internship_Project/blob/main/ezgif.com-video-to-gif.gif)

## Table of Contents
- [Background](#background)
- [Project Overview](#project-overview)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Docker](#docker)
- [script install](#assumptions)
- [Functional Requirements](#functional-requirements)
- [Non-Functional Requirements](#non-functional-requirements)
- [External Interface Requirements](#external-interface-requirements)
- [Technology Used](#technology-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Background
As a part of the Industry Academia community (IAC) activities, many students and freshers participate in an online internship program (IP) every year to become job-ready. This project aims to provide a smart chatbot application using AI technologies to assist these students by answering their queries in real-time.

## Project Overview
The smart chatbot leverages AI technologies to provide seamless and intelligent interactions, enhancing user engagement and automating customer support processes. It integrates with various platforms and messaging services for a comprehensive user experience.

## Hardware Requirements
- Personal computer or mobile phone to test the application.

## Software Requirements
- RASA
- Twilio
- Ngrok
- Python and Python libraries for NLP and ML tasks
- Git
- MySQL

## Docker

Before you begin, ensure you have the following prerequisites installed on your system:

1. **Docker**: Make sure you have Docker installed. You can download and install Docker from [the official Docker website](https://docs.docker.com/get-docker/).

2. **Docker Compose** (Optional): If your application requires multiple containers or services, Docker Compose can be helpful for managing them together. You can install Docker Compose by following the instructions [here](https://docs.docker.com/compose/install/).

## Getting Started

Follow these steps to run SmartSolveAI_Unified_ChatBot_Internship_Project using Docker:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/your-application.git
   cd your-application
   ```

2. **Build the Docker Image**:

   Build a Docker image for your application using the provided `Dockerfile`. Replace `your-app-image` with a suitable name for your image:

   ```bash
   docker build -t your-app-image .
   ```

   This command will create a Docker image with your application and its dependencies.

3. **Run the Docker Container**:

   Run a Docker container from the image you just built. Replace `your-app-container` with a meaningful container name, and specify any necessary environment variables or ports:

   ```bash
   docker run -d --name your-app-container -p 8080:80 your-app-image
   ```

   - `-d`: Run the container in detached mode (in the background).
   - `--name your-app-container`: Assign a name to the container.
   - `-p 8080:80`: Map port 8080 on your host to port 80 in the container. Adjust this as needed for your application.

4. **Access Your Application**:

   Once the container is running, you can access your application in a web browser by navigating to `http://localhost:8080` (or the URL and port you specified in step 3).

## Configuration

If your application requires configuration settings (e.g., environment variables, configuration files), you can provide these during the container run command using the `-e` option:

```bash
docker run -d --name your-app-container -p 8080:80 -e YOUR_ENV_VARIABLE=value your-app-image
```

## Docker Compose (Optional)

If your application consists of multiple services or containers, consider using Docker Compose to define and manage the entire application stack. Create a `docker-compose.yml` file in your project directory to define the services and their configurations. Then, you can start your application stack with a single command:

```bash
docker-compose up -d
```

## Cleanup

To stop and remove the Docker container, use the following commands:

```bash
docker stop your-app-container
docker rm your-app-container
```

To remove the Docker image, use the following command:

```bash
docker rmi your-app-image
```

## Troubleshooting

- If you encounter any issues or errors while running your application in Docker, check the container logs for more information:

  ```bash
  docker logs your-app-container
  ```

- Ensure that your application's dependencies and configuration are correctly set up in the Dockerfile and any environment variables provided during container creation.

## Script Install

Before you begin, ensure you have the following prerequisites installed on your system:

1. **Python**: Make sure you have Python installed. You can download and install Python from [the official Python website](https://www.python.org/downloads/) if it's not already installed.

2. **Pip**: Pip is a package manager for Python. It is usually installed alongside Python. You can check if you have Pip installed by running:

   ```bash
   pip --version
   ```

   If not, you can install Pip by following the instructions [here](https://pip.pypa.io/en/stable/installation/).

## Getting Started

Follow these steps to run [Your Application Name] using the provided Python script:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/your-application.git
   cd your-application
   ```

2. **Install Dependencies**:

   Install the required Python dependencies using Pip. It's recommended to set up a virtual environment to isolate your project's dependencies:

   ```bash
   python -m venv venv  # Create a virtual environment (optional)
   source venv/bin/activate  # Activate the virtual environment (optional)
   pip install -r requirements.txt  # Install project dependencies
   ```

3. **Run the Application**:

   Execute the Python script to run [Your Application Name]:

   ```bash
   python your_app.py
   ```

   Replace `your_app.py` with the actual name of your Python script.

4. **Access Your Application**:

   Once the script is running, you can access your application by opening a web browser and navigating to `http://localhost:8080` (or the appropriate URL and port specified in your script).

## Configuration

If your application requires configuration settings (e.g., environment variables, configuration files), you can typically modify these settings within your Python script or by providing them as command-line arguments.

## Usage

Provide information on how users can interact with or use your application. Include details about available commands, arguments, and options if applicable.

## Troubleshooting

- If you encounter any issues or errors while running your application, check the error messages displayed in the terminal. These messages often provide valuable information about the problem.

- Make sure you have installed all the required dependencies mentioned in the `requirements.txt` file.

## Additional Resources

- [Python Official Documentation](https://docs.python.org/): Refer to the official Python documentation for more information on Python programming.
- [Pip Documentation](https://pip.pypa.io/en/stable/): Explore Pip's documentation for information on Python package management.
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Docker Hub](https://hub.docker.com/): A registry of Docker images, where you can find pre-built images for many popular applications.

## Assumptions
- Users should be aware that the answers are generated by the bot and not assumed as final answers.
- Technical experts should check the bot's efficiency before deploying it into production.

## Functional Requirements
The unified chatbot application built using RASA should:
- Support natural language processing.
- Be compatible with multiple platforms.
- Generate accurate responses.
- Integrate with external APIs for enhanced user interactions, including speech functionality.

## Non-Functional Requirements
The unified chatbot application should:
- Exhibit high availability.
- Maintain low response latency.
- Ensure secure data handling.

## External Interface Requirements
The unified chatbot application should integrate with various messaging platforms, including:
- Facebook
- LinkedIn
- SMS
- WhatsApp

## Technology Used
- RASA for natural language processing with custom SpacyNLP , custom pipelines and policies.
- Twilio API for messaging integration.
- Python and Python libraries for machine learning and deep learning.

## Getting Started
To get started with this project, follow the installation and setup instructions in the [Installation Guide](./docs/installation.md).

## Usage
Refer to the [User Guide](./docs/user-guide.md) for instructions on how to use the chatbot application effectively.

## Contributing
Contributions to this project are welcome! Please see the [Contribution Guidelines](./CONTRIBUTING.md) for details on how to contribute.

## License
This project is licensed under the [MIT License](./LICENSE).

---

This README provides a comprehensive overview of your project, its requirements, and how to get started. Be sure to replace the placeholder content with specific information relevant to your project.
