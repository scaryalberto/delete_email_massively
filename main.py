import imaplib
import datetime

# Credenziali per l'account IMAP
username = "scaryalberto@hotmail.it"
password = "CiaoPippa93"
imap_server = 'outlook.office365.com'

# Stabilisci la connessione IMAP
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, password)

# Seleziona la casella di posta
imap.select("INBOX")

# Calcola la data attuale
today = datetime.date.today()

# Calcola la data di 4 anni fa
four_years_ago = today - datetime.timedelta(days=10*365)

# Crea una query per cercare email dall'anno scorso fino al giorno prima di 4 anni fa
search_query = f"SINCE {four_years_ago.strftime('%d-%b-%Y')} BEFORE {today.strftime('%d-%b-%Y')}"

# Esegui la ricerca
_, search_results = imap.search(None, search_query)

# Stampa i messaggi trovati
for message_id in search_results[0].split():
    print(f"Email trovata: {message_id}")
    imap.store(message_id, "+FLAGS", "\\Deleted")

# Chiudi la connessione e esci
imap.close()
imap.logout()
