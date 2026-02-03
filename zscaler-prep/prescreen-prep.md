1. When would you use a mutex instead of a channel in Go?
    - Precise distinction between state protection (mutex) vs communication(channe)
    - When channels are a bad fit (high-frequency counters, caches)
    - Common mutex pitfalls (deadlocks, contention)

2. What is context.Context

Go / Runtime (Heavy Weight)
	1.	When do you use a mutex instead of a channel in Go?
	2.	What problem does context.Context solve in backend services?
	3.	What causes goroutine leaks? Give a concrete example.
	4.	How does Go handle errors, and why doesn’t it use exceptions?
	5.	What is an interface in Go, and why is implicit implementation important?
	6.	What is escape analysis (high level), and why should backend engineers care?



Backend & API Fundamentals
	7.	Walk through the lifecycle of an HTTP request in a Go backend service.
	8.	What makes an HTTP operation idempotent, and why does that matter?
	9.	How do you decide between returning a 4xx vs a 5xx error?
	10.	What are common causes of backend services slowing down under load?



Beyond REST (They will test this)
	11.	Why would you choose gRPC over REST?
	12.	What problems do WebSockets solve that HTTP doesn’t?
	13.	What are the tradeoffs of GraphQL vs REST?



Protocols (Very Relevant for Zscaler)
	14.	What’s the difference between HTTP/1.1 and HTTP/2, and why does it matter?
	15.	TCP vs UDP — when would you choose one over the other?
	16.	At a high level, what does TLS actually guarantee?
	17.	What happens when a service makes a request to a domain name (DNS flow)?



Architecture & Reliability
	18.	What does it mean for a backend service to be stateless, and why is that useful?
	19.	Why can retries make a system less reliable instead of more reliable?
	20.	What happens to your system if a downstream dependency becomes slow? How should you handle it?
