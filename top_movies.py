import requests
from bs4 import BeautifulSoup

def top_movies(year):
    # URL for movies 
    URL = f"https://www.imdb.com/search/title/?title_type=feature&release_date={year}-01-01,{year}-12-31&sort=num_votes,desc"

    # Fetching the user content with headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(URL, headers=headers)

    print(f"Response Status Code: {response.status_code}")  # Check response status
    if response.status_code != 200:
        print("Failed to fetch data")
        return []

    # Optional: Print part of the response content for debugging
    print(response.text[:500])  # Print first 500 characters of the response

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find movie containers                  
    movies = soup.find_all('div', class_='lister-item mode-advanced')

    top_movies = []

    for movie in movies[:50]:  # Limit to 50 movies
        title = movie.h3.a.text.strip()
        year_text = movie.h3.find('span', class_='lister-item-year').text.strip()
        rating = movie.strong.text.strip() if movie.strong else 'N/A'
        metascore = movie.find('span', class_='metascore').text.strip() if movie.find('span', class_='metascore') else 'N/A'
        votes = movie.find('span', attrs={'name': 'nv'})['data-value'] if movie.find('span', attrs={'name': 'nv'}) else 'N/A'

        top_movies.append({
            'title': title,
            'year': year_text,
            'rating': rating,
            'metascore': metascore,
            'votes': votes
        })

    return top_movies


if __name__ == '__main__':
    year = input("Enter the year: ")
    movies = top_movies(year)
    
    if movies:
        print(f"\nTop Movies of {year}:")
        for index, movie in enumerate(movies, start=1):
            print(f"{index}. {movie['title']} ({movie['year']}) - Rating: {movie['rating']}, Metascore: {movie['metascore']}, Votes: {movie['votes']}")
