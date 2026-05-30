# simplmail

simplmail is a simple raw and stable terminal client. Are you tired of openssl s_client with its long commands and unstable connection? simplmail is the solution for you! 

> [!WARNING]
> This program works only for text protocols with CRLF line endings like SMTP, POP3, IMAP, IRC etc.

## Installation and Usage

Installation: `pip install simplmail`

Usage: `smail server.example PORT`

Also, you can write the `smail` command without arguments so the program will ask you to choose server and port.

### Example of usage:

```
D:\Maksym\PyPI\simplmail>smail smtp.example.net 465
Simplmail v0.1 (and not only email)
Created connection to smtp.example.net:465.
Initialized SSL.

220 2.0.0 EXAMPLE.NET ESMTP from 93.127.124.34 at Sat, 30 May 2026 15:44:02 +0300 [un.20260530.FuduuvooYT]

SMTP>EHLO localhost
250-hosting.com Hello localhost, [93.127.124.34]
250-8BITMIME
250-CHUNKING
250-PIPELINING
250-HELP
250-ENHANCEDSTATUSCODES
250-XUNMTA 6MKrWSHoNqgL70sILRiEh4-lOADjGxB-FnDhOgvHK9FdI-pRVBxX8bLTTVKZ3Px7Ey1tEXvRofmKiSX5nm7eQT98zSUKWzzzUTnLNvdqLXNkty0wY7CCS0fF:zlo0BKT8cVFlle7J
250-AUTH PLAIN LOGIN
250-SIZE 26214400
250 LIMITS MAILMAX=50 RCPTMAX=100

SMTP>AUTH LOGIN
334 VXNlcm5hbWU6

SMTP>$user@example.net
334 UGFzc3dvcmQ6

SMTP>$pass
235 2.7.0 Authentication succeeded [un.20260530.FuduuvooYT]

SMTP>MAIL FROM:<user@example.net>
250 2.1.0 Transaction is open [un.20260530.FuduuvooYT]

SMTP>RCPT TO:<user@example.com>
250 2.1.5 Recipient accepted [un.20260530.FuduuvooYT]

SMTP>DATA
354 2.0.0 Go ahead

SMTP>From: user@example.net
SMTP>To: user@example.com
SMTP>Subject: example
SMTP>
SMTP>This is an example email
SMTP>.
250 2.0.0 Accepted id=3aLdHe-7ZeP6YPrms [un.20260530.FuduuvooYT]

SMTP>QUIT
221 2.0.0 hosting.com closing connection [un.20260530.FuduuvooYT]

SMTP>smail quit
```

## Specifications

Supported protocols (both encrypted (SSL) and unencrypted (plain text) versions):
- SMTP
- POP3
- IMAP
- IRC

And any other text protocol that has CRLF line endings!

## Features

simplmail includes commands and tools right in the console! (they should be written inside the session and not in the shell):
- `smail autotag` for automatic tags in IMAP
- `smail autopong` for automatic pong in IRC
- `smail quit` or `smail exit` for exit

And if the line starts with the `$` sign, simplmail will send text after it in base64 encoding. That is very useful for SMTP `AUTH LOGIN`!

Also, it auto-detects whether it should use SSL for most protocols!

If you are tired of openssl s_client or you like control and interactivity of `ftp` and want to do everything that you can like this, install simplmail and try it yourself!
