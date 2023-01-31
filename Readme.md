## Word Counter API
A REST API for counting the repetition of each word (alphanumeric), the total number of words, the total number of characters with spaces, and the total number of characters without spaces in a given string.
### Installation

Change into the project directory:
``` bash
cd word-counter

```

Create a Docker Image:
``` bash
docker build -t word_count_api:1.0 .
```

Run the Docker Container:
```bash
docker run -p 8000:5000 word_count_api:1.0 
```
### Usage
Run the API server:
Make a request to the API, for example:
```
curl --location --request POST 'http://localhost:8000/word_counter' \
--form 'string="hello world ,, 11 9 zzz zzz"'
```

### Testing
Create a virtual environment and activate it:
```bash
python -m venv env 
```
```bash
source env/bin/activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

To run the unit tests, use the following command:
```
python3 test.py 
```
