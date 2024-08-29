from django.urls import reverse
import requests


class RequestService:
    def __init__(self):
        pass

    def sendInternalRequest(
        self, endpointName, currentRequest=None, pathArgs=[], headers={}, queryArgs={}
    ):
        bearerToken = currentRequest.session.get("bearer", None)
        relativeURL = reverse(endpointName, args=pathArgs)
        fullURL = currentRequest.build_absolute_uri(relativeURL)

        if queryArgs:
            queryString = "&".join([f"{key}={value}" for key, value in queryArgs.items()])
            fullURL += f"?{queryString}"
        if bearerToken:
            headers["Authorization"] = f"Bearer {bearerToken}"
        response = requests.get(fullURL, headers=headers)
        # Throws HTTP Error for status codes 400-599
        response.raise_for_status()
        return response
