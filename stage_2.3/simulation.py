import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from cost import Cost
from market import Market
from company import CompanyDynamic, CompanyStatic
from strategy import StrategyDynamic, StrategyStatic

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

def plot_results(results, companyA_capacity, companyB_capacity):
    (
        profits_A_per_period,
        profits_B_per_period,
        prices_A_early_list,
        prices_A_last_list,
        production_A_list,
        inventory_A_list,
        dA_early_list,
        dA_lm_list,
        dB_early_list,
        dB_lm_list,
        soldB_list,
        market_share_A_list,
        market_share_B_list,
        unit_cost_A_list,
        fixed_cost_A_list,
        unit_cost_B_list,
        fixed_cost_B_list,
        prices_B_early_list,
        prices_B_last_list,
        production_B_list,
        inventory_B_list,
        slots_last_minute_A_list,
        slots_long_term_A_list,
        fixed_percentage_list  # Fester Prozentsatz
    ) = results

    cumulative_profit_A = np.cumsum(profits_A_per_period)
    cumulative_profit_B = np.cumsum(profits_B_per_period)
    oee_A = np.array(production_A_list) / companyA_capacity
    oee_B = np.array(production_B_list) / companyB_capacity

    # Verkäufe von A = dA_early + dA_lm
    soldA_list = [dA_early_list[i] + dA_lm_list[i] for i in range(len(dA_early_list))]

    # Erster Tab
    plt.figure(figsize=(24, 24))

    # 1. Gewinne pro Periode
    plt.subplot(5, 3, 1)
    plt.plot(profits_A_per_period, label='Gewinn A', marker='o')
    plt.plot(profits_B_per_period, label='Gewinn B', marker='x')
    plt.title('Gewinn pro Periode')
    plt.xlabel('Periode')
    plt.ylabel('Gewinn')
    plt.legend()

    # 2. Kumulierte Gewinne
    plt.subplot(5, 3, 2)
    plt.plot(cumulative_profit_A, label='Kumulierte Gewinne A', marker='o')
    plt.plot(cumulative_profit_B, label='Kumulierte Gewinne B', marker='x')
    plt.title('Kumulierte Gewinne')
    plt.xlabel('Periode')
    plt.ylabel('Kumulierte Gewinne')
    plt.legend()

    # 3. Preise von A (Early/Last)
    plt.subplot(5, 3, 3)
    plt.plot(prices_A_early_list, label='A Frühbucher Preis', marker='o')
    plt.plot(prices_A_last_list, label='A Last-Minute Preis', marker='x')
    plt.title('Preisentwicklung A')
    plt.xlabel('Periode')
    plt.ylabel('Preis')
    plt.legend()

    # 4. Auslastung (OEE)
    plt.subplot(5, 3, 4)
    plt.plot(oee_A, label='OEE A', marker='o')
    plt.plot(oee_B, label='OEE B', marker='x')
    plt.title('Auslastung (OEE)')
    plt.xlabel('Periode')
    plt.ylabel('OEE')
    plt.legend()

    # 5. Nachfrage A und B
    plt.subplot(5, 3, 5)
    plt.plot(dA_early_list, label='A Frühbucher Nachfrage', marker='o')
    plt.plot(dA_lm_list, label='A Last-Minute Nachfrage', marker='x')
    plt.plot(dB_early_list, label='B Frühbucher Nachfrage', linestyle='--', marker='o')
    plt.plot(dB_lm_list, label='B Last-Minute Nachfrage', linestyle='--', marker='x')
    plt.title('Nachfrageentwicklung')
    plt.xlabel('Periode')
    plt.ylabel('Nachfrage')
    plt.legend()

    # 6. Produktion und Inventar A
    plt.subplot(5, 3, 6)
    plt.plot(production_A_list, label='Produktion A', marker='o')
    plt.plot(inventory_A_list, label='Lagerbestand A', marker='x')
    plt.title('Produktion und Lagerbestand A')
    plt.xlabel('Periode')
    plt.ylabel('Menge')
    plt.legend()

    # 7. Marktanteile
    plt.subplot(5, 3, 7)
    plt.plot(market_share_A_list, label='Marktanteil A', marker='o')
    plt.plot(market_share_B_list, label='Marktanteil B', marker='x')
    plt.title('Marktanteilsentwicklung')
    plt.xlabel('Periode')
    plt.ylabel('Marktanteil')
    plt.legend()

    # 8. Verkäufe von B
    plt.subplot(5, 3, 8)
    plt.plot(soldB_list, label='Verkäufe B', marker='o')
    plt.title('Verkäufe von B')
    plt.xlabel('Periode')
    plt.ylabel('Verkäufe')
    plt.legend()

    # 9. Lagerbestand vs. Puffer A
    plt.subplot(5, 3, 9)
    plt.plot(inventory_A_list, label='Lagerbestand A', marker='o')
    plt.axhline(y=20, color='r', linestyle='--', label='Puffer Grenze')
    plt.title('Lagerbestand A vs. Puffer')
    plt.xlabel('Periode')
    plt.ylabel('Lagerbestand')
    plt.legend()

    # 10. Last-Minute-Preise vs. Gewinne A
    plt.subplot(5, 3, 10)
    plt.plot(prices_A_last_list, label='Last-Minute Preis A', marker='o')
    plt.plot(profits_A_per_period, label='Gewinn A', marker='x')
    plt.title('Last-Minute Preise vs. Gewinne A')
    plt.xlabel('Periode')
    plt.ylabel('Werte')
    plt.legend()

    # 11. Produktionsauslastung und freie Slots A
    plt.subplot(5, 3, 11)
    used_slots_A = np.array(slots_last_minute_A_list) + np.array(slots_long_term_A_list)
    free_slots_A = companyA_capacity - used_slots_A
    plt.bar(range(len(used_slots_A)), used_slots_A, label='Genutzte Slots A', alpha=0.7, color='blue')
    plt.bar(range(len(free_slots_A)), free_slots_A, bottom=used_slots_A, label='Freie Slots A', alpha=0.7, color='lightblue')
    plt.title('Produktionsauslastung A')
    plt.xlabel('Periode')
    plt.ylabel('Slots')
    plt.legend()

    # 12. Produktionsslots-Verteilung A
    plt.subplot(5, 3, 12)
    ind = np.arange(len(slots_last_minute_A_list))
    width = 0.6
    plt.bar(ind, slots_last_minute_A_list, width, label='Last-Minute', color='skyblue')
    plt.bar(ind, slots_long_term_A_list, width, bottom=slots_last_minute_A_list, label='Langfristig', color='orange')
    plt.title('Produktionsslots-Verteilung A')
    plt.xlabel('Periode')
    plt.ylabel('Slots')
    plt.legend()

    # 13. Festgelegter Prozentsatz für Langfristige Slots
    plt.subplot(5, 3, 13)
    plt.plot(fixed_percentage_list, label='Fester Prozentsatz Langfristig (%)', marker='o', color='green')
    plt.title('Fester Prozentsatz Langfristige Slots')
    plt.xlabel('Periode')
    plt.ylabel('Prozentsatz (%)')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Zweiter Tab
    plt.figure(figsize=(20, 12))
    # 1. Kostenentwicklung A und B (fixe und variable)
    plt.subplot(2, 3, 1)
    plt.plot(fixed_cost_A_list, label='Fixkosten/Einheit A', marker='o')
    plt.plot(unit_cost_A_list, label='Var.Kosten/Einheit A', marker='x')
    plt.plot(fixed_cost_B_list, label='Fixkosten/Einheit B', marker='o', linestyle='--')
    plt.plot(unit_cost_B_list, label='Var.Kosten/Einheit B', marker='x', linestyle='--')
    plt.title('Kostenentwicklung pro Einheit')
    plt.xlabel('Periode')
    plt.ylabel('Kosten/Einheit')
    plt.legend()

    # 2. Preisentwicklung B
    plt.subplot(2, 3, 2)
    plt.plot(prices_B_early_list, label='B Frühbucher Preis', marker='o')
    plt.plot(prices_B_last_list, label='B Last-Minute Preis', marker='x')
    plt.title('Preisentwicklung B')
    plt.xlabel('Periode')
    plt.ylabel('Preis')
    plt.legend()

    # 3. Produktion und Lagerbestand B
    plt.subplot(2, 3, 3)
    plt.plot(production_B_list, label='Produktion B', marker='o')
    plt.plot(inventory_B_list, label='Lagerbestand B', marker='x')
    plt.title('Produktion und Lagerbestand B')
    plt.xlabel('Periode')
    plt.ylabel('Menge')
    plt.legend()

    # 4. Vergleich verkaufte Menge A und B
    plt.subplot(2, 3, 4)
    plt.plot(soldA_list, label='Verkäufe A', marker='o')
    plt.plot(soldB_list, label='Verkäufe B', marker='x')
    plt.title('Verkäufe A vs B')
    plt.xlabel('Periode')
    plt.ylabel('Verkäufe')
    plt.legend()

    plt.tight_layout()
    plt.show()


