Inventory App

This is a fully containerized inventory management application built with **Flask** and **MongoDB**. The app provides backend functionality for managing inventory items and includes shell scripts to build and run the project, as well as a **Docker Compose** configuration for easy setup.

## Features
- Backend API built with Flask for managing inventory.
- MongoDB is used for data storage.
- Fully containerized using Docker, simplifying the deployment process.
- Includes shell commands and a Docker Compose file for building and running the application.
- Comes with tests and a packaging setup for easy distribution.

## Project Structure
```
├── build/                     # Build artifacts
├── dist/                      # Distribution files
├── instance/                  # Application instance folder
├── inventory/                 # Core application code
├── inventory.egg-info/        # Python egg info for packaging
├── inventorydb/               # MongoDB database files
├── tests/                     # Unit and integration tests
├── .DS_Store                  # MacOS system file (optional to include)
├── Dockerfile                 # Docker setup for Flask app
├── MANIFEST.in                # Packaging instructions
├── README.md                  # Project documentation (this file)
├── build.sh                   # Shell script to build the project
├── docker-compose.yml         # Docker Compose configuration
├── requirements.txt           # Python dependencies
├── run.sh                     # Shell script to run the app
├── setup.cfg                  # Configuration for package distribution
├── setup.py                   # Python setup script for packaging
```

## Installation & Setup

### Using Shell Commands
1. Build the project:
   ```bash
   sh build.sh
   ```
2. Run the project:
   ```bash
   sh run.sh
   ```

### Using Docker Compose
1. Make sure you have Docker and Docker Compose installed.
2. Build and start the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. The Flask app will be accessible at `http://localhost:5000`.

## Running Tests
The project includes unit and integration tests located in the `tests/` directory. To run the tests, use the following command:
```bash
python -m unittest discover tests
```

## Dependencies
- **Flask** for building the API.
- **MongoDB** for data persistence.
- **Docker** and **Docker Compose** for containerization.

All required Python packages are listed in the `requirements.txt` file, and they will be installed automatically when using Docker.

## Packaging and Distribution
The project is set up for packaging using `setup.py`. To create a distributable version of the app, you can run:
```bash
python setup.py sdist
```

## Usage
Once the app is running, you can use tools like **Postman** or **cURL** to interact with the API and manage inventory items. The API will allow you to perform typical inventory management tasks such as adding, updating, and deleting items.

## License
This project is licensed under the MIT License.

---

This updated **README** provides a more comprehensive overview of your inventory app, including its structure, setup instructions, and relevant files. Let me know if you'd like to refine it further!
