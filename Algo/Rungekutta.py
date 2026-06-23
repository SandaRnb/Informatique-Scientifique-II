class RungeKutta:
    
    def __init__(self, a, b, h, alpha):
        self.a = a
        self.b = b
        self.h = h
        self.alpha = alpha
        self.N = round((b - a) / h)

    def fonction(self, t, y):
        return (1/t**2) - (y/t) - y**2
    
    @staticmethod
    def solution_exacte_rungekutta(t):
        return -1/t 
    
    def rungekutta(self, afficher=False, comparaison=False):
        self.t = self.a
        self.w = self.alpha
        if afficher:
            self.affichage(self.t, self.w, comparaison)

        for i in range(1, self.N + 1):
            k1 = self.h*self.fonction(self.t, self.w)
            k2 = self.h*self.fonction(self.t + self.h/2, self.w + k1/2)
            k3 = self.h*self.fonction(self.t + self.h/2, self.w + k2/2)
            k4 = self.h*self.fonction(self.t + self.h, self.w + k3)
            
            self.w = self.w + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
            self.t = self.a + i * self.h
            if afficher:
                self.affichage(self.t, self.w, comparaison)
                
        return self.w
    
    def affichage(self, t, w, comparaison=False):
        if comparaison:
            y_exact = self.solution_exacte_rungekutta(t)
            print(f"            t = {t:.2f} | w = {w:.6f} | y = {y_exact:.6f}")
        else:
            print(f"            t = {t:.2f} | w = {w:.6f}")
                
def main():
    a, b, alpha, h = 1, 2, -1, 0.1
    exacte = RungeKutta.solution_exacte_rungekutta(b)
    print("\nSujet 3")
    print("**Approximation en utilisant l'algorithme de Runge-Kutta d'ordre 4")
    
    print(f"\nAvec h = {h:.2f} ")
    
    print("\na) Approximation de y en utilisant l'algorithme de Runge-Kutta d'ordre 4 avec h=0.1:")
    RungeKutta(a, b, h, alpha).rungekutta(afficher=True, comparaison=False)
    
    print("\nb) Comparaison de celle-ci avec la valeur actuelle de y:")
    approximation_b = RungeKutta(a, b, h, alpha).rungekutta(afficher=True, comparaison=True)
        
    print(f"\n==>Valeur exacte = {exacte:.6f}\n")
    print(f"==>Valeur optimale = {approximation_b:.6f}\n")

if __name__ == "__main__":
    main()