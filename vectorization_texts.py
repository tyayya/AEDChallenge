from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calcular_similitud_intereses(intereses1, intereses2):
    """
    Calcula la similitud entre dos listas de intereses usando la similitud de Jaccard.
    """
    set1 = set(intereses1)
    set2 = set(intereses2)
    
    # Intersección y unión
    interseccion = set1 & set2
    union = set1 | set2
    
    # Similitud de Jaccard
    return len(interseccion) / len(union) if union else 0


def calcular_similitud_objetivos(objetivo1, objetivo2):
    """
    Calcula la similitud entre dos textos usando TF-IDF y similitud de coseno.
    """
    # Vectorizador TF-IDF
    vectorizer = TfidfVectorizer()

    # Convertir los textos a vectores TF-IDF
    tfidf_matrix = vectorizer.fit_transform([objetivo1, objetivo2])

    # Calcular similitud de coseno entre los dos vectores
    return cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]


