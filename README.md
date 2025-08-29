# Bajaj Flask API

This project is a simple Flask-based API for processing lists of mixed data (numbers, alphabets, and special characters) and returning structured information about them.

## Features
- Accepts a POST request at `/bfhl` with a JSON payload containing a list of strings under the `data` key.
- Separates even and odd numbers, alphabets, and special characters from the input.
- Calculates the sum of all numeric values.
- Returns a reversed, alternating caps string of all alphabets in the input.
- Responds with user details (name, DOB, email, roll number) and processed data.

## API Endpoint
### POST `/bfhl`
**Request Body:**
```json
{
  "data": ["A", "1", "b", "2", "@", "C"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["2"],
  "alphabets": ["A", "B", "C"],
  "special_characters": ["@"],
  "sum": "3",
  "concat_string": "CbA"
}
```

## Setup Instructions
1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
2. **Run the Flask app:**
   ```powershell
   python app.py
   ```
   The server will start at `http://127.0.0.1:5000/`.

## Notes
- Update the user details in `app.py` as needed.
- For production, use `gunicorn` as specified in `requirements.txt`.

## Requirements
- Python 3.7+
- Flask
- gunicorn

## License
This project is for demonstration purposes.
