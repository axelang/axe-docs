# .\net.axec

## model HttpResponse

HTTP response model containing status code, headers, and body

## model MemoryStruct

Memory struct for curl write callback

## def write_callback(contents: char*, size: usize, nmemb: usize, userp: char*): usize

Internal write callback function for curl - grows buffer as needed

## def curl_init()

Initialize the cURL library globally

## def curl_cleanup()

Cleanup the cURL library globally

## def http_get(url: string): HttpResponse

Perform an HTTP GET request

## def http_post(url: string, data: string): HttpResponse

Perform an HTTP POST request with data

## def http_put(url: string, data: string): HttpResponse

Perform an HTTP PUT request with data

## def http_delete(url: string): HttpResponse

Perform an HTTP DELETE request

## def http_patch(url: string, data: string): HttpResponse

Perform an HTTP PATCH request with data

## def http_head(url: string): HttpResponse

Perform an HTTP HEAD request (retrieves headers only)

## def download_file(url: string, output_path: string): bool

Download a file from a URL and save it to disk

## def url_encode(input: string): string

URL encode a string (percent encoding for URLs)

## def url_decode(input: string): string

URL decode a string (decode percent-encoded URLs)

## def is_success_status(status_code: i32): bool

Check if a response status code indicates success (2xx)

## def is_redirect_status(status_code: i32): bool

Check if a response status code indicates a redirect (3xx)

## def is_client_error_status(status_code: i32): bool

Check if a response status code indicates a client error (4xx)

## def is_server_error_status(status_code: i32): bool

Check if a response status code indicates a server error (5xx)

## def free_response(response: HttpResponse)

Free the memory allocated for an HttpResponse
