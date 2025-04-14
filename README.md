# Sentiment Analysis Web Application

This project is a **Sentiment Analysis Web Application** built using **Flask** and **TextBlob**. It allows users to input text and analyzes the sentiment, providing an overall sentiment score, subjectivity, and a breakdown of sentiment for each sentence.

---

## Features

- **Sentiment Analysis**:
  - Determines the overall sentiment (Positive, Negative, or Neutral).
  - Provides polarity (ranging from -1 to 1) and subjectivity (ranging from 0 to 1).
- **Sentence-Level Analysis**:
  - Breaks down the sentiment for each sentence in the input text.
- **Responsive Design**:
  - A futuristic and responsive user interface that works seamlessly on desktops, tablets, and mobile devices.
- **Error Handling**:
  - Handles empty or invalid inputs gracefully.

---

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS (with a futuristic design)
- **Sentiment Analysis**: TextBlob

---

## Installation

### Prerequisites
- Python 3.7 or higher
- `pip` (Python package manager)

## Steps
### Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/practice_project.git
   cd practice_project
   ```
### Install the required dependencies:
 ```bash
pip install -r requirements.txt
```

### Download the necessary NLTK corpora for TextBlob:
```bash
python -m textblob.download_corpora
```

Run the Flask application:
```bash
python server.py
```
Open your browser and navigate to:
```bash
http://127.0.0.1:5000
```

## Usage
1. Enter the text you want to analyze in the provided text area. \n
2. Click the Analyze button. \n
3. View the results, including: \n
- Overall sentiment (Positive, Negative, or Neutral) \n
- Polarity and subjectivity scores \n
- Sentence-level sentiment breakdown \n

### Example
Input:
```bash
I love programming. Debugging can be frustrating, but solving problems is rewarding.
```

Output:
```bash
Overall Sentiment: Positive
Polarity: 0.5 
Subjectivity: 0.6 
Sentence Breakdown:
Sentence: "I love programming." 
Polarity: 0.5 
Subjectivity: 0.6 
Sentiment: Positive 
Sentence: "Debugging can be frustrating, but solving problems is rewarding." 
Polarity: 0.4 
Subjectivity: 0.7 
Sentiment: Positive
```

### Project Structure
```bash
practice_project/
├── app/
│   ├── __init__.py          # Initializes the Flask app
│   ├── server.py            # Flask application logic
│   ├── sentiment_analysis.py # Sentiment analysis logic
│   ├── templates/
│   │   └── index.html       # Frontend HTML template
│   └── static/              # Static assets (e.g., CSS, images)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── setup.py                 # Packaging configuration
└── LICENSE                  # License file
```

### Future Enhancements
-Add support for multiple languages using TextBlob's translation feature.
-Integrate a database to store user inputs and analysis results.
-Add data visualization for sentiment scores using libraries like Chart.js or Matplotlib.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
- Flask - Lightweight Python web framework.
- TextBlob - Library for processing textual data.
- NLTK - Natural Language Toolkit for Python.


---

