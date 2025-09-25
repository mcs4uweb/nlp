import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from typing import Dict, Any, Optional, Tuple, Union

class RequestHelper:

    boundary = "------------------------boundary0USMEPCOM"

    def __init__(self):
        pass

    def initialize(
        self,
        headers: Optional[Dict[str, str]] = None,
        retries: int = 3,
        backoff_factor: float = 0.3,
        status_forcelist: Optional[tuple] = None,
        cert: Optional[Union[Tuple[str, str], str]] = None,
        verify: bool = False
    ):
        """
        Initializes the RequestHelper with default headers and retry strategy.
        If no headers are provided, defaults to 'Content-Type': 'application/json'.

        Args:
            headers (Optional[Dict[str, str]]): Default headers for all requests.
            retries (int): Number of retries for failed requests.
            backoff_factor (float): A backoff factor to apply between attempts.
            status_forcelist (Optional[tuple]): HTTP status codes that we should force a retry on.
        """
        self.default_headers = headers or {'Content-Type': 'application/json'}
        self.session = requests.Session()

        # Apply certificate configuration to session if available
        if cert:
            self.session.cert = cert
        self.session.verify = verify

        # Define the retry strategy
        retry_strategy = Retry(
            total=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist or (500, 502, 503, 504),
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT", "DELETE"],
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)

        # Mount the adapter to both HTTP and HTTPS protocols
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        return self

    def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> requests.Response:
        """
        Performs a GET request to the specified URL with retry logic.

        Args:
            url (str): The endpoint URL.
            params (Optional[Dict[str, Any]]): Query parameters for the request.
            headers (Optional[Dict[str, str]]): Headers to override or add to the default headers.

        Returns:
            requests.Response: The response object from the GET request.
        """
        # Merge default headers with any additional headers
        request_headers = self.default_headers.copy()
        if headers:
            request_headers.update(headers)

        # Perform the GET request with retry logic
        response = self.session.get(url, params=params, headers=request_headers)
        return response

    def post(
        self,
        url: str,
        data: Optional[Any] = None,
        json: Optional[Any] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> requests.Response:
        """
        Performs a POST request to the specified URL with retry logic.

        Args:
            url (str): The endpoint URL.
            data (Optional[Any]): The form data to send in the body of the request.
            json (Optional[Any]): The JSON data to send in the body of the request.
            headers (Optional[Dict[str, str]]): Headers to override or add to the default headers.

        Returns:
            requests.Response: The response object from the POST request.
        """
        # Merge default headers with any additional headers
        request_headers = self.default_headers.copy()
        if headers:
            request_headers.update(headers)

        # Perform the POST request with retry logic
        response = self.session.post(url, data=data, json=json, headers=request_headers)
        return response
