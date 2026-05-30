# simplmail

simplmail is a simple raw and stable terminal client. Are you tired of openssl s_client with its long commands and unstable connection? simplmail is the solution for you! 

> [!WARNING]
> This program works only for text protocols with CRLF line endings like SMTP, POP3, IMAP, IRC etc.

## Installation and Usage

Installation: `pip install simplmail`

Usage: `smail server.example PORT`

Also, you can write the `smail` command without arguments so the program will ask you to choose server and port.

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

And if the line starts with the `$` sign, simplmail will send text after it in base64 encoding. That is very useful for SMTP `AUTH LOGIN`!

Also, it auto-detects whether it should use SSL for most protocols!

If you are tired of openssl s_client or you like control and interactivity of `ftp` and want to do everything that you can like this, install simplmail and try it yourself!
