# Dynamisches Bertrand-Duopol Modell

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Eine Python-Implementierung eines dynamischen Bertrand-Duopol Modells mit gradueller Preisanpassung und realistischer Marktaufteilung.

# Markt-Simulationsprojekt: Erweiterte Bertrand-Wettbewerbsmodelle

## 📝 Inhaltsverzeichnis

- [Einleitung](#einleitung)
  - [Projektstruktur nach VDI 3633](#projektstruktur-nach-vdi-3633)
- [Ausgangssituation und Ziel](#ausgangssituation-und-ziel)
  - [Ausgangssituation](#ausgangssituation)
  - [Ziel](#ziel)
- [Projekt-Roadmap](#projekt-roadmap)
  - [Evolutionsstufe 0](#evolutionsstufe-0)
  - [Evolutionsstufe 1](#evolutionsstufe-1)
  - [Evolutionsstufe 2](#evolutionsstufe-2)
- [Detaillierte Modellbeschreibungen](#detaillierte-modellbeschreibungen)
  - [Evolutionsstufe 0: Markt-Simulation](#evolutionsstufe-0-markt-simulation)
    - [Überblick](#überblick)
    - [Theoretischer Hintergrund](#theoretischer-hintergrund)
      - [Bertrand-Wettbewerbsmodell](#bertrand-wettbewerbsmodell)
      - [Nash-Gleichgewicht](#nash-gleichgewicht)
    - [Projektstruktur](#projektstruktur)
      - [Klassendiagramm](#klassendiagramm)
      - [Company Klasse (company.py)](#company-klasse-companypy)
      - [Market Klasse (market.py)](#market-klasse-marketpy)
      - [Simulation Klasse (simulation.py)](#simulation-klasse-simulationpy)
    - [Mathematische Grundlagen](#mathematische-grundlagen)
      - [Lineare Nachfragefunktion](#lineare-nachfragefunktion)
    - [Simulationsparameter](#simulationsparameter)
    - [Potenzielle Erweiterungen und Forschungsrichtungen](#potenzielle-erweiterungen-und-forschungsrichtungen)
    - [Anforderungen](#anforderungen)
    - [Nutzung](#nutzung)
      - [Beispielcode](#beispielcode)
    - [Implementierung der Klassen](#implementierung-der-klassens)
      - [1. Company Klasse (company.py)](#1-company-klasse-companypy)
      - [2. Market Klasse (market.py)](#2-market-klasse-marketpy)
      - [3. Simulation Klasse (simulation.py)](#3-simulation-klasse-simulationpy)
  - [Evolutionsstufe 1: Erweiterte Wettbewerbsmarktsimulation](#evolutionsstufe-1-erweiterte-wettbewerbsmarktsimulation)
    - [Übersicht](#übersicht)
    - [Wissenschaftlicher Hintergrund](#wissenschaftlicher-hintergrund)
      - [Erweiterung des Bertrand-Wettbewerbsmodells](#erweiterung-des-bertrand-wettbewerbsmodells)
    - [Projektstruktur](#projektstruktur-1)
      - [Klassenübersicht](#klassenübersicht)
      - [Vergleichsanalyse](#vergleichsanalyse)
      - [Simulationsdynamik](#simulationsdynamik)
    - [Visualisierung](#visualisierung-1)
    - [Implementierung der erweiterten Klassen](#implementierung-der-erweiterten-klassens)
  - [Evolutionsstufe 2: Dynamisches Preis- und Produktionsoptimierungsmodell](#evolutionsstufe-2-dynamisches-preis--und-produktionsoptimierungsmodell)
    - [Übersicht](#übersicht-1)
    - [Theoretischer Hintergrund](#theoretischer-hintergrund-1)
      - [Wissenschaftliche Innovation: Dynamische Produktionsslot-Planung](#wissenschaftliche-innovation-dynamische-produktionsslot-planung)
      - [Probabilistische Nachfragemodellierung](#probabilistische-nachfragemodellierung)
    - [Systemarchitektur](#systemarchitektur)
      - [Kernkomponenten](#kernkomponenten)
      - [Detaillierte Klassen- und Attributreferenz](#detaillierte-klassen--und-attributreferenz)
        - [1. Market Klasse (market.py)](#1-market-klasse-marketpy)
        - [2. Cost Klasse (cost.py)](#2-cost-klasse-costpy)
        - [3. CompanyDynamic Klasse (company.py)](#3-companydynamic-klasse-companypy)
        - [4. CompanyStatic Klasse (company.py)](#4-companystatic-klasse-companypy)
        - [5. StrategyDynamic Klasse (strategy.py)](#5-strategydynamic-klasse-strategypy)
        - [6. StrategyStatic Klasse (strategy.py)](#6-strategystatic-klasse-strategypy)
        - [7. Simulation Klasse (simulation.py)](#7-simulation-klasse-simulationpy)
    - [Mathematische Grundlagen](#mathematische-grundlagen-1)
      - [Marktanteilsberechnung](#marktanteilsberechnung)
      - [Nachfragemodell](#nachfragemodell)
    - [Schlüsselinnovationen](#schlüsselinnovationen)
    - [Leistungskennzahlen](#leistungskennzahlen)
    - [Nutzung](#nutzung-1)
      - [Voraussetzungen](#voraussetzungen)
      - [Simulation Ausführen](#simulation-ausführen)
      - [Visualisierung](#visualisierung-2)
      - [Konfigurationsoptionen](#konfigurationsoptionen)
    - [Zukünftige Forschungsrichtungen](#zukünftige-forschungsrichtungen)
    - [Einschränkungen](#einschränkungen)
- [Wechselwirkungen](#wechselwirkungen)
  - [Interaktion zwischen Komponenten](#interaktion-zwischen-komponenten)
  - [Datenfluss](#datenfluss)
  - [Abhängigkeiten](#abhängigkeiten)
  - [UML-Diagramm Hinweis](#uml-diagramm-hinweis)
- [Installation](#installation)
- [Nutzung](#nutzung-2)
  - [Beispielcode](#beispielcode-1)
- [Lizenz](#lizenz)
- [Beitragende](#beitragende)
- [Kontakt](#kontakt)
- [Abschluss](#abschluss)
- [Autor](#autor)

## 🎯 Überblick

Dieses Projekt zielt darauf ab, umfassende und erweiterte Modelle des Bertrand-Wettbewerbs zu entwickeln und zu simulieren. Der Fokus liegt auf der Maximierung des Gewinns durch dynamische Preisstrategien, die die Produktionsauslastung optimieren. Der Projektaufbau orientiert sich an der VDI-Richtlinie 3633, welche eine strukturierte Vorgehensweise für technische Projekte bietet. Durch die Durcharbeitung von drei Evolutionsstufen wird eine zunehmende Komplexität und Realitätsnähe der Modelle erreicht, um realistische Marktbedingungen und strategische Interaktionen zwischen Unternehmen zu simulieren.

### 📦 Projektstruktur nach VDI 3633

Die VDI 3633 unterteilt Projekte in mehrere Phasen, die hier adaptiert wurden:

1. **Projektdefinition**
   - Zielsetzung
   - Anforderungen
   - Rahmenbedingungen
2. **Konzeptentwicklung**
   - Erstellung der Roadmap
   - Modellierung der Evolutionsstufen
3. **Umsetzung**
   - Implementierung der Modelle
   - Integration der Komponenten
   - Test und Validierung
     - Simulationen durchführen
     - Ergebnisse analysieren
4. **Dokumentation und Abschluss**
   - Erstellung der Dokumentation
   - Abschlussbericht

## 🎯 Ausgangssituation und Ziel

### Ausgangssituation

Das klassische Bertrand-Wettbewerbsmodell beschreibt den Preiswettbewerb zwischen zwei Firmen, die identische Produkte anbieten. Obwohl dieses Modell grundlegende Einblicke in oligopolistische Marktstrukturen bietet, weist es mehrere Einschränkungen auf, die seine Anwendbarkeit auf reale Märkte begrenzen. Insbesondere berücksichtigt das klassische Modell keine dynamischen Preisadjustierungen, realistische Marktanteilsverteilungen oder stochastische Elemente in der Nachfrage- und Kostenstruktur.

### Ziel

Ziel ist die Entwicklung einer dynamischen Preisstrategie zur Maximierung des Gewinns durch optimale Steuerung der Produktionsauslastung. Günstige Preise sollen in Zeiten niedriger Nachfrage freie Kapazitäten füllen, um Fixkosten zu amortisieren und Verluste zu minimieren, während bei hoher Nachfrage Premiumpreise zusätzliche Gewinne abschöpfen. Durch die Berücksichtigung stochastischer Nachfrage- und Kostenfaktoren wird eine datengetriebene Entscheidungsgrundlage geschaffen, um Kapazitäten effizient auszunutzen und langfristige Profitabilität sicherzustellen.

## Projekt-Roadmap

### Evolutionsstufe 0

Grundlegendes Markt-Simulationsmodell mit statischen Preisstrategien und einfacher Berechnung des Nash-Gleichgewichts.

### Evolutionsstufe 1

Erweiterung des Modells um dynamische Preisadjustierungen, realistischere Marktanteilsberechnungen und Einführung von Vergleichsanalysen zwischen klassischen und erweiterten Modellen.

### Evolutionsstufe 2

Vollständig dynamisches Modell mit fortschrittlichen Optimierungsstrategien, stochastischer Nachfrage- und Kostenstruktur sowie umfassender Simulation und Visualisierung der Marktinteraktionen.

## Detaillierte Modellbeschreibungen

### Evolutionsstufe 0: Markt-Simulation

#### Überblick

Dieses Projekt implementiert ein grundlegendes Markt-Simulationsmodell, das die Dynamik des Preiswettbewerbs zwischen zwei Firmen anhand des Bertrand-Modells eines Oligopols untersucht. Die Simulation berechnet die Nash-Gleichgewichte der Preise und visualisiert die strategischen Interaktionen zwischen den konkurrierenden Unternehmen.

#### Theoretischer Hintergrund

##### Bertrand-Wettbewerbsmodell

Das Bertrand-Wettbewerbsmodell, entwickelt von Joseph Bertrand im Jahr 1883, ist eine grundlegende ökonomische Theorie, die den Preiswettbewerb zwischen Firmen beschreibt. In diesem Modell:

- Firmen konkurrieren durch gleichzeitiges Festsetzen der Preise.
- Konsumenten kaufen beim Unternehmen mit dem niedrigsten Preis.
- Alle Firmen produzieren identische Produkte.
- Firmen haben vollständige Informationen über Marktbedingungen.

##### Nash-Gleichgewicht

Ein Nash-Gleichgewicht stellt einen Zustand dar, in dem keine Firma einseitig ihr Ergebnis durch eine Änderung ihrer Strategie verbessern kann. Im Kontext des Preiswettbewerbs bedeutet dies, dass jede Firma ihren optimalen Preis festlegt, gegeben den Preis des Wettbewerbers.

#### Projektstruktur

##### Klassendiagramm

```plaintext
+---------------+       +---------------+       +---------------+
|    Market     |       |   Company     |       |   Simulation  |
+---------------+       +---------------+       +---------------+
| - company1    |       | - alpha       |       | - market      |
| - company2    |       | - beta        |       | - visualization|
+---------------+       | - gamma       |       +---------------+
| + calculate_nash_equilibrium() | | - marginal_cost|
+---------------+       | - name        |
                        +---------------+
                        | + reaction_price() |
                        +---------------+
```

##### Company Klasse (company.py)

**Zweck**  
Repräsentiert eine Firma mit spezifischen Markteigenschaften und strategischem Preisverhalten.

**Wichtige Attribute**
- `alpha`: Basissachfrageparameter
- `beta`: Preisempfindlichkeit der eigenen Nachfrage
- `gamma`: Kreuzpreisempfindlichkeit
- `marginal_cost`: Kosten für die Produktion einer zusätzlichen Einheit
- `name`: Kennung für die Firma

**Wichtige Methode: `reaction_price()`**  
Berechnet die optimale Preisreaktion auf den Preis des Wettbewerbers mittels einer linearen Reaktionsfunktion:

```python
def reaction_price(self, competitor_price):
    return (self.alpha + self.beta * self.marginal_cost + self.gamma * competitor_price) / (2 * self.beta)
```

**Wissenschaftlicher Einblick:**  
Diese Funktion verkörpert die strategische Interdependenz in oligopolistischen Märkten, bei der der optimale Preis einer Firma sowohl von ihren eigenen Eigenschaften als auch von den Preisen des Wettbewerbers abhängt.

##### Market Klasse (market.py)

**Zweck**  
Berechnet die Nash-Gleichgewichts-Preise für zwei konkurrierende Firmen.

**Wichtige Methode: `calculate_nash_equilibrium()`**  
**Theoretischer Ansatz:**  
Löst ein System simultaner linearer Gleichungen.

**Mathematische Formulierung:**
- Erstellt eine 2x2 Matrix `A`, die die interfirmären Preisabhängigkeiten erfasst.
- Erstellt einen Vektor `b`, der Markt- und Kostenparameter repräsentiert.
- Verwendet lineare Algebra zur Lösung der Gleichgewichtspreise.

**Rechnerische Strategie:**
- Verwendet NumPy's lineare Algebra Solver (`np.linalg.solve`).
- Bietet eine rechnerisch effiziente Berechnung des Gleichgewichts.

##### Simulation Klasse (simulation.py)

**Zweck**  
Orchestriert die Marktinteraktion und visualisiert die Ergebnisse.

**Funktionalität**
- Initialisiert Firmen- und Marktobjekte.
- Berechnet die Nash-Gleichgewichts-Preise.
- Generiert eine Visualisierung der Reaktionsfunktionen.

**Methoden**
- `run()`: Führt die Simulation durch, berechnet die Gleichgewichte und visualisiert die Reaktionsfunktionen.
- `plot_reaction_functions(equilibrium_prices)`: Erstellt die Visualisierung der Reaktionsfunktionen und markiert das Nash-Gleichgewicht.

**Visualisierung**
- Plottet die Reaktionsfunktionen beider Firmen.
- Markiert den Punkt des Nash-Gleichgewichts.
- Bietet grafische Einblicke in strategische Interaktionen.

#### Mathematische Grundlagen

##### Lineare Nachfragefunktion

Das Modell nimmt eine lineare Nachfragefunktion der Form an:

$$
Q_i = \alpha - \beta_i \cdot p_i + \gamma \cdot p_j
$$

Dabei gilt:

- \( Q_i \): Nachfrage nach Firma \( i \)
- \( \alpha \): Marktpotenzial
- \( \beta_i \): Preisempfindlichkeit der eigenen Nachfrage
- \( \gamma \): Kreuzpreisempfindlichkeit
- \( p_i \): Preis von Firma \( i \)
- \( p_j \): Preis des Wettbewerbers

#### Simulationsparameter

Im bereitgestellten Beispiel:

- Marktpotenzial (\( \alpha \)): 100
- Preisempfindlichkeit (\( \beta \)): 10
- Kreuzpreisempfindlichkeit (\( \gamma \)): 5
- Grenzkosten: 20


##### Beispielcode

```python
# Marktkomponenten initialisieren
company_a = Company(alpha=100, beta=10, gamma=5, marginal_cost=20, name='Firma A')
company_b = Company(alpha=100, beta=10, gamma=5, marginal_cost=20, name='Firma B')
market = Market(company1=company_a, company2=company_b)

# Simulation durchführen
simulation = Simulation(market=market, company1=company_a, company2=company_b)
simulation.run()
```

#### Implementierung der Klassen

##### 1. Company Klasse (company.py)

```python
class Company:
    def __init__(self, alpha, beta, gamma, marginal_cost, name):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.marginal_cost = marginal_cost
        self.name = name

    def reaction_price(self, competitor_price):
        return (self.alpha + self.beta * self.marginal_cost + self.gamma * competitor_price) / (2 * self.beta)
```

##### 2. Market Klasse (market.py)

```python
import numpy as np

class Market:
    def __init__(self, company1, company2):
        self.company1 = company1
        self.company2 = company2

    def calculate_nash_equilibrium(self):
        A = np.array([
            [1, -self.company1.gamma / (2 * self.company1.beta)],
            [-self.company2.gamma / (2 * self.company2.beta), 1]
        ])
        b = np.array([
            (self.company1.alpha + self.company1.beta * self.company1.marginal_cost) / (2 * self.company1.beta),
            (self.company2.alpha + self.company2.beta * self.company2.marginal_cost) / (2 * self.company2.beta)
        ])
        equilibrium_prices = np.linalg.solve(A, b)
        return equilibrium_prices
```

##### 3. Simulation Klasse (simulation.py)

```python
import matplotlib.pyplot as plt
import numpy as np

class Simulation:
    def __init__(self, market, company1, company2):
        self.market = market
        self.company1 = company1
        self.company2 = company2

    def run(self):
        equilibrium_prices = self.market.calculate_nash_equilibrium()
        print(f"Nash Gleichgewichts-Preise:\n{self.company1.name}: {equilibrium_prices[0]}\n{self.company2.name}: {equilibrium_prices[1]}")
        self.plot_reaction_functions(equilibrium_prices)

    def plot_reaction_functions(self, equilibrium_prices):
        prices = np.linspace(0, 100, 400)
        reaction1 = [self.company1.reaction_price(p2) for p2 in prices]
        reaction2 = [self.company2.reaction_price(p1) for p1 in prices]

        plt.figure(figsize=(10, 6))
        plt.plot(prices, reaction1, label=f'{self.company1.name} Reaktionsfunktion')
        plt.plot(prices, reaction2, label=f'{self.company2.name} Reaktionsfunktion')
        plt.plot(equilibrium_prices[0], equilibrium_prices[1], 'ro', label='Nash Gleichgewicht')
        plt.xlabel('Preis')
        plt.ylabel('Optimale Reaktion')
        plt.title('Reaktionsfunktionen und Nash Gleichgewicht')
        plt.legend()
        plt.grid(True)
        plt.show()
```

### Evolutionsstufe 1: Erweiterte Wettbewerbsmarktsimulation

#### Übersicht

In der ersten Evolutionsstufe wird das grundlegende Markt-Simulationsmodell erweitert, um dynamische Preisadjustierungen, realistischere Marktanteilsberechnungen und eine Vergleichsanalyse zwischen dem klassischen und dem erweiterten Bertrand-Modell zu integrieren. Diese Erweiterungen ermöglichen eine differenziertere Analyse der strategischen Interaktionen und des Marktverhaltens.

##### Erweiterung des Bertrand-Wettbewerbsmodells

Während das klassische Bertrand-Modell statische Preisstrategien und einfache Marktanteilsberechnungen verwendet, integriert die erste Evolutionsstufe dynamische Elemente, um realistischere Marktbedingungen abzubilden. Dies beinhaltet:

- **Dynamische Preisadjustierungen:** Unternehmen passen ihre Preise in jedem Simulationszyklus basierend auf den Marktbedingungen und den Preisen des Wettbewerbers an.
- **Realistischere Marktanteilsberechnungen:** Anstelle einer binären Marktzuweisung wird eine kontinuierliche Marktanteilszuweisung mittels logistischer Funktionen implementiert.
- **Vergleichsanalyse:** Analyse der Unterschiede und Vorteile des erweiterten Modells gegenüber dem klassischen Modell.

#### Projektstruktur

##### Klassenübersicht

1. **Market Klasse (market.py)**
   - Repräsentiert das Marktumfeld mit zentralen ökonomischen Mechanismen.
   - **Attribute:**
     - `company1`: Instanz der ersten Firma
     - `company2`: Instanz der zweiten Firma
   - **Wichtige Methoden:**
     - `calculate_nash_equilibrium()`: Berechnet die Nash-Gleichgewichte der Preise.
     - `calculate_market_shares(price_a, price_b, sensitivity)`: Berechnet die Marktanteile anhand logistischer Funktionen.

2. **Company Klasse (company.py)**
   - Repräsentiert eine Firma mit spezifischen Markt- und Kostenparametern.
   - **Attribute:**
     - `alpha`: Basissachfrageparameter
     - `beta`: Preisempfindlichkeit der eigenen Nachfrage
     - `gamma`: Kreuzpreisempfindlichkeit
     - `marginal_cost`: Grenzkosten
     - `name`: Kennung für die Firma
     - `price`: Aktueller Preis
   - **Wichtige Methoden:**
     - `set_price(price)`: Setzt den aktuellen Preis der Firma.
     - `reaction_price(competitor_price)`: Berechnet den optimalen Preis als Reaktion auf den Preis des Wettbewerbers.

3. **Simulation Klasse (simulation.py)**
   - Orchestriert die Marktinteraktion und visualisiert die Ergebnisse.
   - **Attribute:**
     - `market`: Instanz der Marktklasse
     - `company1`: Instanz der ersten Firma
     - `company2`: Instanz der zweiten Firma
   - **Wichtige Methoden:**
     - `run()`: Führt die Simulation durch, berechnet die Gleichgewichte und visualisiert die Reaktionsfunktionen.
     - `plot_reaction_functions(equilibrium_prices)`: Erstellt die Visualisierung der Reaktionsfunktionen und markiert das Nash-Gleichgewicht.

#### Simulationsdynamik

- **Dynamische Preisadjustierung:**  
  In jedem Simulationszyklus passen die Unternehmen ihre Preise basierend auf den aktuellen Marktbedingungen und den Preisen des Wettbewerbers an. Dies ermöglicht eine realistischere Darstellung der Marktbewegungen und strategischen Entscheidungen.

- **Kontinuierliche Marktanteilszuweisung:**  
  Anstelle einer binären Zuweisung wird eine logistische Funktion verwendet, um die Marktanteile kontinuierlich und realitätsnah zu verteilen. Dies vermeidet den "Gewinner nimmt alles"-Ansatz und reflektiert die tatsächliche Marktaufteilung besser.

#### Implementierung der erweiterten Klassen

##### 1. Market Klasse (market.py)

```python
import numpy as np

class Market:
    def __init__(self, company1, company2):
        self.company1 = company1
        self.company2 = company2

    def calculate_nash_equilibrium(self):
        A = np.array([
            [1, -self.company1.gamma / (2 * self.company1.beta)],
            [-self.company2.gamma / (2 * self.company2.beta), 1]
        ])
        b = np.array([
            (self.company1.alpha + self.company1.beta * self.company1.marginal_cost) / (2 * self.company1.beta),
            (self.company2.alpha + self.company2.beta * self.company2.marginal_cost) / (2 * self.company2.beta)
        ])
        equilibrium_prices = np.linalg.solve(A, b)
        return equilibrium_prices

    def calculate_market_shares(self, price_a, price_b, sensitivity):
        price_diff = (price_b - price_a) / ((price_a + price_b)/2 + 1e-9)
        share_a = 1 / (1 + np.exp(-sensitivity * price_diff))
        share_b = 1 - share_a
        return share_a, share_b
```

##### 2. Company Klasse (company.py)

```python
class Company:
    def __init__(self, alpha, beta, gamma, marginal_cost, name):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.marginal_cost = marginal_cost
        self.name = name
        self.price = None

    def set_price(self, price):
        self.price = price

    def reaction_price(self, competitor_price):
        return (self.alpha + self.beta * self.marginal_cost + self.gamma * competitor_price) / (2 * self.beta)
```

##### 3. Simulation Klasse (simulation.py)

```python
import matplotlib.pyplot as plt
import numpy as np

class Simulation:
    def __init__(self, market, company1, company2):
        self.market = market
        self.company1 = company1
        self.company2 = company2

    def run(self):
        equilibrium_prices = self.market.calculate_nash_equilibrium()
        self.company1.set_price(equilibrium_prices[0])
        self.company2.set_price(equilibrium_prices[1])
        print(f"Nash Gleichgewichts-Preise:\n{self.company1.name}: {equilibrium_prices[0]:.2f}\n{self.company2.name}: {equilibrium_prices[1]:.2f}")
        self.plot_reaction_functions(equilibrium_prices)

    def plot_reaction_functions(self, equilibrium_prices):
        prices = np.linspace(0, 100, 400)
        reaction1 = [self.company1.reaction_price(p2) for p2 in prices]
        reaction2 = [self.company2.reaction_price(p1) for p1 in prices]

        plt.figure(figsize=(10, 6))
        plt.plot(prices, reaction1, label=f'{self.company1.name} Reaktionsfunktion')
        plt.plot(prices, reaction2, label=f'{self.company2.name} Reaktionsfunktion')
        plt.plot(equilibrium_prices[0], equilibrium_prices[1], 'ro', label='Nash Gleichgewicht')
        plt.xlabel('Preis')
        plt.ylabel('Optimale Reaktion')
        plt.title('Reaktionsfunktionen und Nash Gleichgewicht')
        plt.legend()
        plt.grid(True)
        plt.show()
```

### Evolutionsstufe 2: Dynamisches Preis- und Produktionsoptimierungsmodell

#### Übersicht

Diese Evolutionsstufe präsentiert einen innovativen Ansatz zur dynamischen Preisgestaltung und Produktionsoptimierung, der fortschrittliche rechnergestützte Strategien nutzt, um die wirtschaftliche Effizienz über Frühbuchungs- und Last-Minute-Marktsegmente hinweg zu maximieren.

#### Theoretischer Hintergrund

##### Wissenschaftliche Innovation: Dynamische Produktionsslot-Planung

Der Kern wissenschaftlicher Beitrag dieser Forschung liegt in der dynamischen Zuordnung der Produktionskapazität zu Preisstrategien. Traditionelle Produktionsmodelle behandeln die Kapazität oft als statische Einschränkung, während diese Simulation einen neuartigen Mechanismus einführt:

- **Adaptive Preis-Kapazitäts-Kopplung**
  - Produktionsslots werden basierend auf prognostizierter Marktnachfrage dynamisch zugewiesen.
  - Preise dienen als strategisches Hebel für die Kapazitätsauslastung.
  - Echtzeit-Nachfrageelastizität beeinflusst Produktionsentscheidungen.

##### Probabilistische Nachfragemodellierung

- Implementiert stochastische Marktanteilsberechnungen.
- Verwendet marktsensitivitätsinspirierte logistische Marktanteilsfunktionen.
- Integriert Preisempfindlichkeit und Marktschwankungen.

#### Systemarchitektur

##### Kernkomponenten

- **Market Klasse (market.py)**
- **Cost Klasse (cost.py)**
- **CompanyDynamic Klasse (company.py)**
- **CompanyStatic Klasse (company.py)**
- **StrategyDynamic Klasse (strategy.py)**
- **StrategyStatic Klasse (strategy.py)**
- **Simulation Klasse (simulation.py)**

##### Detaillierte Klassen- und Attributreferenz

###### 1. Market Klasse (market.py)

**Zweck**  
Simuliert Marktdynamiken, Nachfragesgenerierung und Marktanteilszuweisung.

**Initialisierungsparameter**
- `early_price_sensitivity` (float, Standard=3.0):  
  Sensitivität des Frühbuchungsmarktsegments gegenüber Preisänderungen.  
  Höherer Wert = Dramatischere Marktanteilsverschiebungen bei Preisänderungen.
- `last_minute_base_sensitivity` (float, Standard=1.0):  
  Sensitivität des Last-Minute-Marktsegments gegenüber Preisänderungen.  
  Bestimmt, wie schnell sich Marktanteile bei Preisunterschieden ändern.
- `early_ratio` (float, Standard=0.8):  
  Anteil der Gesamtmarktgröße, der dem Frühbuchungssegment zugewiesen wird.  
  Gibt die Präferenz des Marktes für Vorauskäufe an.
- `last_minute_ratio` (float, Standard=0.2):  
  Anteil der Gesamtmarktgröße für das Last-Minute-Segment.  
  Repräsentiert spontane oder späte Kaufentscheidungen.
- `market_size_mean` (int, Standard=1000):  
  Durchschnittliche Gesamtmarktgröße.  
  Grundlage für die Nachfragesgenerierung.
- `market_size_std` (int, Standard=200):  
  Standardabweichung der Marktgröße.  
  Führt Variabilität in der gesamten Marktnachfrage ein.

**Wichtige Methoden**
- `market_share(price_A, price_B, sensitivity)`:  
  Berechnet den Marktanteil mittels logistischer Transformation.  
  Berücksichtigt Preisunterschied und Sensitivität.  
  Gibt Marktanteile für zwei Wettbewerber zurück.
- `generate_demands(price_A_early, price_B_early, price_A_last, price_B_last)`:  
  Generiert probabilistische Nachfrage für Frühbuchungs- und Last-Minute-Segmente.  
  Anwenden von Preisempfindlichkeit und Marktschwankungen.  
  Gibt Nachfragemengen für beide Unternehmen zurück.

###### 2. Cost Klasse (cost.py)

**Zweck**  
Verwaltet Kostenstrukturen mit dynamischen Update-Mechanismen.

**Initialisierungsparameter**
- `fixed_cost` (float):  
  Fixkosten, unabhängig vom Produktionsvolumen.  
  Repräsentiert Gemeinkosten.
- `marginal_cost` (float):  
  Variable Kosten pro Produktionseinheit.  
  Direkt beeinflusst durch Produktionsvolumen.
- `raw_material_price` (float, Standard=10):  
  Kosten der Rohmaterialien pro Einheit.  
  Reflektiert Schwankungen in der Lieferkette und Inputkosten.
- `inventory_holding_cost` (float, Standard=2):  
  Kosten für die Lagerhaltung.  
  Repräsentiert Lager-, Wartungs- und Opportunitätskosten.

**Wichtige Methoden**
- `total_unit_cost()`:  
  Berechnet die Gesamtkosten pro Einheit.  
  Kombination aus Grenzkosten und Rohmaterialpreis.
- `update_fixed_costs(inflation_rate=0.01)`:  
  Simuliert eine schrittweise Erhöhung der Fixkosten.  
  Modelliert wirtschaftliche Inflationseffekte.
- `update_marginal_costs(fluctuation_std=0.05)`:  
  Führt stochastische Variationen der Grenzkosten ein.  
  Verwendung der Normalverteilung für realistische Kostenänderungen.
- `update_raw_material_price(fluctuation_std=0.05)`:  
  Anwenden von zufälligen Schwankungen auf Rohmaterialpreise.  
  Simuliert Lieferketten- und Marktvolatilität.

###### 3. CompanyDynamic Klasse (company.py)

**Zweck**  
Repräsentiert ein anspruchsvolles Unternehmen mit dynamischen Entscheidungsfähigkeiten.

**Initialisierungsparameter**
- `name` (str): Unternehmensidentifikator.
- `capacity` (float): Maximale Produktionskapazität.
- `cost` (Cost): Kostenstruktur-Instanz.
- `base_price` (float): Anfangsstrategie der Preisgestaltung.
- `inventory` (float, Standard=0): Anfangsbestand.
- `buffer_stock` (int, Standard=20): Mindestbestandsschwelle.

**Wichtige Methoden**
- `set_buffer_stock(new_buffer)`:  
  Anpassung der Mindestbestandsgröße.  
  Ermöglicht eine adaptive Lagerhaltungsstrategie.
- `use_strategy(strategy, price_B_early, price_B_last, market)`:  
  Anwendung der Optimierungsstrategie.  
  Berücksichtigung von Wettbewerberpreisen und Marktbedingungen.  
  Aktualisierung von Lagerbestand und Basispreis basierend auf Strategieergebnis.

###### 4. CompanyStatic Klasse (company.py)

**Zweck**  
Repräsentiert ein einfacheres, reaktives Preisgestaltungsunternehmen.

**Initialisierungsparameter**
- `name` (str): Unternehmensidentifikator.
- `capacity` (float): Maximale Produktionskapazität.
- `cost` (Cost): Kostenstruktur-Instanz.
- `base_price` (float): Anfangsstrategie der Preisgestaltung.

**Wichtige Methoden**
- `simple_decision(dB_early, dB_lm)`:  
  Trifft Produktions- und Verkaufsentscheidungen.  
  Berücksichtigt Nachfrage und Produktionskapazität.  
  Berechnet Gewinn basierend auf Verkäufen und Kosten.
- `adjust_price(strategy, competitor_price)`:  
  Anwendung der adaptiven Preisstrategie.  
  Reaktion auf die Preisgestaltung des Wettbewerbers.  
  Sicherstellung, dass der Preis über den Grenzkosten bleibt.

###### 5. StrategyDynamic Klasse (strategy.py)

**Zweck**  
Implementiert eine komplexe Optimierungsstrategie für fortschrittliche Preisentscheidungen.

**Initialisierungsparameter**
- `early_price_candidates` (Liste, Standard=[60, 80, 100, 120, 140]):  
  Potenzielle Preisoptionen für Frühbuchungen.  
  Ermöglicht strategische Preiserkundung.
- `last_price_candidates` (Liste, Standard=[80, 120, 160, 200]):  
  Potenzielle Preisoptionen für Last-Minute-Angebote.  
  Ermöglicht flexible Preisadaptionen.

**Wichtige Methode**
- `optimize_decision(company, price_B_early, price_B_last, market)`:  
  Generiert mehrere Preisszenarien.  
  Verwendung der linearen Programmierung zur optimalen Entscheidungsfindung.  
  Berücksichtigung von:
  - Produktionskapazitätsbeschränkungen.
  - Lagerbestandsbeschränkungen.
  - Umsatzmaximierung.
  - Nachfragevariabilität.

###### 6. StrategyStatic Klasse (strategy.py)

**Zweck**  
Bietet einen einfachen, adaptiven Preisgestaltungsmechanismus.

**Initialisierungsparameter**
- `max_adjustment` (float, Standard=0.05):  
  Maximale erlaubte prozentuale Preisänderung.  
  Verhindert extreme Preisschwankungen.

**Wichtige Methode**
- `adjust_price(own_price, competitor_price, marginal_cost)`:  
  Implementiert die Preisänderungslogik.  
  Vergleich des eigenen Preises mit dem des Wettbewerbers.  
  Sicherstellung, dass der Preis über den Grenzkosten bleibt.  
  Einführung leichter Zufälligkeit für Marktrealismus.

###### 7. Simulation Klasse (simulation.py)

**Zweck**  
Orchestriert die Interaktion zwischen allen Komponenten über mehrere Zeiteinheiten hinweg.

**Funktionalität**
- Initialisiert Markt- und Unternehmensparameter.
- Führt mehrperiodige Simulationen durch.
- Generiert Nachfrageszenarien.
- Wendet unternehmensspezifische Strategien an.
- Berechnet finanzielle Ergebnisse.
- Aktualisiert Kostenstrukturen.
- Visualisiert und analysiert die Ergebnisse.

#### Mathematische Grundlagen

##### Marktanteilsberechnung

Der Marktanteil wird durch eine logistische Funktion des Preisunterschieds bestimmt:

$$
share\_A = \frac{1}{1 + e^{-sensitivity \times price\_diff}}
$$

**Eigenschaften der logistischen Transformation:**
- Gleichmäßiger Marktanteilsübergang.
- Symmetrische Reaktion um die Preisparität.
- Kontinuierliche Wahrscheinlichkeitsverteilung.

##### Nachfragemodell

Die Nachfrage wird durch einen mehrstufigen stochastischen Prozess generiert:

- Basismarktgröße (Normalverteilung).
- Preisabhängige Skalierungsfaktoren.
- Segment-spezifische Nachfragezuweisung.

**Formel:**

$$
Q_i = market\_size \times \left(1 - \frac{max\_price}{p_i}\right)
$$


#### Leistungskennzahlen

- Gewinn pro Periode
- Marktanteil
- Produktionseffizienz
- Lagerbestandsmanagement
- Kostenstruktur-Entwicklung

#### Nutzung

##### Voraussetzungen

- Python 3.8+
- NumPy
- Pandas
- Matplotlib
- PuLP (Lineare Programmierung)


##### Visualisierung

Die Simulation generiert zwei umfassende Visualisierungen:

- Gesamte Marktdynamik
- Kosten- und Produktionsinsights

**Ausgaben umfassen:**
- Gewinntrends
- Preisentwicklung
- Marktanteilentwicklung
- Produktions- und Lagerbestandskennzahlen

##### Konfigurationsoptionen

- Anpassbare Marktsensitivität.
- Konfigurierbare Kostenstrukturen.
- Anpassbare Preisstrategien.
- Variable Marktgrößenparameter.

#### Zukünftige Erweiterungen

- Maschinelles Lernen zur Nachfrageprognose anstelle von der gegebenen Nachfragekurve für die Simulation
- Erweiterung auf Mehrfirmen-Szenarien
- Entwicklung von Echtzeit-Adaptivpreismechanismen
- Erweiterung der Kosten-, Nachfrage-Attribute


#### Einschränkungen

- Annahme rationalen Marktverhaltens.
- Vereinfachte Kosten- und Nachfragemodelle.
- Deterministischer Optimierungsansatz.

## Wechselwirkungen

### Interaktion zwischen Komponenten

Die verschiedenen Klassen und Module interagieren wie folgt:

- **Market:** Zentralisiert die Marktdynamik und generiert die Nachfragemengen basierend auf den Preisen der Unternehmen. Kommuniziert mit den Company Klassen, um Marktanteile und Nachfrage zu verteilen.
- **Cost:** Jede Company Instanz besitzt eine Cost Instanz, die die Kostenstruktur des Unternehmens verwaltet. Änderungen in den Kosten beeinflussen direkt die Preisentscheidungen der Unternehmen.
- **CompanyDynamic und CompanyStatic:** Repräsentieren unterschiedliche Unternehmensstrategien. Sie interagieren mit der Market Klasse, um Preise anzupassen und Gewinne zu maximieren.
- **StrategyDynamic und StrategyStatic:** Definieren die Preisentscheidungslogiken für die jeweiligen Company Klassen. Sie nutzen Daten von Market und Cost, um optimale Preisentscheidungen zu treffen.
- **Simulation:** Koordiniert die Interaktion aller Komponenten über mehrere Zeiteinheiten hinweg. Sammeln Daten von Market und Company Klassen, führen Anpassungen durch und visualisieren die Ergebnisse.

### Datenfluss

1. **Initialisierung:**  
   Market und Company Klassen werden mit Anfangsparametern instanziiert.

2. **Simulation Loop:** In jeder Periode:
   - Market generiert die Nachfrage basierend auf aktuellen Preisen.
   - Company Klassen entscheiden über Preisänderungen unter Verwendung ihrer Strategy Klassen.
   - Cost Klassen aktualisieren die Kostenstrukturen.
   - Market verteilt die Nachfrage entsprechend den neuen Preisen.
   - Simulation sammelt und speichert die Ergebnisse.

3. **Visualisierung:**  
   Nach Abschluss der Simulation werden die gesammelten Daten visualisiert.

### Abhängigkeiten

- Company Klassen sind abhängig von Market und Cost Klassen für Entscheidungsgrundlagen.
- Strategy Klassen sind abhängig von Company und Market Klassen, um fundierte Preisentscheidungen zu treffen.
- Simulation Klasse ist die orchestrierende Einheit, die alle anderen Komponenten integriert und koordiniert.

### Beispielcode

```python
# Marktkomponenten initialisieren
from company import Company
from market import Market
from simulation import Simulation

company_a = Company(alpha=100, beta=10, gamma=5, marginal_cost=20, name='Firma A')
company_b = Company(alpha=100, beta=10, gamma=5, marginal_cost=20, name='Firma B')
market = Market(company1=company_a, company2=company_b)

# Simulation durchführen
simulation = Simulation(market=market, company1=company_a, company2=company_b)
simulation.run()
```

## Lizenz

MIT Lizenz

## Kontakt

**Leon de Vries**  
Email: mail@leondevries.de  
Projekt: [GitHub Repository](https://github.com/IhrBenutzername/market-simulation)

## Abschluss

Diese Dokumentation bietet einen umfassenden Überblick über die Entwicklung und Implementierung eines erweiterten Bertrand-Wettbewerbsmodells. Durch die strukturierte Herangehensweise gemäß VDI 3633 und die detaillierte Beschreibung der Evolutionsstufen wird eine solide Grundlage für die weitere Forschung und Entwicklung in diesem Bereich geschaffen.  
Für weitere Informationen, Fragen oder Beiträge stehen wir Ihnen gerne zur Verfügung.

## Autor

**Leon de Vries**
```
