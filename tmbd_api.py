import requests

def get_movie_info(movie_title, api_key):
    # URL base para buscar películas por título en TMDb
    search_url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&api_key={api_key}"
    
    # Realiza la solicitud GET a la API de TMDb
    response = requests.get(search_url)
    
    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear la respuesta JSON
        search_results = response.json()
        
        # Verificar si hay resultados de búsqueda
        if search_results['results']:
            # Obtener el primer resultado de la búsqueda
            movie_id = search_results['results'][0]['id']
            
            # URL para obtener los detalles de la película usando el ID
            details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
            details_response = requests.get(details_url)
            
            if details_response.status_code == 200:
                # Devolver los detalles de la película
                return details_response.json()
            else:
                return f"Error: Unable to fetch movie details (Status code: {details_response.status_code})"
        else:
            return f"No results found for movie title: {movie_title}"
    else:
        return f"Error: Unable to search for movies (Status code: {response.status_code})"

# Ejemplo de uso

movie_title = 'Inception'
movie_info = get_movie_info(movie_title, api_key)

print(movie_info)