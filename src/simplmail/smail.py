import ssl, socket, base64, sys, threading

print("Simplmail v0.1 (and not only email)")
HOST = input("HOST>") if len(sys.argv)<2 else sys.argv[1]
PORT = int(input("PORT>")) if len(sys.argv)<3 else int(sys.argv[2])
SSL = True if PORT in [993, 995, 465, 6697, 7000] else False if PORT in [143, 587, 110, 25, 587, 6667, 6665, 6666, 6669] else False if input("SSL (Y/n)>").lower() in ["n"] else True

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

def starttls():
    global ctx, conn
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    conn = ctx.wrap_socket(sock, server_hostname=HOST)
    print("Initialized SSL.")

if SSL:
    starttls()
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
    sys.stdout.write("\r"+msg)
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

def scommand(command):
    global AUTOPONG, AUTOTAG
    data = command.split(" ")
    cmd = data[0]
    params = data[1:] if len(data)>1 else []
    match cmd:
        case "quit" | "exit":
            exit(0)
        case "autopong":
            if params != []:
                AUTOPONG = params[0].lower().startswith("y")
                print(f"SMAIL: autopong {'enabled' if AUTOPONG else 'disabled'}")
        case "autotag":
            if params != []:
                AUTOTAG = params[0].lower().startswith("y")
                print(f"SMAIL: autotag {'enabled' if AUTOTAG else 'disabled'}")
        case "starttls":
            starttls()
    return

print()
print()
threading.Thread(target=reader, daemon=True).start()

while True:
    cmd = input(f"\r{INSTR}")
    if cmd.lower().startswith("smail"):
        scommand(cmd.lower()[6:])
        continue
    elif cmd != "":
        if cmd[0] == "$":
            cmd = base64.b64encode(cmd[1:].encode()).decode()
    send(cmd)
