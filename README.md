# Evolutionsstufe 1

# Bertrand Competition Market Simulation

## Overview

This project simulates a Bertrand competition between two companies, implementing a strategic pricing model based on microeconomic principles of market dynamics and strategic interaction.

## Scientific Background

### Bertrand Competition Model

The Bertrand competition model, first proposed by Joseph Bertrand in 1883, is a fundamental economic theory describing price competition between firms. Unlike Cournot competition, which focuses on quantity, Bertrand competition centers on price-setting strategies.

Key characteristics:
- Firms compete by simultaneously setting prices
- Consumers purchase from the lowest-price firm
- Firms aim to maximize profits through strategic pricing
- In perfect competition, prices converge to marginal cost

## Project Structure

### Class Breakdown

#### 1. `Market` (market.py)
Represents the market environment with key economic mechanisms:

**Attributes:**
- `market_size`: Total potential market volume
- `max_price`: Maximum sustainable price point
- `price_sensitivity`: Elasticity of demand relative to price differences

**Key Methods:**
- `market_share(price_a, price_b)`: Calculates market share using a logistic function
- `demand(price)`: Computes market demand based on price

**Scientific Mechanism:**
The market share is determined by a logistic function, which captures non-linear consumer behavior:
- Small price differences have minimal impact
- Significant price differences dramatically shift market share
- Ensures smooth transition between competing firms

#### 2. `Company` (company.py)
Represents individual market participants:

**Attributes:**
- `name`: Identifier for the company
- `cost`: Cost structure
- `price`: Current price setting

**Key Methods:**
- `set_price(price)`: Adjusts company's price
- `profit(quantity)`: Calculates profit based on price and quantity

**Profit Calculation:**
Π = (p - c) * Q
- p: Price
- c: Marginal Cost
- Q: Quantity sold

#### 3. `Cost` (cost.py)
Manages cost structure:

**Attributes:**
- `marginal_cost`: Constant cost per unit produced

**Method:**
- `get_marginal_cost()`: Returns marginal cost

#### 4. `BertrandUnderbiddingStrategy` (strategy.py)
Implements pricing strategy with dynamic adjustment:

**Key Features:**
- Automatic price underbidding when at a competitive disadvantage
- Randomized underbidding to simulate market uncertainty
- Ensures prices never fall below marginal cost

**Strategy Mechanism:**
1. Compare own price with competitor's price
2. If higher, reduce price strategically
3. Use random factor to introduce market variability
4. Maintain a price floor at marginal cost

#### 5. `Simulation` (simulation.py)
Orchestrates market interaction and data collection:

**Key Functions:**
- Run multi-period market simulation
- Track prices, profits, and market shares
- Visualize market dynamics
- Calculate period-by-period economic interactions

## Simulation Dynamics

### Market Share Calculation
Market share is determined by a logistic function of price difference:
- Captures non-linear consumer decision-making
- Smooth transition between competing firms
- Mathematically represented as: 
  share_a = 1 / (1 + exp(-price_sensitivity * price_diff))

### Demand Model
Linear demand function:
Q = market_size * (1 - price/max_price)
- Demand decreases as price increases
- Total market size acts as a scaling factor

## Economic Insights

### Pricing Strategies
- Dynamic price adjustment
- Competitive underbidding
- Maintaining profitability above marginal cost

### Market Equilibrium
The simulation explores how firms:
- Respond to competitor pricing
- Maintain profit margins
- Adapt to market conditions

## Usage Example

```python
# Initialize market components
cost = Cost(marginal_cost=10)
market = Market(market_size=1000, max_price=50, price_sensitivity=2.0)
company_a = Company(name='A', cost=cost, initial_price=45)
company_b = Company(name='B', cost=cost, initial_price=40)

# Create strategies
strategy_a = BertrandUnderbiddingStrategy()
strategy_b = BertrandUnderbiddingStrategy()

# Run simulation
simulation = Simulation(market, company_a, company_b, strategy_a, strategy_b, num_periods=50)
prices_a, prices_b, profits_a, profits_b, shares_a, shares_b = simulation.run()
simulation.plot_results(prices_a, prices_b, profits_a, profits_b, shares_a, shares_b)
```



# Evolutionsstufe 2 

# Dynamic Pricing and Market Simulation Model

## Overview

This project presents a sophisticated computational model for analyzing dynamic pricing strategies in a competitive market environment. The simulation explores complex interactions between two companies (A and B) using advanced optimization techniques, stochastic demand modeling, and adaptive pricing strategies.

## Scientific Background

### Market Dynamics Modeling

The research is grounded in microeconomic principles of:
- Price elasticity of demand
- Market segmentation
- Strategic decision-making under uncertainty
- Dynamic optimization

### Key Theoretical Foundations

1. **Demand Elasticity Theory**
   - Utilizes logistic function for market share calculation
   - Incorporates price sensitivity parameters
   - Models non-linear demand responses to price changes

