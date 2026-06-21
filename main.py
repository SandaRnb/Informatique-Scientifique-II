from Algo.Euler import main as main_euler
from Algo.Taylor import main as main_taylor
from Algo.Rungekutta import main as main_rungekutta

if __name__ == "__main__":
    print()
    print("TP INFORMATIQUE SCIENTIFIQUE II - Euler, Taylor et Runge-Kutta")
    print("" + "-"*80)
    
    main_euler()
    
    print("\n" + "-"*80)
    main_taylor()
    
    print("\n" + "-"*80)
    main_rungekutta()
    
    print("\n" + "-"*80)