def run_simulation():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Importieren der notwendigen Klassen
    from cost import Cost
    from market import Market
    from company import CompanyDynamic, CompanyStatic
    from strategy import StrategyDynamic, StrategyStatic

    # Initialisieren der Kostenstrukturen
    costA = Cost(fixed_cost=500, marginal_cost=25, raw_material_price=10, inventory_holding_cost=2)
    costB = Cost(fixed_cost=500, marginal_cost=25, raw_material_price=10, inventory_holding_cost=2)

    # Initialisieren der Unternehmen
    compA = CompanyDynamic(name='A', capacity=550, cost=costA, base_price=100, inventory=0)
    compB = CompanyStatic(name='B', capacity=550, cost=costB, base_price=100)

    # Initialisieren des Marktes
    market = Market()

    # Initialisieren der Strategien
    strategyA = StrategyDynamic(fixed_long_term_percentage=0.3)  # 30% fest für Langfristig
    strategyB = StrategyStatic()

    periods = 30
    profitA = 0
    profitB = 0

    # Listen für Ergebnisse
    profits_A_per_period = []
    profits_B_per_period = []
    prices_A_early_list = []
    prices_A_last_list = []
    production_A_list = []
    inventory_A_list = []
    dA_early_list = []
    dA_lm_list = []
    dB_early_list = []
    dB_lm_list = []
    soldB_list = []
    unit_cost_A_list = []
    fixed_cost_A_list = []
    market_share_A_list = []
    market_share_B_list = []

    # Daten für B
    unit_cost_B_list = []
    fixed_cost_B_list = []
    prices_B_early_list = []
    prices_B_last_list = []
    production_B_list = []
    inventory_B_list = []

    # Zusätzliche Listen für Produktionsslots von A
    slots_last_minute_A_list = []
    slots_long_term_A_list = []
    fixed_percentage_list = []

    # Initial Preis für B
    compB.base_price = 100  # Startpreis

    for t in range(periods):
        try:
            # Variiere den Puffer zufällig zwischen -5 und +5, Mindestpuffer 0
            buffer_variation = np.random.randint(-5, 6)
            new_buffer = max(0, 200 + buffer_variation)
            compA.set_buffer_stock(new_buffer)

            unit_cost_A = costA.total_unit_cost()
            fix_cost_per_unit_A = costA.fixed_cost / compA.capacity

            unit_cost_B = costB.total_unit_cost()
            fix_cost_per_unit_B = costB.fixed_cost / compB.capacity

            # Unternehmen A trifft Entscheidung
            compA.use_strategy(strategyA, price_B_early=compB.base_price, price_B_last=compB.base_price, market=market)
            # Ergebnis von A
            (pe, pl, prodA, invA, profitA_period, dA_early, dA_lm,
             slots_last_minute_A, slots_long_term_A, fixed_percentage) = compA.last_decision

            # Debugging: Werte von pe und pl
            print(f"Periode {t+1}:")
            print(f"  A Frühbucher Preis (pe): {pe}")
            print(f"  A Last-Minute Preis (pl): {pl}")

            # Überprüfen, ob pl korrekt ist
            if pl == 0:
                print(f"  Warnung: Last-Minute Preis (pl) in Periode {t+1} ist 0.")

            profits_A_per_period.append(profitA_period)
            profitA += profitA_period

            dA_early_list.append(dA_early)
            dA_lm_list.append(dA_lm)
            production_A_list.append(prodA)
            inventory_A_list.append(invA)
            prices_A_early_list.append(pe)
            prices_A_last_list.append(pl)
            unit_cost_A_list.append(unit_cost_A)
            fixed_cost_A_list.append(fix_cost_per_unit_A)

            # Produktionsslots für A speichern
            slots_last_minute_A_list.append(slots_last_minute_A)
            slots_long_term_A_list.append(slots_long_term_A)
            fixed_percentage_list.append(fixed_percentage)

            # Unternehmen B passt seinen Preis leicht an
            compB.adjust_price(strategyB, competitor_price=pe)
            prices_B_early = compB.base_price
            prices_B_last = compB.base_price
            prices_B_early_list.append(prices_B_early)
            prices_B_last_list.append(prices_B_last)

            # Nachfrage berechnen
            dA_early_val, dA_lm_val, dB_early_val, dB_lm_val = market.generate_demands(pe, prices_B_early, pl, prices_B_last)

            # Debugging: Nachfragewerte
            print(f"  Nachfrage A Frühbucher: {dA_early_val}")
            print(f"  Nachfrage A Last-Minute: {dA_lm_val}")
            print(f"  Nachfrage B Frühbucher: {dB_early_val}")
            print(f"  Nachfrage B Last-Minute: {dB_lm_val}")

            # Nachfrage von B hinzufügen
            dB_early_list.append(dB_early_val)
            dB_lm_list.append(dB_lm_val)

            # Unternehmen B trifft einfache Entscheidung
            pB_period, soldB = compB.simple_decision(dB_early_val, dB_lm_val)
            profits_B_per_period.append(pB_period)
            profitB += pB_period
            soldB_list.append(soldB)

            # B hat keine Inventarführung, daher 0
            inventory_B_list.append(0)
            production_B_list.append(soldB)

            # Fixe und variable Kosten für B
            unit_cost_B_list.append(unit_cost_B)
            fixed_cost_B_list.append(fix_cost_per_unit_B)

            # Marktanteile berechnen
            total_market = (dA_early + dA_lm) + (dB_early_val + dB_lm_val)
            if total_market > 0:
                market_share_A = (dA_early + dA_lm) / total_market
                market_share_B = (dB_early_val + dB_lm_val) / total_market
            else:
                market_share_A = 0.5
                market_share_B = 0.5

            market_share_A_list.append(market_share_A)
            market_share_B_list.append(market_share_B)

            # Debugging: Fixkosten pro Einheit
            print(f"  Fixkosten pro Einheit A: {fix_cost_per_unit_A}")
            print(f"  Fixkosten pro Einheit B: {fix_cost_per_unit_B}")

            # Kosten anpassen
            costA.update_fixed_costs(0.01)
            costB.update_fixed_costs(0.01)
            costA.update_marginal_costs(0.05)
            costB.update_marginal_costs(0.05)
            costA.update_raw_material_price(0.05)
            costB.update_raw_material_price(0.05)

            print(f"  Fixkosten nach Anpassung A: {costA.fixed_cost}")
            print(f"  Fixkosten nach Anpassung B: {costB.fixed_cost}")
            print("  ---------------------------------------")

        except Exception as e:
            print(f"Fehler in Periode {t+1}: {e}")
            # Optional: Stop the execution
            # break

    print("Kumulierter Gewinn A:", profitA)
    print("Kumulierter Gewinn B:", profitB)

    results = (
        profits_A_per_period,
        profits_B_per_period,
        prices_A_early_list,
        prices_A_last_list,
        production_A_list,
        inventory_A_list,
        dA_early_list,
        dA_lm_list,
        dB_early_list,
        dB_lm_list,
        soldB_list,
        market_share_A_list,
        market_share_B_list,
        unit_cost_A_list,
        fixed_cost_A_list,
        unit_cost_B_list,
        fixed_cost_B_list,
        prices_B_early_list,
        prices_B_last_list,
        production_B_list,
        inventory_B_list,
        slots_last_minute_A_list,
        slots_long_term_A_list,
        fixed_percentage_list  # Fester Prozentsatz
    )

    # Plots anzeigen
    plot_results(results, compA.capacity, compB.capacity)

    # Daten in XLSX speichern
    data = {
        'Periode': list(range(1, periods + 1)),
        'Gewinn_A': profits_A_per_period,
        'Gewinn_B': profits_B_per_period,
        'A_Frühbucher_Preis': prices_A_early_list,
        'A_LastMinute_Preis': prices_A_last_list,
        'B_Frühbucher_Preis': prices_B_early_list,
        'B_LastMinute_Preis': prices_B_last_list,
        'Produktion_A': production_A_list,
        'Inventar_A': inventory_A_list,
        'Produktion_B': production_B_list,
        'Inventar_B': inventory_B_list,
        'A_Frühbucher_Nachfrage': dA_early_list,
        'A_LastMinute_Nachfrage': dA_lm_list,
        'B_Frühbucher_Nachfrage': dB_early_list,
        'B_LastMinute_Nachfrage': dB_lm_list,
        'Verkaufte_Menge_B': soldB_list,
        'Marktanteil_A': market_share_A_list,
        'Marktanteil_B': market_share_B_list,
        'Var_Kosten_A/Einheit': unit_cost_A_list,
        'Fix_Kosten_A/Einheit': fixed_cost_A_list,
        'Var_Kosten_B/Einheit': unit_cost_B_list,
        'Fix_Kosten_B/Einheit': fixed_cost_B_list,
        # Neue Slot-Daten hinzufügen
        'Slots_LastMinute_A': slots_last_minute_A_list,
        'Slots_Langfristig_A': slots_long_term_A_list,
        'Fixed_LongTerm_Percentage_A': fixed_percentage_list,  # Fester Prozentsatz
    }

    # Überprüfen, ob alle Listen die gleiche Länge haben
    print("\nÜberprüfung der Listenlängen:")
    expected_length = periods
    all_lengths = {key: len(value) for key, value in data.items()}
    for key, length in all_lengths.items():
        print(f"{key}: {length} (erwartet: {expected_length})")

    if all(length == expected_length for length in all_lengths.values()):
        df = pd.DataFrame(data)
        df.to_excel("results.xlsx", index=False)
        print("\nErgebnisse wurden in results.xlsx gespeichert.")
    else:
        print("\nFehler: Nicht alle Listen haben die gleiche Länge.")
        for key, length in all_lengths.items():
            if length != expected_length:
                print(f"  {key}: {length} (erwartet: {expected_length})")
        # Optional: Stop the execution
        # exit(1)


if __name__ == "__main__":
    run_simulation()
