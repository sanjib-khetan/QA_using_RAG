# PDF Upload and Processing Application

This is a Flask application that allows users to upload a PDF file along with some text. The uploaded file and text are processed and the results are displayed on the UI.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.6+.
- You have a working internet connection to download the necessary dependencies.

## Getting Started

Follow these instructions to set up and run the application on your local machine.

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/sanjib-khetan/QA_using_RAG.git
cd QA_using_RAG

2. Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Set the Secret Key
export SECRET_KEY='your_secret_key'

5. Create the Upload Directory
Ensure that the uploads directory exists. You can create it manually or the application will create it automatically when it runs.

6. Run the Application
Start the Flask application using the following command: python run.py
The application will start running on http://127.0.0.1:5000/.

7. Access the Application
Open your web browser and go to http://127.0.0.1:5000/ to access the application.


Project Structure
Here is the project structure for reference:
pdf-upload-processing/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│
├── python_code/
│   ├── LLM
│       ├── llm_call_rag.py
│   ├── RAG
│       ├── rag.py
│   ├── utils
│       ├── odf_parser.py
│       ├── post_slack.py
│   ├── main.py
│
├── templates/
│   ├── layout.html
│   ├── upload.html
│   └── result.html
│
├── config.py
├── run.py
└── requirements.txt
