# IMDB Movie search project

This project is a simple movie search engine built using the IMDB dataset. The dataset is a collection of movies and their associated metadata, including titles, actors, genres, and more. The project uses the dataset to create a movie search engine that can search for movies based on various criteria, such as title, year, genre, and actor.

## Project Overview

The project is divided into two main components: the backend and the frontend. The backend is responsible for processing and storing the data from the IMDB dataset, while the frontend is responsible for providing a user-friendly interface for searching and displaying movie information.

### Backend

The backend is built using Python and the FastAPI framework.

The backend uses the SQLAlchemy library to interact with the database.

The backend also uses the Pandas library to load and process the data from the IMDB dataset.

### Frontend
TODO in React JS

## Installation

### 1. Download the Dataset

Use the `wget` command to download the required IMDb datasets:

```bash
wget https://datasets.imdbws.com/name.basics.tsv.gz
wget https://datasets.imdbws.com/title.basics.tsv.gz
```

### Setup

To install the project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using pip: `pip install -r requirements.txt`.
4. Load the data into the database using the `load_data.py` script. Please note that only the first 100 rows of the title and name files are loaded, as the dataset is too large to load all of it.
4. Run the project using the command `uvicorn main:app --reload`.

## Usage

To use the project, you can search for movies by title, year, genre, or actor. The search results will be displayed in the terminal.

### Usage Example
#### Search for Movies

```curl
curl http://127.0.0.1:8000/search?type=short&year=1999
```

This command will search for movies with a title type "short" and a release year of 1999.

#### Search for People

```curl
curl http://127.0.0.1:8000/people?profession=producer
```

This command will search for people with a profession of "producer".
