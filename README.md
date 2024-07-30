# Job Application Tracker

Job Application Tracker is a simple GUI application built with Python and Tkinter to help you track your job applications. You can add, view, update, and delete job applications easily. The application uses SQLite for data storage.

## Features

- Add new job applications with details such as company name, job title, application date, job posted date, notes, and status of cover letter and job reply.
- View all job applications in a tabular format.
- Update existing job applications.
- Delete job applications with a confirmation prompt.
- Search job applications by company name or job title.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- SQLite (usually included with Python)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Install the required libraries**:
    ```sh
    pip install tk
    ```

## Usage

1. **Run the application**:
    ```sh
    python Job_App_Tracker.py
    ```

2. **Add a new application**:
    - Click on "Add Application".
    - Fill in the details and click "Add Application".

3. **View applications**:
    - Click on "View Applications".
    - You can search, update, or delete applications from this screen.

## File Structure

- `Job_App_Tracker.py`: The main Python script containing the GUI and functionality.
- `job_applications.db`: The SQLite database file (automatically created).
- `README.md`: This file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
