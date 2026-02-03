7. A request is sent from a Go client, containing a request body,
and an auth token to a specific endpoint on the server. The Go application waits
for a response from the server. Once the response is received, the response body is 
then unmarshaled for further inspection, allowing the client to handle error codes
as it chooses. 
==WRONG==

8. An HTTP operation is idempotent when a client can make the same request multiple times,
and the server is able to cache the first request made in state storage to check all future requests against
to ensure the same operation is not conducted if the request bodies match. This is important for
operations where uniqueness is of importance. 
==WRONG==

9. 4xx errors are returned when there is an issue with the client, and 5xx errors are 
returned in the case of a server issue.

10. Common causes of backend services slowing down under load are request storms, failure to utilize
DNS to cache URLs.
==WRONG==

11. You would use gRPC over REST if your goal was speed and efficiency, as gRPC allows 
you to directly call a function on a server, instead of sending a request to an endpoint.
This allows the client to bypass all of the procedures/operations that are conducted once an
endpoint is hit. Instead, they can just retrieve a value produced by a function on the server.
==REVIEW==    

12. WebSockets open a persistent connection between a client and a server until a closeframe
is sent. This allows the client to sent multiple requests without the server having to open a connection,
receive a request, send a response, and close the connection. Instead, the server maintains an open
connection with the client allowing for multiple requests to be handled without as much load.
==REVIEW==

13. GraphQL allows the client to be selective about what 
information it wants from a given endpoint on the server. This benefits
the client because they only receive the data that they need. REST forces the 
client to receive an entire response body from the endpoint they aim to hit,
which is easier for the server as it does not have to parse exactly what information to send to the client


14. HTTP/1.1 incorporates a single TCP connection between a client and server. HTTP/2 uses
a multiplexed connection, allowing for multiple TCP connections in individual sub-streams of the 
overall client-server conection. This is important, because HTTP/2 prevents load and back up issues in cases
where a single TCP connection made in HTTP/1.1 could cause a backlog of API calls if the first call hangs.
==REVIEW==

15. TCP is an ACK-based connection, meaning a client sends data, and the server acknowledges that 
the data has been received. This allows for retries upon failure, and preserves data integrity if 
data completion/correctness is of importance. UDP is a much faster protocol, that allows data to be sent
directly to a server, without checking if data was actually received. This is useful for applications 
where speed is valued over data integrity. 


16. TLS guarantees connection security, but does not guarantee application security.
i.e. while a connection might be secure, an application might contain logical flaws,
exposing information that should be secure/encrypted.


17. When a service makes a request to a domain name this the process that occurs:
    - The browser's cache is first checked to see if the domain's IP exists there
    - If not, the ISP's server is checked to see if the domain's IP exists there
    - If not, then the root server of the DNS is contacted with the desired domain name
        - From here, the root server contacts the TLD server of the DNS is contacted
        - The TLD server takes the top level domain of the domain name
        - Based on the top level domain, the server containing all the IP's that have this 
        top level domain is contacted
        - This server returns the IP matching the name of the requested domain
        - This ip is then propagated back down to the client
         ==REVIEW==

18. A backend service is considered stateless when the server does not cache/remember
any information of requests sent from a client. A client a body and 
auth token for each request made to the server. This can be useful to reduce the amount of 
cache and storage space taken up on the server running the service, improving the performance 
of said service.
==REVIEW==

19. Retries can make a system less reliable for multiple reasons:
    - The server's load can exponentially increase if multiple retries 
    are made for the same request
    - If an operation is not idempotent, then an operation that was intended 
    to only execute once can execute multiple times
    These can cause the system to fail completely if load thresholds are reached.

20. If a downstream dependency becomes slow, the system can be caught in a deadlock with
multiple requests piling up on the api level (or an upstream level) which can either cause
the system to fail or slow down without clarity as to what the exact cause is. This should be handled 
by preventing any future requests to be made for a period of time and resolving/processing the requests
made up to that point.
==REVIEW==
