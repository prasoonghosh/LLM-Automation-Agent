# LLM Automation Agent

## Overview

The **LLM Automation Agent** is designed to process log files, reports, and code artifacts, automating routine tasks and integrating with the CI pipeline. It leverages a Large Language Model (LLM) to handle unpredictable data and execute deterministic multi-step processes while ensuring the results are exactly verifiable against pre-computed expected outputs.

## Current Achievements

- **Log File Analysis:** Extracts and processes error messages from log files.
- **Summarization:** Generates concise summaries from long text inputs.
- **FastAPI Integration:** Provides an API endpoint (`/execute-task/`) to accept tasks via HTTP requests.

## How It Works

1. **Receive User Input**: The agent receives a plain-English task request through the API.
2. **Task Parsing**: The input is processed and classified into an appropriate category (log analysis, email processing, summarization, etc.).
3. **Task Execution**: The parsed task is executed using pre-defined handlers for each task type.
4. **Result Return**: The API returns a structured response containing the execution status and processed data.

## Installation and Setup

### Prerequisites

- Python 3.9+
- Virtual environment setup
- Required dependencies installed (`pip install -r requirements.txt`)

### Steps to Run

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd llm-automation-agent
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```
5. Test API using `curl` or Postman:
   ```sh
   curl -X POST "http://127.0.0.1:8000/execute-task/" -H "Content-Type: application/json" -d '{"user_input": "Summarize this long paragraph..."}'
   ```

## API Endpoints

### `POST /execute-task/`

Executes an automation task based on the given user input.

#### Request Format

```json
{
    "user_input": "Summarize this long paragraph..."
}
```

#### Response Format

```json
{
    "status": "success",
    "data": {
        "status": "success",
        "summary": "This long paragraph summarized."
    }
}
```

## Future Enhancements (Planned for Today)

- **Data Extraction from Reports:** Extract structured data from CSV, Excel, and PDF reports.
- **Database Query Execution:** Run SQL queries on structured data.
- **Automated Issue Resolution:** Intelligent resolution of identified issues using predefined actions.
- **LLM-Based Decision Making:** Use AI to suggest or take actions based on input patterns.
- **Enhanced Error Handling:** More robust logging and handling for different error scenarios.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

MIT License

Copyright (c) 2025 Prasoon Ghosh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

