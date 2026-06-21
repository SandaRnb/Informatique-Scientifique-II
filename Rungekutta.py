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
    
    def rungekutta(self, afficher=False):
        self.t = self.a
        self.w = self.alpha
        if afficher:
            self.affichage(self.t, self.w)

        for i in range(1, self.N + 1):
            k1 = self.h*self.fonction(self.t, self.w)
            k2 = self.h*self.fonction(self.t + self.h/2, self.w + k1/2)
            k3 = self.h*self.fonction(self.t + self.h/2, self.w + k2/2)
            k4 = self.h*self.fonction(self.t + self.h, self.w + k3)
            
            self.w = self.w + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
            self.t = self.a + i * self.h
            if afficher:
                self.affichage(self.t, self.w)
                
        return self.w
    
    def affichage(self, t, w):
        print(f"            t = {t:.6f} | w = {w:.6f}")
                
def main():
    a, b, alpha, h = 1, 2, -1, 0.1
    exacte = RungeKutta.solution_exacte_rungekutta(b)
    print("\nSujet 2")
    print("Approximation en utilisant l'algorithme de Runge-Kutta d'ordre 4")
    
    print(f"\nAvec h = {h:.2f} ")
    
    approximation = RungeKutta(a, b, h, alpha).rungekutta(afficher=True)
        
    print(f"\n==>Valeur exacte = {exacte:.6f}\n")
    print(f"==>Valeur optimale = {approximation:.6f}\n")

if __name__ == "__main__":
    main()