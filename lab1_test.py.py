import matplotlib.pyplot as plt
from decimal import Decimal, getcontext, ROUND_FLOOR, ROUND_HALF_UP

# --- CONFIGURATION ---
# 1. Set precision high enough (150) to handle the 100th decimal test
getcontext().prec = 150

# 2. Physics Constants
# Length of the pendulum (67 meters, like the Arts et Métiers Pendulum)
LENGTH = Decimal('67.0') 
GRAVITY = Decimal('9.80665')

# 3. The True Value of Pi (100 digits)
PI_TRUE = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')

def get_time_error(n_decimals):
    """
    Calculates the error in TIME (Seconds) for one full swing.
    """
    # Create a formatter to cut Pi to 'n' decimals
    fmt = Decimal('1.' + '0' * n_decimals)
    
    # Define the two competing Pi values
    pi_trunc = PI_TRUE.quantize(fmt, rounding=ROUND_FLOOR)   # 3.1415...
    pi_round = PI_TRUE.quantize(fmt, rounding=ROUND_HALF_UP) # 3.1416...
    
    # THE FORMULA: T = 2 * pi * sqrt(L / g)
    physics_part = (LENGTH / GRAVITY).sqrt()
    
    time_true  = Decimal(2) * PI_TRUE * physics_part
    time_trunc = Decimal(2) * pi_trunc * physics_part
    time_round = Decimal(2) * pi_round * physics_part
    
    # Calculate the Absolute Error
    err_trunc = abs(time_true - time_trunc)
    err_round = abs(time_true - time_round)
    
    return err_trunc, err_round

# --- RUN THE EXPERIMENT ---
precisions = [20, 40, 60, 100]
trunc_results = []
round_results = []

# Header with the GAP column
print(f"{'Decimal':<8} | {'Truncated Err':<18} | {'Rounded Err':<18} | {'GAP (Difference)':<18}")
print("-" * 75)

for p in precisions:
    t_err, r_err = get_time_error(p)
    trunc_results.append(t_err)
    round_results.append(r_err)
    
    # Calculate the GAP (How much better is Rounding?)
    gap = t_err - r_err
    
    # Print results (using scientific notation for tiny numbers)
    print(f"{p:<8} | {float(t_err):<.2e} | {float(r_err):<.2e} | {float(gap):<.2e}")

# --- VISUALIZE ---
plt.figure(figsize=(10, 6))

# Plotting on Log Scale
plt.semilogy(precisions, trunc_results, label='Truncation (3.14...)', marker='o', color='red', linestyle='--')
plt.semilogy(precisions, round_results, label='Rounding (3.15...)', marker='s', color='green', linestyle='-')

plt.title('Pendulum Time Error: Truncation vs Rounding')
plt.xlabel('Decimal Precision of Pi')
plt.ylabel('Time Error per Swing (Seconds)')
plt.grid(True, which="both", linestyle="--", alpha=0.7)
plt.legend()

plt.show()