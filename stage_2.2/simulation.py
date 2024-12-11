import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from cost import Cost
from market import Market
from company import CompanyDynamic, CompanyStatic
from strategy import StrategyDynamic, StrategyStatic

def plot_results(results, companyA_capacity, companyB_capacity):
    (
        profits_A_per_period, profits_B_per_period, prices_A_early_list, prices_A_last_list,
        production_A_list, inventory_A_list, dA_early_est_list, dA_lm_est_list,
        dB_early_list, dB_lm_list, soldB_list, market_share_A_list, market_share_B_list,
        unit_cost_A_list, fixed_cost_A_list, unit_cost_B_list, fixed_cost_B_list,
        prices_B_early_list, prices_B_last_list, production_B_list, inventory_B_list,
        dA_early_val_list, dA_lm_val_list, actual_sales_A_list
    ) = results

    cumulative_profit_A = np.cumsum(profits_A_per_period)
    cumulative_profit_B = np.cumsum(profits_B_per_period)
    oee_A = np.array(production_A_list) / companyA_capacity
    oee_B = np.array(production_B_list) / companyB_capacity

    # Verkäufe von A = actual_sales_A_list
    soldA_list = actual_sales_A_list

    # Erster Tab
    plt.figure(figsize=(20, 18))
    # 1. Gewinne pro Periode
    plt.subplot(4, 3, 1)
    plt.plot(profits_A_per_period, label='Gewinn A', marker='o')
    plt.plot(profits_B_per_period, label='Gewinn B', marker='x')
    plt.title('Gewinn pro Periode')
    plt.xlabel('Periode')
    plt.ylabel('Gewinn')
    plt.legend()

    # 2. Kumulierte Gewinne
    plt.subplot(4, 3, 2)
    plt.plot(cumulative_profit_A, label='Kumulierte Gewinne A', marker='o')
    plt.plot(cumulative_profit_B, label='Kumulierte Gewinne B', marker='x')
    plt.title('Kumulierte Gewinne')
    plt.xlabel('Periode')
    plt.ylabel('Kumulierte Gewinne')
    plt.legend()

    # 3. Preise von A (Early/Last)
    plt.subplot(4, 3, 3)
    plt.plot(prices_A_early_list, label='A Frühbucher Preis', marker='o')
    plt.plot(prices_A_last_list, label='A Last-Minute Preis', marker='x')
    plt.title('Preisentwicklung A')
    plt.xlabel('Periode')
    plt.ylabel('Preis')
    plt.legend()

    # 4. Auslastung (OEE)
    plt.subplot(4, 3, 4)
    plt.plot(oee_A, label='OEE A', marker='o')
    plt.plot(oee_B, label='OEE B', marker='x')
    plt.title('Auslastung (OEE)')
    plt.xlabel('Periode')
    plt.ylabel('OEE')
    plt.legend()

    # 5. Nachfrage A und B (geschätzt)
    plt.subplot(4, 3, 5)
    plt.plot(dA_early_est_list, label='A Frühbucher Nachfrage (geschätzt)', marker='o')
    plt.plot(dA_lm_est_list, label='A Last-Minute Nachfrage (geschätzt)', marker='x')
    plt.plot(dB_early_list, label='B Frühbucher Nachfrage (geschätzt)', linestyle='--', marker='o')
    plt.plot(dB_lm_list, label='B Last-Minute Nachfrage (geschätzt)', linestyle='--', marker='x')
    plt.title('Nachfrageentwicklung (geschätzt)')
    plt.xlabel('Periode')
    plt.ylabel('Nachfrage')
    plt.legend()

    # 6. Produktion und Inventar A
    plt.subplot(4, 3, 6)
    plt.plot(production_A_list, label='Produktion A', marker='o')
    plt.plot(inventory_A_list, label='Lagerbestand A', marker='x')
    plt.title('Produktion und Lagerbestand A')
    plt.xlabel('Periode')
    plt.ylabel('Menge')
    plt.legend()

    # 7. Marktanteile
    plt.subplot(4, 3, 7)
    plt.plot(market_share_A_list, label='Marktanteil A', marker='o')
    plt.plot(market_share_B_list, label='Marktanteil B', marker='x')
    plt.title('Marktanteilsentwicklung')
    plt.xlabel('Periode')
    plt.ylabel('Marktanteil')
    plt.legend()

    # 8. Verkäufe von B
    plt.subplot(4, 3, 8)
    plt.plot(soldB_list, label='Verkäufe B', marker='o')
    plt.title('Verkäufe von B')
    plt.xlabel('Periode')
    plt.ylabel('Verkäufe')
    plt.legend()

    # 9. Lagerbestand A und B vs. Puffer
    plt.subplot(4, 3, 9)
    plt.plot(inventory_A_list, label='Lagerbestand A', marker='o')
    plt.plot(inventory_B_list, label='Lagerbestand B', marker='x')
    plt.axhline(y=20, color='r', linestyle='--', label='Puffer Grenze A')
    plt.axhline(y=20, color='g', linestyle='--', label='Puffer Grenze B')
    plt.title('Lagerbestand A und B vs. Puffer')
    plt.xlabel('Periode')
    plt.ylabel('Lagerbestand')
    plt.legend()

    # 10. Last-Minute-Preise vs. Gewinne A
    plt.subplot(4, 3, 10)
    plt.plot(prices_A_last_list, label='Last-Minute Preis A', marker='o')
    plt.plot(profits_A_per_period, label='Gewinn A', marker='x')
    plt.title('Last-Minute Preise vs. Gewinne A')
    plt.xlabel('Periode')
    plt.ylabel('Werte')
    plt.legend()

    # 11. Geschätzte vs. Tatsächliche Nachfrage A Frühbucher
    plt.subplot(4, 3, 11)
    plt.plot(dA_early_est_list, label='A Frühbucher Nachfrage (geschätzt)', marker='o')
    plt.plot(dA_early_val_list, label='A Frühbucher Nachfrage (tatsächlich)', marker='x')
    plt.title('Geschätzte vs. Tatsächliche Nachfrage A Frühbucher')
    plt.xlabel('Periode')
    plt.ylabel('Nachfrage')
    plt.legend()

    # 12. Geschätzte vs. Tatsächliche Nachfrage A Last-Minute
    plt.subplot(4, 3, 12)
    plt.plot(dA_lm_est_list, label='A Last-Minute Nachfrage (geschätzt)', marker='o')
    plt.plot(dA_lm_val_list, label='A Last-Minute Nachfrage (tatsächlich)', marker='x')
    plt.title('Geschätzte vs. Tatsächliche Nachfrage A Last-Minute')
    plt.xlabel('Periode')
    plt.ylabel('Nachfrage')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Neuer Overlay-Plot: Geschätzte vs. Tatsächliche Nachfrage A
    plt.figure(figsize=(20, 10))

    # Frühbucher Nachfrage
    plt.subplot(1, 2, 1)
    plt.plot(dA_early_est_list, label='Geschätzte Nachfrage (Frühbucher)', marker='o')
    plt.plot(dA_early_val_list, label='Tatsächliche Nachfrage (Frühbucher)', marker='x')
    plt.title('Geschätzte vs. Tatsächliche Nachfrage A Frühbucher')
    plt.xlabel('Periode')
    plt.ylabel('Nachfrage')
    plt.legend()

    # Last-Minute Nachfrage
    plt.subplot(1, 2, 2)
    plt.plot(dA_lm_est_list, label='Geschätzte Nachfrage (Last-Minute)', marker='o')
    plt.plot(dA_lm_val_list, label='Tatsächliche Nachfrage (Last-Minute)', marker='x')
    plt.title('Geschätzte vs. Tatsächliche Nachfrage A Last-Minute')
    plt.xlabel('Periode')
    plt.ylabel('Nachfrage')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Zweiter Tab
    plt.figure(figsize=(20, 16))
    # 1. Kostenentwicklung A und B (fixe und variable)
    plt.subplot(3, 2, 1)
    plt.plot(fixed_cost_A_list, label='Fixkosten/Einheit A', marker='o')
    plt.plot(unit_cost_A_list, label='Var.Kosten/Einheit A', marker='x')
    plt.plot(fixed_cost_B_list, label='Fixkosten/Einheit B', marker='o', linestyle='--')
    plt.plot(unit_cost_B_list, label='Var.Kosten/Einheit B', marker='x', linestyle='--')
    plt.title('Kostenentwicklung pro Einheit')
    plt.xlabel('Periode')
    plt.ylabel('Kosten/Einheit')
    plt.legend()

    # 2. Preisentwicklung B
    plt.subplot(3, 2, 2)
    plt.plot(prices_B_early_list, label='B Frühbucher Preis', marker='o')
    plt.plot(prices_B_last_list, label='B Last-Minute Preis', marker='x')
    plt.title('Preisentwicklung B')
    plt.xlabel('Periode')
    plt.ylabel('Preis')
    plt.legend()

    # 3. Produktion und Lagerbestand B
    plt.subplot(3, 2, 3)
    plt.plot(production_B_list, label='Produktion B', marker='o')
    plt.plot(inventory_B_list, label='Lagerbestand B', marker='x')
    plt.title('Produktion und Lagerbestand B')
    plt.xlabel('Periode')
    plt.ylabel('Menge')
    plt.legend()

    # 4. Vergleich verkaufte Menge A und B
    plt.subplot(3, 2, 4)
    plt.plot(soldA_list, label='Verkäufe A', marker='o')
    plt.plot(soldB_list, label='Verkäufe B', marker='x')
    plt.title('Verkäufe A vs B')
    plt.xlabel('Periode')
    plt.ylabel('Verkäufe')
    plt.legend()

    # 5. Abweichung Produktion A vs Tatsächliche Nachfrage A
    plt.subplot(3, 2, 5)
    actual_demand_A = np.array(dA_early_val_list) + np.array(dA_lm_val_list)
    production_A = np.array(production_A_list)
    deviation_A = production_A - actual_demand_A
    plt.plot(deviation_A, label='Produktion A - Tatsächliche Nachfrage A', marker='o')
    plt.title('Abweichung Produktion A vs Tatsächliche Nachfrage A')
    plt.xlabel('Periode')
    plt.ylabel('Abweichung (Menge)')
    plt.legend()

    # 6. Lagerbestand A im Vergleich zur tatsächlichen Nachfrage
    plt.subplot(3, 2, 6)
    plt.plot(inventory_A_list, label='Lagerbestand A', marker='o')
    plt.plot(actual_demand_A, label='Tatsächliche Nachfrage A', marker='x')
    plt.title('Lagerbestand A vs Tatsächliche Nachfrage A')
    plt.xlabel('Periode')
    plt.ylabel('Menge')
    plt.legend()

    plt.tight_layout()
    plt.show()


