from product import Product
from utils import generate_quantities, generate_parameters, calculate_total_time

def main():
    # 1. Genera quantità e parametri
    quantities = generate_quantities()
    params = generate_parameters()
    
    # 2. Crea oggetti Product
    products = [
        Product("bun", quantities["bun"], params["unit_time"]["bun"]),
        Product("chicken", quantities["chicken"], params["unit_time"]["chicken"]),
        Product("fries", quantities["fries"], params["unit_time"]["fries"])
    ]
    
    # 3. Calcola tempo totale e giorni lavorativi reali basati sulla capacità giornaliera
    total_minutes, total_days = calculate_total_time(
        products,
        params["daily_capacity"],
        params["setup_time"],
        params["machine_failure_chance"],
        params["defect_rate"],
        params["operator_efficiency"],
        params["material_shortage_chance"]
    )
    
    # 4. Output
    print("=== Simulazione Produzione ===\n")
    
    print("Quantità da produrre:")
    for p in products:
        print(f" - {p.name.capitalize()}: {p.quantity} unità")
    
    print("\nParametri di produzione:")
    print(f" - Tempo unitario (min/unit): {params['unit_time']}")
    print(f" - Capacità giornaliera: {params['daily_capacity']} min")
    print(f" - Tempo setup tra prodotti: {params['setup_time']} min")
    print(f" - Probabilità guasto linea: {params['machine_failure_chance']}%")
    print(f" - Percentuale prodotti difettosi: {params['defect_rate']}%")
    print(f" - Efficienza operatori: {params['operator_efficiency']}%")
    print(f" - Probabilità carenza materiali: {params['material_shortage_chance']}%\n")
    
    print("Tempo totale per prodotto:")
    for p in products:
        print(f" - {p.name.capitalize()}: {round(p.total_time(), 2)} minuti totali")
    
    # 5. Conversione totale in ore e minuti
    total_hours = total_minutes / 60
    hours = int(total_hours)
    minutes = int(total_minutes % 60)
    
    print(f"\nTempo totale produzione: {round(total_minutes, 2)} minuti (comprensivo di setup e imprevisti)")
    print(f"≈ {round(total_hours, 2)} ore di lavoro")
    
    # 6. Giorni lavorativi standard (8h = 480 min)
    total_days_standard = total_minutes / 480
    print(f"Stima giorni lavorativi (1 turno da 8h/giorno): {round(total_days_standard, 2)} giorni")
    
    # 7. Giorni lavorativi reali basati sulla capacità giornaliera generata
    if params["daily_capacity"] > 480:
        note = "Avendo più di 1 turno di produzione al giorno, i giorni stimati si riducono proporzionalmente."
    else:
        note = "Avendo 1 turno di produzione al giorno, i giorni stimati sono quelli standard."
    
    print(f"Giorni lavorativi reali (capacità giornaliera = {params['daily_capacity']} min): "
          f"{round(total_days, 2)} giorni ({note})")
    
    print(f"Che equivale a circa: {hours} ore e {minutes} minuti di lavoro")

if __name__ == "__main__":
    main()
