import socket, uuid

pid = str(uuid.uuid4())            # identifiant unique du paiement
for essai in range(2):
    try:
        c = socket.create_connection(("127.20.0.1", 5000), timeout=2)
        c.sendall((pid + " payer 5000").encode())
        print(c.recv(1024).decode()); break
    except OSError as e:
        print("Essai", essai + 1, "échoué :", e)