## Likely Interview Questions and Modification Requests (2-Hour Interview)

---

## 1. Architecture & Control-Flow

**Questions**
- Walk me through the request lifecycle from client to disk.
    - The client makes a post request with the body containing the ndjson file to the 
    /user-events endpoint on port 8000 of the host (port running the container with the executing go process)
    - Then, the request is routed to the port running the server within the go process (port 8080)
    - The request is handled by the handler mapped to the /user-events endpoint
    - This handler has a dependency called IntervalManager which keeps track of the current interval and csv file across
    the life time of the go process
    - The request is processed line by line, using a scanner to stream a single line of the body at a time
    - If this is the first request received within this process lifetime, then initialize the IntervalManager members
    according to the time of the first entry in this request
    - If this is not the first request received within this process lifetime, then determine where to write the current line 
    - If the time of the current entry being processed is within the interval set by the IntervalManager, write to the csv file pointed to by IntervalManager.File
    - If the time of the current entry being processed is not within the interval
        - close the current csv file, open a new one for the new interval, initialize a new writer
        - update the IntervalManager with these members
        - write to this new file
    - After the entire request body has been processed, respond with 200 OK

- Where does streaming happen and why did you choose that approach?
    - streaming happens when we receive the request, we stream the request body line by line
    - I chose this approach to avoid reading the entirety of the potentially large
    request body into memory all at once
- What guarantees does the problem give you, and which parts of your design rely on them?
    - only one request in flight at at time
        - my design does not support concurrent requests, there is no thread safe
        method for modifying shared memory (i.e. IntervalManager and its members)
    - fields are static and not expected to change
        - there is no rigourous file validation of any kind
    - payload is newline delimited
        - in my design, it is assumed each line read is equivalent to one user event
    - rows are ordered by time across requests
        - in my design the the logic for deciding when to close or open new csv files
        assumes that every request will contain data with increasing time fields
- Why do you keep the CSV file open across requests?
    - we keep the csv file open accross requests to account for the
    possibility that future requests might be within the interval of
    the most recently opened csv file. if it is, we need to write to this
    same csv file
- What state lives across requests, and where?
    - the interval manager that is attached to the handler which is mapped to the endpoint
    - the interval contains the interval span, the file writer, and the file pointer
    - it lives in the main thread

**Possible Modifications**
- Refactor or rename `IntervalManager` to clarify responsibility
- Add comments explaining lifecycle boundaries
- Reorder logic to make control flow clearer

---

## 2. Error Handling & Robustness

**Questions**
- What happens if a single JSON line is malformed?
    - the process is killed
- What happens if time parsing fails?
    - the process eventually is killed
- What happens if disk writes fail?
    - the process is killed
- Should one bad event kill the entire service?
    - no, this was merely a trade off due to time constraints.
    in a production environment, I would never let one error kill
    the entire process.

**Likely Modifications**
- Replace `log.Fatalf` inside handlers
- Return proper HTTP error codes (`400`, `500`)
- Skip malformed rows and continue processing
- Log errors instead of terminating the process

---

## 3. Streaming & Memory
**Questions**
- Why did you use `bufio.Scanner`?
    - I used bufio Scanner to stream the request body line by line
- Do you know its limitations?
    - bufio.Scanner.Scan() max size is around 64 kb i believe
- What happens if a JSON line is very large?
    - the process would hang
- How would you fix that?
    - I could buffer the line using a larger size than the initial buffer

**Likely Modifications**
- Increase scanner buffer size
- Switch to `bufio.Reader`
- Add comments documenting memory tradeoffs

---

## 4. Interval Logic & Correctness

**Questions**
- How are your 5-minute intervals defined?
    - the 5 minute intervals are defined by reading an entry if the entry meets one 
    of the requirements to open a new csv file, then the interval starts at that entry's time
    and ends at that entry's time + 5 minutes
- Are these rolling or fixed wall-clock intervals?
    - This is a fixed interval 
- Does this implementation match the spec exactly?
    - I thought this is what the spec was asking for.
- What happens at interval boundaries?
    - If an entry is outside of said interval, then a new interval is set starting at that
    entry's time

**Likely Modifications**
- Change interval computation to fixed wall-clock buckets
- Use time truncation for interval start
- Clarify interval inclusivity (`[start, end)`)

---

## 5. CSV File Semantics

**Questions**
- What happens if multiple requests contribute to the same interval?
    - if multiple requests contribute to the same interval,
    then they are written to the same csv given that the csv file has not
    been closed. this would mean that the requests would be made in succession
    while the csv file is still open
- Do you write the CSV header more than once?
    - no, you do not
- What happens if the file already exists?
    - i dont think this should ever happen, if we assume times in requests will always
    have the same value or later

**Likely Modifications**
- Prevent duplicate CSV headers
- Detect file existence or size before writing headers
- Separate file-creation logic from append logic

---

## 6. Concurrency & Scaling

**Questions**
- What breaks if two requests arrive at the same time?
    - there would be race condition when attempting to access or 
    modify the interval manager or its members
- How would you make this safe for concurrency?
    - we could wrap the interval manager in a mutex
- How would you prevent concurrent file writes?
    - by locking the interval manager when the file is being written
    to, and unlocking it after

**Expected Discussion (Conceptual)**
- Protect `IntervalManager` with a mutex
- Use a single writer goroutine with a channel
- Serialize disk writes to avoid corruption

---

## 7. Crash Recovery & Durability

**Questions**
- What happens if the process crashes mid-write?
    - Currently, if the process crashes mid-write, i'm not sure
    of the behavior as the processes crashes. I'm not sure
    if the file is automatically closed, but maybe we can assume
    that the Go runtime causes all file objects to be closed
    upon exit.
- How would you resume on restart?
    - right now, there is no case for resuming on restart. one method
- How do you know which file is still logically “open”?

**Possible Modifications**
- Add startup logic to inspect existing files
- Treat the last file as incomplete
- Log committed vs open intervals

---

## 8. Docker & Runtime Environment

**Questions**
- Why use a multi-stage Docker build?
- What’s inside the final container?
- Why Alpine?
- What happens if `/app/output` doesn’t exist?

**Likely Modifications**
- Create the output directory at startup
- Fail fast with a clear startup error
- Add minimal startup logging

---

## 9. Go Fundamentals (Using Your Code)

**Questions**
- Why is `IntervalManager` passed as a pointer?
- Who owns the file lifecycle?
- What happens if `Writer.Flush()` fails?
- Why are some structs and fields exported?
- Why split code into `api`, `handlers`, and `internal`?

**Possible Modifications**
- Make ownership boundaries more explicit
- Tighten package responsibilities
- Improve naming for clarity

---

## 10. Production Evolution / Tradeoffs

**Questions**
- What would you change first if this were production?
- What did you intentionally simplify?
- What tradeoffs did you make due to time constraints?

**Expected Framing**
- Acknowledge flaws proactively
- Explain why they’re acceptable here
- Explain how you’d fix them with more time
