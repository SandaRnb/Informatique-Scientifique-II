import math

class Euler:
    def __init__(self, a, b, h, alpha):
        self.a = a
        self.b = b
        self.h = h
        self.alpha = alpha
        self.N = round((b - a) / h)
    
    def fonction(self, t, y):
        return -y + t + 1

    @staticmethod
    def solution_exacte(t):
        return math.exp(-t) + t

    def euler(self, afficher=False):
        self.t = self.a
        self.w = self.alpha
        if afficher:
            self.affichage(self.t, self.w)

        for i in range(1, self.N + 1):
            self.w = self.w + self.h * self.fonction(self.t, self.w)
            self.t = self.a + i * self.h
            if afficher:
                self.affichage(self.t, self.w)

        return self.w

    def affichage(self, t, w):
        print(f"            t = {t:.2f} | w = {w:.6f}")


def main():
    a, b, alpha = 0, 5, 1
    exacte = Euler.solution_exacte(b)
    
    print("Sujet 1")
    print("**Approximation de y(5) utilisatant l'algorithme d'Euler")
    print("\n\na) Approximation de y(5) avec Euler avec h=0.2 , h=0.1 et h=0.05")
    
    for h in [0.2, 0.1, 0.05]:
        print(f"\nAvec h = {h:.2f} ")
        approximation = Euler(a, b, h, alpha).euler(afficher=True)
        
    
    print("b) Recherche du valeur optimal (par bisection)")
    h = 0.2
    while True:
        h /= 2.0
        approximation = Euler(a, b, h, alpha).euler(afficher=False)
        difference = abs(exacte - approximation)
        print(f"            h = {h:.8f} | w = {approximation:.8f}")
        if difference < 1e-6:
            break
        
    print(f"\n==>Valeur exacte y(5) = {exacte:.6f}\n")
    print(f"\nLa valeur optimale  est w = {approximation:.8f} ")


if __name__ == "__main__":
    main()