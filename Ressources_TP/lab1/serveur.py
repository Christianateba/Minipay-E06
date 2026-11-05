import socket, time

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 5000))
s.listen()
print("Serveur en attente sur le port 5000")
compteur = 0
deja = set()                       # identifiants déjà traités
while True:
    conn, addr = s.accept()
    data = conn.recv(1024).decode()
    pid, _, msg = data.partition(" ")
    if pid in deja:
        print("doublon ignoré :", pid)
        reponse = "OK deja_traite " + msg
    else:
        deja.add(pid)
        compteur += 1              # le paiement est exécuté
        print("paiements exécutés :", compteur)
        time.sleep(3)              # plus long que le timeout du client
        reponse = "OK " + msg
    try:
        conn.sendall(reponse.encode())
    except OSError:
        pass                       # le client est déjà parti
    conn.close()