def run_simulation():
    # Initialisieren der Kostenstrukturen
    costA = Cost(fixed_cost=10000, marginal_cost=30, raw_material_price=15, inventory_holding_cost=2)
    costB = Cost(fixed_cost=10000, marginal_cost=30, raw_material_price=15, inventory_holding_cost=2)

    # Initialisieren der Unternehmen
    # Einheitliche Pufferbestände: 20 +/- Variation
    compA = CompanyDynamic(name='A', capacity=550, cost=costA, base_price=100, inventory=0, buffer_stock=200, demand_uncertainty=0.1)
    compB = CompanyStatic(name='B', capacity=550, cost=costB, base_price=100, inventory=0, buffer_stock=200, demand_uncertainty=0.1)

    # Initialisieren des Marktes
    market = Market()

    # Initialisieren der Strategien
    strategyA = StrategyDynamic(demand_uncertainty=0.1)  # 10% Unsicherheit
    strategyB = StrategyStatic()

    periods = 30
    profitA = 0
    profitB = 0

    profits_A_per_period = []
    profits_B_per_period = []
    prices_A_early_list = []
    prices_A_last_list = []
    production_A_list = []
    inventory_A_list = []
    dA_early_est_list = []  # Geschätzte Frühbucher-Nachfrage
    dA_lm_est_list = []    # Geschätzte Last-Minute-Nachfrage
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

    # Listen für tatsächliche Nachfrage von A
    dA_early_val_list = []
    dA_lm_val_list = []
    actual_sales_A_list = []

    # Initial Preis für B
    compB.base_price = 100  # Startpreis

    for t in range(periods):
        try:
            # Einheitliche Puffervariation für beide Unternehmen
            buffer_variation_A = np.random.randint(-5, 6)
            new_buffer_A = max(0, 20 + buffer_variation_A)
            compA.set_buffer_stock(new_buffer_A)

            unit_cost_A = costA.total_unit_cost()
            fix_cost_per_unit_A = costA.fixed_cost / compA.capacity

            unit_cost_B = costB.total_unit_cost()
            fix_cost_per_unit_B = costB.fixed_cost / compB.capacity

            # Debugging: Überprüfen der variablen Kosten
            print(f"Periode {t+1}:")
            print(f"  Variable Kosten A: {unit_cost_A}")
            print(f"  Variable Kosten B: {unit_cost_B}")

            # Unternehmen A trifft Entscheidung basierend auf geschätzter Nachfrage
            compA.use_strategy(strategyA, price_B_early=compB.base_price, price_B_last=compB.base_price, market=market)
            pe, pl, prodA, invA, profitA_period_est, dA_early_est, dA_lm_est = compA.last_decision

            # Debugging: Werte von pe und pl
            print(f"  A Frühbucher Preis (pe): {pe}")
            print(f"  A Last-Minute Preis (pl): {pl}")

            # Überprüfen, ob pl korrekt ist
            if pl == 0:
                print(f"  Warnung: Last-Minute Preis (pl) in Periode {t+1} ist 0.")

            # Speichern der geschätzten Daten
            dA_early_est_list.append(dA_early_est)
            dA_lm_est_list.append(dA_lm_est)
            production_A_list.append(prodA)
            inventory_A_list.append(invA)
            prices_A_early_list.append(pe)
            prices_A_last_list.append(pl)
            unit_cost_A_list.append(unit_cost_A)
            fixed_cost_A_list.append(fix_cost_per_unit_A)

            # Unternehmen B passt seinen Preis leicht an
            compB.adjust_price(strategyB, competitor_price=pe)
            prices_B_early = compB.base_price
            prices_B_last = compB.base_price
            prices_B_early_list.append(prices_B_early)
            prices_B_last_list.append(prices_B_last)

            # Tatsächliche Nachfrage berechnen (unabhängig von der Strategie)
            dA_early_val, dA_lm_val, dB_early_val, dB_lm_val = market.generate_demands(pe, prices_B_early, pl, prices_B_last)

            # Debugging: Nachfragewerte
            print(f"  Nachfrage A Frühbucher (tatsächlich): {dA_early_val}")
            print(f"  Nachfrage A Last-Minute (tatsächlich): {dA_lm_val}")
            print(f"  Nachfrage B Frühbucher (tatsächlich): {dB_early_val}")
            print(f"  Nachfrage B Last-Minute (tatsächlich): {dB_lm_val}")

            # **Wichtig: Nachfrage von B hinzufügen**
            dB_early_list.append(dB_early_val)
            dB_lm_list.append(dB_lm_val)

            # Speichern der tatsächlichen Nachfrage von A
            dA_early_val_list.append(dA_early_val)
            dA_lm_val_list.append(dA_lm_val)

            # Berechnung der tatsächlichen Verkäufe von A
            available_A = prodA + compA.inventory  # Produktion + Inventar
            actual_demand_A = dA_early_val + dA_lm_val
            actual_sales_A = min(available_A, actual_demand_A)
            actual_sales_A_list.append(actual_sales_A)

            # Aktualisierung des Inventars basierend auf tatsächlicher Nachfrage
            new_inventory_A = available_A - actual_sales_A
            compA.inventory = new_inventory_A
            inventory_A_list[-1] = new_inventory_A  # Update der letzten Inventar-Eintragung

            # Berechnung des tatsächlichen Gewinns von A
            revenue_A = actual_sales_A * pe  # Annahme: der Frühbucher-Preis wird für alle Verkäufe genutzt
            cost_A = prodA * costA.total_unit_cost() + new_inventory_A * costA.inventory_holding_cost
            profitA_period = revenue_A - cost_A
            profits_A_per_period.append(profitA_period)
            profitA += profitA_period

            # Unternehmen B trifft Entscheidung basierend auf tatsächlicher Nachfrage mit Unsicherheit
            pB_period, productionB, soldB = compB.simple_decision(dB_early_val, dB_lm_val)
            profits_B_per_period.append(pB_period)
            profitB += pB_period
            soldB_list.append(soldB)
            production_B_list.append(productionB)

            # B's Inventar aktualisieren
            inventory_B_list.append(compB.inventory)

            # Fixe und variable Kosten für B
            unit_cost_B_list.append(unit_cost_B)
            fixed_cost_B_list.append(fix_cost_per_unit_B)

            # Marktanteile
            total_market = actual_demand_A + (dB_early_val + dB_lm_val)
            if total_market > 0:
                market_share_A = actual_demand_A / total_market
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
        dA_early_est_list,  # Geschätzte Frühbucher-Nachfrage
        dA_lm_est_list,    # Geschätzte Last-Minute-Nachfrage
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
        dA_early_val_list,  # Tatsächliche Frühbucher-Nachfrage
        dA_lm_val_list,     # Tatsächliche Last-Minute-Nachfrage
        actual_sales_A_list  # Tatsächliche Verkäufe A
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
        'A_Frühbucher_Nachfrage_Geschätzt': dA_early_est_list,
        'A_LastMinute_Nachfrage_Geschätzt': dA_lm_est_list,
        'A_Frühbucher_Nachfrage_Tatsächlich': dA_early_val_list,
        'A_LastMinute_Nachfrage_Tatsächlich': dA_lm_val_list,
        'B_Frühbucher_Nachfrage': dB_early_list,
        'B_LastMinute_Nachfrage': dB_lm_list,
        'Verkaufte_Menge_A': actual_sales_A_list,
        'Verkaufte_Menge_B': soldB_list,
        'Marktanteil_A': market_share_A_list,
        'Marktanteil_B': market_share_B_list,
        'Var_Kosten_A_Einheit': unit_cost_A_list,
        'Fix_Kosten_A_Einheit': fixed_cost_A_list,
        'Var_Kosten_B_Einheit': unit_cost_B_list,
        'Fix_Kosten_B_Einheit': fixed_cost_B_list,
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
