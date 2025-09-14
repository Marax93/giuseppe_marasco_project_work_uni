import random # Importa il modulo random, utile per generare numeri casuali

# In questo file vengono definite le funzioni utili per l'esecuzione del programma che avverà nel main.py

# Genera casualmente le quantità da produrre per ogni tipologia di prodotto.
def generate_quantities():
    return {
        "bun": random.randint(20000, 50000),       # Panini (tra 20.000 e 50.000 pezzi)
        "chicken": random.randint(10000, 30000),   # Filetti di pollo (tra 10.000 e 30.000 pezzi)
        "fries": random.randint(15000, 40000)      # Porzioni di patatine (tra 15.000 e 40.000 pezzi)
    }

# Genera casualmente i parametri di configurazione della produzione.
def generate_parameters():
    return {
        # Tempo unitario per ciascun prodotto
        "unit_time": {
            "bun": round(random.uniform(0.05, 0.07), 3),      # 3–4 sec per panino
            "chicken": round(random.uniform(0.10, 0.14), 3),  # 6–8 sec per filetto
            "fries": round(random.uniform(0.03, 0.05), 3)     # 2–3 sec per porzione
        },
        
        # Capacità massima giornaliera in minuti, scelta tra 1, 2 o 3 turni da 8 ore
        # 1 turno = 480 min, 2 turni = 960 min, 3 turni = 1440 min
        "daily_capacity": random.choice([480, 960, 1440]),
        
        # Tempo di setup (cambio linea) tra prodotti (in minuti)
        "setup_time": random.randint(45, 90),
        
        # Probabilità che la linea si fermi per un guasto (%)
        "machine_failure_chance": round(random.uniform(0, 5), 2),
        
        # Percentuale di prodotti difettosi da rifare (%)
        "defect_rate": round(random.uniform(0, 2), 2),
        
        # Efficienza media degli operatori (%)
        "operator_efficiency": round(random.uniform(80, 100), 2),
        
        # Probabilità che ci siano ritardi per mancanza di materiali (%)
        "material_shortage_chance": round(random.uniform(0, 5), 2)
    }

# Calcola il tempo totale di produzione per un lotto di prodotti considerando parametri realistici.
def calculate_total_time(products, daily_capacity, setup_time, machine_failure_chance=0,
                         defect_rate=0, operator_efficiency=100, material_shortage_chance=0):

    # 1. Calcolo del tempo totale iniziale sommando i tempi di produzione di ciascun prodotto utilizzando la funzione somma e un ciclo for compatto
    total_minutes = sum([p.total_time() for p in products])

    # 2. Aggiungo il tempo di setup per i cambi di produzione tra i prodotti
    # (numero di cambi = numero di prodotti - 1)
    total_minutes += (len(products) - 1) * setup_time

    # 3. Considero il tempo perso per guasti della macchina
    total_minutes *= (1 + machine_failure_chance / 100)

    # 4. Considero il tempo aggiuntivo dovuto ai prodotti difettosi da rifare
    total_minutes *= (1 + defect_rate / 100)

    # 5. Considero l'efficienza degli operatori: meno efficienza -> più tempo richiesto
    total_minutes *= (100 / operator_efficiency)

    # 6. Considero eventuali ritardi per carenza di materiali
    total_minutes *= (1 + material_shortage_chance / 100)

    # 7. Calcolo i giorni necessari dividendo per la capacità giornaliera (480/960/1440 min)
    total_days = total_minutes / daily_capacity

    # 8. Ritorno il tempo totale in minuti e i giorni necessari
    return total_minutes, total_days
