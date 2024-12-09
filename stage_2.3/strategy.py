from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus
import numpy as np


from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus

class StrategyDynamic:
    def __init__(self, early_price_candidates=[60, 80, 100, 120, 140],
                 last_price_candidates=[80, 120, 160, 200],
                 slot_price_adjustments={'last_minute': 1.2, 'long_term': 0.9},
                 fixed_long_term_percentage=0.3):  # 30% fest für Langfristig
        self.early_price_candidates = early_price_candidates
        self.last_price_candidates = last_price_candidates
        self.slot_price_adjustments = slot_price_adjustments
        self.fixed_long_term_percentage = fixed_long_term_percentage

    def optimize_decision(self, company, price_B_early, price_B_last, market):
        scenarios = []
        for pe in self.early_price_candidates:
            for pl in self.last_price_candidates:
                dA_early, dA_lm, dB_early, dB_lm = market.generate_demands(pe, price_B_early, pl, price_B_last)
                
                # Produktionszuweisungen basierend auf festen und dynamischen Slots
                slots_long_term = self.fixed_long_term_percentage * company.capacity
                slots_last_minute = company.capacity - slots_long_term
                
                # Produktion basierend auf Nachfrage und Kapazität
                prod_long_term = min(dA_early, slots_long_term)
                prod_last_minute = min(dA_lm, slots_last_minute)
                
                # Inventar am Ende
                inv_end = company.inventory + (prod_last_minute + prod_long_term) - (dA_early + dA_lm)
                
                # **Angepasste Buffer-Stock-Bedingung**
                if inv_end < 0:
                    profit_i = -float('inf')  # Unzulässiges Szenario
                else:
                    # Einnahmen berechnen
                    revenue = (prod_last_minute * pe * self.slot_price_adjustments['last_minute'] +
                               prod_long_term * pe * self.slot_price_adjustments['long_term'])
                    
                    # Kosten berechnen
                    cost = (company.cost.fixed_cost +
                            (prod_last_minute + prod_long_term) * company.cost.total_unit_cost() +
                            inv_end * company.cost.inventory_holding_cost)
                    
                    # Gewinn berechnen
                    profit_i = revenue - cost

                scenarios.append({
                    'pe': pe,
                    'pl': pl,
                    'profit': profit_i,
                    'prod_total': prod_last_minute + prod_long_term,
                    'inventory_end': inv_end,
                    'dA_early': dA_early,
                    'dA_lm': dA_lm,
                    'prod_last_minute': prod_last_minute,
                    'prod_long_term': prod_long_term,
                    'fixed_percentage': self.fixed_long_term_percentage * 100  # in Prozent
                })

        # Debugging: Szenarien anzeigen
        print(f"Anzahl der Szenarien: {len(scenarios)}")
        for idx, scenario in enumerate(scenarios):
            print(f"Szenario {idx + 1}: pe={scenario['pe']}, pl={scenario['pl']}, profit={scenario['profit']}, inv_end={scenario['inventory_end']}")

        # Erstellen des LP-Modells
        model = LpProblem("A_decision", LpMaximize)

        # Entscheidungsvariablen: Auswahl eines Szenarios
        x = {i: LpVariable(f"x_{i}", cat='Binary') for i in range(len(scenarios))}

        # Zielfunktion: Maximierung des Gewinns
        model += lpSum([x[i] * scenarios[i]['profit'] for i in range(len(scenarios))]), "Total_Profit"

        # Einschränkung: Nur ein Szenario darf ausgewählt werden
        model += lpSum(x.values()) == 1, "One_scenario"

        # Modell lösen
        model.solve()

        # Überprüfen, welches Szenario gewählt wurde
        chosen = None
        for i in x:
            if x[i].varValue > 0.5:
                chosen = i
                break

        if chosen is not None and scenarios[chosen]['profit'] != -float('inf'):
            chosen_scenario = scenarios[chosen]
            return (
                chosen_scenario['pe'],
                chosen_scenario['pl'],
                chosen_scenario['prod_total'],
                chosen_scenario['inventory_end'],
                chosen_scenario['profit'],
                chosen_scenario['dA_early'],
                chosen_scenario['dA_lm'],
                chosen_scenario['prod_last_minute'],
                chosen_scenario['prod_long_term'],
                chosen_scenario['fixed_percentage']
            )
        else:
            # Fallback, falls kein Szenario gewählt wurde
            print("Keine zulässigen Szenarien gefunden.")
            return (company.base_price, 100, 0, company.inventory, 0, 0, 0, 0, 0, 0)
