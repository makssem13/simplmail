import ssl, socket, base64, sys, threading

print("Simplmail v0.1 (and not only email)")
HOST = input("HOST>") if len(sys.argv)<2 else sys.argv[1]
PORT = int(input("PORT>")) if len(sys.argv)<3 else int(sys.argv[2])
SSL = True if PORT in [993, 995, 465, 6697] else False if input("SSL (Y/n)>").lower() in ["n"] else True

def get_instr():
    match PORT:
        case 143 | 993: return "IMAP"
        case 110 | 995: return "POP3"
        case 25 | 465 | 587: return "SMTP"
        case 6667 | 6665 | 6666 | 6668 | 6669 | 6697 | 7000: return "IRC"

INSTR = get_instr()+">"
AUTOPONG = False
AUTOTAG = False

sock = socket.create_connection((HOST, PORT))
print(f"Created connection to {HOST}:{PORT}.")
if SSL:
    ctx = ssl.create_default_context()
    conn = ctx.wrap_socket(sock, server_hostname=HOST)
    print("Initialized SSL.")
else:
    conn = sock

conn.settimeout(1)

def read():
    try:
        data = conn.recv(65536)
        return data.decode(errors="ignore")
    except:
        return ""

TAG = "autotag"
TAGID = 0

def automod(data):
    global TAGID
    if AUTOTAG:
        TAGID+=1
        data = TAG+str(TAGID)+" "+data
    return data

def send(data):
    conn.sendall((automod(data) + "\r\n").encode())

def print_msg(msg):
    sys.stdout.write("\033[2K\r")
    sys.stdout.write(msg+"\n")
    sys.stdout.write(INSTR)
    sys.stdout.flush()

def autoreply(msg):
    if AUTOPONG:
        if msg.startswith("PING"):
            server = msg.split(":")[1] if ":" in msg else ""
            cmd = f"PONG{f' :{server}' if server else ''}"
            send(cmd)
            print_msg(f"SMAIL AUTOREPLY: {cmd}")

def reader():
    while 1:
        data = read()
        if data:
            print_msg(data)
            autoreply(data)

def scommand(cmd):
    global AUTOPONG, AUTOTAG
    match cmd:
        case "quit" | "exit":
            exit(0)
        case "autopong":
            AUTOPONG = True
        case "noautopong":
            AUTOPONG = False
        case "autotag":
            AUTOTAG = True
        case "noautotag":
            AUTOTAG = False
    return

print()
threading.Thread(target=reader, daemon=True).start()

while True:
    cmd = input(f"{INSTR}")
    if cmd.lower().startswith("smail"):
        scommand(cmd.lower()[6:])
    elif cmd != "":
        if cmd[0] == "$":
            cmd = base64.b64encode(cmd[1:].encode()).decode()
        send(cmd)