2. **Stochastic Market Modeling**
   - Employs normal distribution for market size estimation
   - Introduces randomness to simulate real-world market uncertainties
   - Allows for dynamic market size and price-dependent demand fluctuations

## System Architecture

### Core Components

# Detailed Class and Attribute Reference

## 1. `Market` Class (`market.py`)
### Purpose
Simulates market dynamics, demand generation, and market share allocation.

### Initialization Parameters
- `early_price_sensitivity` (float, default=3.0): 
  - Sensitivity of early booking market segment to price changes
  - Higher value = More dramatic market share shifts based on price

- `last_minute_base_sensitivity` (float, default=1.0):
  - Sensitivity of last-minute market segment to price changes
  - Controls how quickly market share changes with price differences

- `early_ratio` (float, default=0.8):
  - Proportion of total market size allocated to early booking segment
  - Indicates market's preference for advance purchases

- `last_minute_ratio` (float, default=0.2):
  - Proportion of total market size for last-minute segment
  - Represents spontaneous or late purchasing behavior

- `market_size_mean` (int, default=1000):
  - Average total market size
  - Serves as base for demand generation

- `market_size_std` (int, default=200):
  - Standard deviation of market size
  - Introduces variability in total market demand

### Key Methods
1. `market_share(price_A, price_B, sensitivity)`:
   - Calculates market share using logistic transformation
   - Considers price difference and sensitivity
   - Returns market share for two competitors

2. `generate_demands(price_A_early, price_B_early, price_A_last, price_B_last)`:
   - Generates probabilistic demand for early and last-minute segments
   - Applies price sensitivity and market size variations
   - Returns demand quantities for both companies

## 2. `Cost` Class (`cost.py`)
### Purpose
Manages cost structures with dynamic update mechanisms.

### Initialization Parameters
- `fixed_cost` (float): 
  - Constant costs independent of production volume
  - Represents overhead expenses

- `marginal_cost` (float): 
  - Variable costs per unit of production
  - Directly influenced by production volume

- `raw_material_price` (float, default=10):
  - Cost of raw materials per unit
  - Reflects supply chain and input cost variations

- `inventory_holding_cost` (float, default=2):
  - Cost of maintaining inventory
  - Represents storage, maintenance, and opportunity costs

### Key Methods
1. `total_unit_cost()`:
   - Calculates total cost per unit
   - Combines marginal cost and raw material price

2. `update_fixed_costs(inflation_rate=0.01)`:
   - Simulates gradual increase in fixed costs
   - Models economic inflation effects

3. `update_marginal_costs(fluctuation_std=0.05)`:
   - Introduces stochastic variations in marginal costs
   - Uses normal distribution for realistic cost changes

4. `update_raw_material_price(fluctuation_std=0.05)`:
   - Applies random fluctuations to raw material prices
   - Simulates supply chain and market volatility

## 3. `CompanyDynamic` Class (`company.py`)
### Purpose
Represents a sophisticated company with dynamic decision-making capabilities.

### Initialization Parameters
- `name` (str): Company identifier
- `capacity` (float): Maximum production capacity
- `cost` (Cost): Cost structure instance
- `base_price` (float): Initial pricing strategy
- `inventory` (float, default=0): Initial inventory level
- `buffer_stock` (int, default=20): Minimum inventory threshold

### Key Methods
1. `set_buffer_stock(new_buffer)`:
   - Dynamically adjusts minimum inventory level
   - Allows adaptive inventory management strategy

2. `use_strategy(strategy, price_B_early, price_B_last, market)`:
   - Applies optimization strategy
   - Considers competitor prices and market conditions
   - Updates inventory and base price based on strategy outcome

## 4. `CompanyStatic` Class (`company.py`)
### Purpose
Represents a more simplistic, reactively pricing company.

### Initialization Parameters
- `name` (str): Company identifier
- `capacity` (float): Maximum production capacity
- `cost` (Cost): Cost structure instance
- `base_price` (float): Initial pricing strategy

### Key Methods
1. `simple_decision(dB_early, dB_lm)`:
   - Makes production and sales decisions
   - Considers demand and production capacity
   - Calculates profit based on sales and costs

2. `adjust_price(strategy, competitor_price)`:
   - Applies adaptive pricing strategy
   - Responds to competitor's pricing
   - Ensures price remains above marginal cost

## 5. `StrategyDynamic` Class (`strategy.py`)
### Purpose
Implements complex optimization strategy for advanced pricing decisions.

### Initialization Parameters
- `early_price_candidates` (list, default=[60, 80, 100, 120, 140]):
  - Potential early booking price options
  - Provides strategic price exploration

- `last_price_candidates` (list, default=[80, 120, 160, 200]):
  - Potential last-minute price options
  - Allows flexible pricing adaptation

