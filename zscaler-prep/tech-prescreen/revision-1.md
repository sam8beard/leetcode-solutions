Revise answers to questions 7, 8, 10, 11, 12, 14, 17, 18, 20

### 7
A request is made to an endpoint in the Go backend service with an auth token i.e. user/123.

The go service utilizes a router api (i.e. gorilla/mux) to attach handlers
to endpoints and auth verification functionality and instantiates any connections using context.Context needed by the server.

The handler matching the request endpoint is called. The request body closure should be deffered
upon arrival to prevent data leaks when the operation finishes.

Then, the request body is read into memory, processed, any other services are called. If external API calls are made, they are made with the initial request's context to ensure timelines and prevent api failure propagation.

Once the request is processed, a response is built with the appropriate status code and response body. The headers are written to the response writer, and then the json body is encoded and written to the response writer. 

The connection then closes.

### 8
An HTTP operation is idempotent if making executing the operation more than once
does not change the state of the backend.

### 10
Common causes of backend services slowing down under load

### 11


