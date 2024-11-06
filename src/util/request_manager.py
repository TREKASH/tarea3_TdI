import time
import requests
from typing import Dict, Any

class RequestsManager:
    BASE_URL = "http://tormenta.ing.puc.cl/api"
    RATE_LIMIT = 10  # requests per second
    TIMEOUT = 120  # max duration for each request in seconds
    EMBEDDING_MODEL = "nomic-embed-text"
    LLM_MODEL = "integra-LLM"

    def __init__(self):
        self.last_request_time = 0  # To track the time of the last request

    def _wait_for_rate_limit(self):
        """Ensures that requests respect the API rate limit."""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        if time_since_last < 1 / self.RATE_LIMIT:
            time.sleep((1 / self.RATE_LIMIT) - time_since_last)
        self.last_request_time = time.time()

    def _send_request(self, endpoint: str, payload: Dict[str, Any]) -> Any:
        """Sends a request to the specified API endpoint with rate limiting and error handling."""
        self._wait_for_rate_limit()
        url = f"{self.BASE_URL}/{endpoint}"
        try:
            response = requests.post(url, json=payload, timeout=self.TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {e}")

    def get_embedding(self, text: str) -> Any:
        """Generates an embedding for a given text."""
        payload = {
            "model": self.EMBEDDING_MODEL,
            "input": text
        }
        return self._send_request("embed", payload)

    def get_llm_response(self, prompt: str, context: str = "") -> Any:
        """Generates a response from the LLM API given a prompt and context."""
        payload = {
            "model": self.LLM_MODEL,
            "input": {"prompt": prompt, "context": context}
        }
        return self._send_request("generate", payload)

# Usage example:
# manager = RequestsManager()
# embedding = manager.get_embedding("Sample text to vectorize")
# response = manager.get_llm_response("Explain this movie scene")

if __name__ == "__main__":
    
    manager = RequestsManager()
    embedding = manager.get_embedding("Sample text to vectorize")
    print(embedding)

    response = manager.get_llm_response("gs out a bottle of whiskey. DECKARD (V.O.) Bryant's got a liver problem. A couple years back he handed me a bottle and said have a drink for another man. I been drinking for him ever since. Deckard sets down the report and takes the shot Bryant just poured for him. DECKARD Six, huh? BRYANT Five. Three nights ago one of them managed to break into the Tyrell Corporation. Killed two guards and got as far as the Genetic Sector before he got fried going through an electro- field. DECKARD What was he after? BRYAN")
    print(response)