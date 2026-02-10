## Section 1
- Refactor or rename `IntervalManager` to clarify responsibility
- Add comments explaining lifecycle boundaries
- Reorder logic to make control flow clearer

## Section 2
- Replace `log.Fatalf` inside handlers
- Return proper HTTP error codes (`400`, `500`)
- Skip malformed rows and continue processing
- Log errors instead of terminating the process

## Section 3
- Increase scanner buffer size
- Switch to `bufio.Reader`
- Add comments documenting memory tradeoffs

## Section 4
- Change interval computation to fixed wall-clock buckets
- Use time truncation for interval start
- Clarify interval inclusivity (`[start, end)`)

## Section 5
- Prevent duplicate CSV headers
- Detect file existence or size before writing headers
- Separate file-creation logic from append logic

## Section 6
- Protect `IntervalManager` with a mutex
- Use a single writer goroutine with a channel
- Serialize disk writes to avoid corruption

## Section 7
- Add startup logic to inspect existing files
- Treat the last file as incomplete
- Log committed vs open intervals

## Section 8
- Create the output directory at startup
- Fail fast with a clear startup error
- Add minimal startup logging
