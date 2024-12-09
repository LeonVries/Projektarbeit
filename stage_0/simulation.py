import numpy as np
import matplotlib.pyplot as plt
from company import Company
from market import Market

if __name__ == "__main__":
    # Initialisierung der Unternehmen
    company1 = Company(alpha=100, beta=10, gamma=5, marginal_cost=20, name="Unternehmen 1")
    company2 = Company(alpha=100, beta=10, gamma=5, marginal_cost=20, name="Unternehmen 2")

    # Marktmodell
    market = Market(company1, company2)

    # Nash-Gleichgewicht berechnen
    p1_star, p2_star = market.calculate_nash_equilibrium()
    print(f"Nash-Gleichgewicht:")
    print(f"Preis von {company1.name}: p1* = {p1_star:.2f}")
    print(f"Preis von {company2.name}: p2* = {p2_star:.2f}")

    # Reaktionsfunktionen visualisieren
    p_range = np.linspace(0, 50, 500)
    p1_values = [company1.reaction_price(p2) for p2 in p_range]
    p2_values = [company2.reaction_price(p1) for p1 in p_range]

    plt.figure(figsize=(10, 6))

    plt.plot(p_range, p1_values, label=f'Reaktionsfunktion von {company1.name}', color='blue')
    plt.plot(p2_values, p_range, label=f'Reaktionsfunktion von {company2.name}', color='red')

    # Nash-Gleichgewichtspunkt
    plt.plot(p1_star, p2_star, 'go', label='Nash-Gleichgewicht')

    # Begrenzung des Diagramms
    plt.xlim(0, 50)
    plt.ylim(0, 50)

    # Achsenbeschriftungen und Titel
    plt.xlabel(f'Preis von {company1.name}, p1')
    plt.ylabel(f'Preis von {company2.name}, p2')
    plt.title('Reaktionsfunktionen im Bertrand-Modell mit Nash-Gleichgewicht')
    plt.legend()
    plt.grid(True)
    plt.show()