### Key Method
1. `optimize_decision(company, price_B_early, price_B_last, market)`:
   - Generates multiple price scenarios
   - Uses linear programming for optimal decision
   - Considers:
     * Production capacity
     * Inventory constraints
     * Revenue maximization
     * Demand variability

## 6. `StrategyStatic` Class (`strategy.py`)
### Purpose
Provides a simple, adaptive pricing mechanism.

### Initialization Parameters
- `max_adjustment` (float, default=0.05):
  - Maximum allowed price change percentage
  - Prevents extreme pricing fluctuations

### Key Method
1. `adjust_price(own_price, competitor_price, marginal_cost)`:
   - Implements price adjustment logic
   - Compares own price with competitor
   - Ensures price stays above marginal cost
   - Introduces slight randomness for market realism

## Interaction Mechanisms

### Price Sensitivity
- Logistic market share allocation
- Non-linear demand response
- Segment-specific elasticity

### Cost Dynamics
- Stochastic cost updates
- Inflation and market fluctuation modeling
- Dynamic marginal cost management

### Strategic Decision Processes
1. **Company A (Dynamic)**
   - Complex optimization
   - Multiple scenario evaluation
   - Advanced inventory management

2. **Company B (Static)**
   - Reactive pricing
   - Simple decision framework
   - Competitor-based adjustments

## Simulation Workflow
1. Initialize market parameters
2. Generate demand scenarios
3. Apply company-specific strategies
4. Calculate financial outcomes
5. Update cost structures
6. Visualize and analyze results

### Pricing Strategies Detailed

#### Company A: Dynamic Optimization Strategy

**Mechanism:**
- Uses linear programming (PuLP library) for decision optimization
- Evaluates multiple price scenarios
- Considers:
  - Production capacity constraints
  - Inventory management
  - Revenue maximization
  - Cost minimization

**Key Optimization Variables:**
- Early and last-minute prices
- Production volume
- Ending inventory
- Demand scenarios

#### Company B: Static Adaptive Strategy

**Mechanism:**
- Implements marginal price adjustments
- Responds to competitor's pricing
- Constraints:
  - Maximum price adjustment (5%)
  - Marginal cost floor

## Mathematical Modeling Insights

### Demand Generation Function

```python
def generate_demands(self, price_A_early, price_B_early, price_A_last, price_B_last):
    # Stochastic market size generation
    base_market = np.random.normal(market_size_mean, market_size_std)
    
    # Price sensitivity transformations
    early_factor = 1 - max(0, (avg_price_early - 100) * 0.003)
    lm_boost = 1 + (100 - avg_price_last) * 0.01
```

**Key Characteristics:**
- Non-linear price response
- Market size volatility
- Segment-specific demand elasticity

### Market Share Allocation

```python
def market_share(self, price_A, price_B, sensitivity):
    price_diff = (price_B - price_A) / ((price_A + price_B)/2 + 1e-9)
    share_A = 1 / (1 + np.exp(-sensitivity * price_diff))
```

**Logistic Transformation Properties:**
- Smooth market share transition
- Symmetrical response around price parity
- Continuous probability distribution

## Simulation Workflow

1. Initialize market and company parameters
2. Run iterative simulation (30 periods)
3. Generate demand scenarios
4. Apply pricing strategies
5. Calculate financial outcomes
6. Update cost structures
7. Visualize results

## Performance Metrics

- Cumulative Profit
- Market Share
- Price Elasticity
- Production Efficiency
- Inventory Management

## Visualization Outputs

The `plot_results()` function generates comprehensive visualizations:
- Profits per Period
- Cumulative Profits
- Pricing Trends
- Production Utilization
- Demand Dynamics
- Market Share Evolution
- Cost Structures

## Advanced Features

- Randomized buffer stock
- Incremental cost updates
- Flexible price candidate ranges
- Stochastic demand modeling

## Computational Requirements

- Python 3.8+
- NumPy
- Matplotlib
- PuLP (Linear Programming)
- Pandas (Result Export)

## Future Research Directions

1. Machine Learning Price Prediction
2. More Complex Market Segmentation
3. Multi-period Strategic Modeling
4. Risk Assessment Frameworks

## Limitations and Assumptions

- Simplified market model
- Limited number of price candidates
- Deterministic cost progression
- Binary decision frameworks

## Installation

```bash
git clone https://github.com/yourusername/market-simulation
pip install -r requirements.txt
python simulation.py
```

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create pull request

## License

[Specify your license - e.g., MIT, Apache]

---

**Note:** This simulation represents a theoretical model and should be interpreted as a research tool, not a definitive market prediction mechanism.

## Limitations and Future Work
- Extends basic Bertrand model with stochastic elements
- Can be enhanced with:
  - More complex cost structures
  - Additional market entry/exit mechanisms
  - Advanced consumer behavior models
  - Complex Inventory Management

## Author
[Your Name]
