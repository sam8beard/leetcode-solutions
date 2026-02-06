- What does success look like for someone in this role in the first 6-12 months? 

- What does a day in the life look like for someone in this role?

- Is the upcoming technical interview more centered on Go-related knowledge? 
System design? 
Data structures/Algorithms?
General problem solving?

- What does the rest of the interview process look like after the first technical? 

- What does growth look like for someone in this position?


### Authentication & Token Knowledge (Backend / Go Context)

- **Authentication vs Authorization**
  - Authentication verifies *who* the caller is.
  - Authorization determines *what* the authenticated identity is allowed to do.

- **Token-Based Authentication**
  - Used to avoid server-side sessions and enable stateless services.
  - Common in distributed and microservice architectures.

- **JWT (JSON Web Token)**
  - Consists of a header, payload (claims), and signature.
  - Signed using HMAC (shared secret) or RSA/ECDSA (public/private key).
  - Verifiable by downstream services without calling an auth server.

- **Common Token Claims**
  - Identity: user ID, service account, tenant.
  - Authorization: roles, scopes, permissions.
  - Time-based: `exp` (expiration), `iat` (issued at), sometimes `nbf` (not before).

- **Access Tokens vs Refresh Tokens**
  - Access tokens are short-lived to limit damage if compromised.
  - Refresh tokens are longer-lived and exchanged for new access tokens.
  - Refresh tokens must be stored more securely and rotated carefully.

- **Stateless System Benefits**
  - Easier horizontal scaling.
  - Reduced coupling to a central auth service.
  - Better performance in high-throughput systems.

- **Security Considerations**
  - Always transmit tokens over TLS.
  - Strict validation: signature, expiration, issuer, and audience.
  - Poor validation can lead to replay attacks or privilege escalation.
  - Token revocation is difficult; key rotation and short TTLs mitigate risk.

- **Go Backend Implementation Pattern**
  - Authentication enforced in middleware.
  - Validated identity is attached to request context.
  - Business logic consumes identity info without handling auth directly.
