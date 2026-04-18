Basics of HTTP/HTTPS

In web development, communication between a client and a server happens through protocols. The most common protocol is HTTP, and its secure version is HTTPS. These protocols define how data is requested, transferred, and received over the internet.

HTTP (Hypertext Transfer Protocol) is a protocol used to transfer data between a client and a server. The data in HTTP is sent in plain text, which means it is not encrypted and can potentially be intercepted by third parties.

HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP. It uses SSL/TLS encryption to protect the data during transmission, ensuring confidentiality and security.

The main differences between HTTP and HTTPS are:
HTTP is not secure while HTTPS is secure. HTTP uses port 80 while HTTPS uses port 443. HTTPS encrypts data using SSL/TLS. HTTPS is used for sensitive data like passwords, banking, and login systems.

An HTTP request is sent from a client to a server. It contains:
- Method (type of action)
- URL (resource path)
- Headers (additional information)
- Body (optional data sent to server)

Example HTTP request:
GET /index.html HTTP/1.1
Host: example.com

An HTTP response is sent from the server back to the client. It contains:
- Status code (result of request)
- Headers (metadata)
- Body (content like HTML or JSON)

Example HTTP response:
HTTP/1.1 200 OK
Content-Type: text/html

<html>
  <body>Hello World</body>
</html>

Common HTTP Methods:
- GET → Retrieve data from server
- POST → Send data to server
- PUT → Update existing data on server
- DELETE → Remove data from server

Common HTTP Status Codes:
- 200 OK → Request was successful
- 201 Created → New resource was created
- 301 Moved Permanently → Resource moved to another URL
- 404 Not Found → Resource does not exist
- 500 Internal Server Error → Server encountered an error

In conclusion, HTTP is a basic but insecure protocol, while HTTPS provides secure communication using encryption. Understanding methods, requests, responses, and status codes is essential for working with APIs and web applications.
