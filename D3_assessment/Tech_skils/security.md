# Security

## Expectation
The Developer is adept at implementing both transport and message-level security in web applications. They should also have an understanding of the Application Security Verification Standard (OWASP).

## Justification

### Transport level security
Transport level security is based on Secure Sockets Layer (SSL) or Transport Layer Security (TLS) that runs beneath HTTP. SSL and TLS provide security features including authentication, data protection, and cryptographic token support for secure HTTP connections. To run with HTTPS, the service endpoint address must be in the form https://. The integrity and confidentiality of transport data, including SOAP messages and HTTP basic authentication, is confirmed when you use SSL and TLS. 
SSL is the Industry accepted standard protocol for secured encrypted communications over TCP/IP.

### Message level security
In message level security, security information is contained within the data, which allows security information to travel along with the data. For example, a portion of the data may be signed by a sender and encrypted for a particular receiver. When the data is sent from the initial sender, it may pass through intermediate nodes before reaching its intended receiver. In this scenario, the encrypted portions continue to be opaque to any intermediate nodes and can only be decrypted by the intended receiver. For this reason, message-level security is also sometimes referred to as end-to-end security.

###  Application Security Verification Standard (OWASP)
The Open Web Application Security Project (OWASP), is an international non-profit organization dedicated to web application security. The primary aim of the OWASP Application Security Verification Standard (ASVS) Project is to provide an open application security standard for web apps and web services of all types.

Some security risks include Sensitive data exposure, cross-site scripting, SQL injection, broken authentication, and cross-site request forgery.

Security tips include:
- Use trusted frameworks and libraries.
- Use CSRF protection for forms
- Perform user authentication both at the client and server
- Data input validation and sanitization.
- Access control by using authorization, and ensure with auth tokens
- Output data encryption
- Not storing sensitive data when not necessary.
- Use general error handling on the client, and on the server be more specific. 
- Implement logging and monitoring on the server.
- Use 2FA for critical sites.
- Use precompiled SQL as much as possible
