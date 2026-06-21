import math

class Taylor:
    def __init__(self, a, b, h, alpha):
        self.a = a
        self.b = b
        self.h = h
        self.alpha = alpha
        self.N = round((b - a) / h)

    def f(self, t, w):
        return 1 + t * math.sin(t * w)
    
    def fprime(self, t, w):
        return math.sin(t * w) + t * (w + t * self.f(t, w)) * math.cos(t * w)

    @staticmethod
    def solution_exacte(t):
        return math.exp(-t) + t

    def taylor(self, afficher=False, comparaison=False):
        self.t = self.a
        self.w = self.alpha
        if afficher:
            self.affichage(self.t, self.w, comparaison)

        for i in range(1, self.N + 1):
            f = self.f(self.t, self.w)
            fp = self.fprime(self.t, self.w)

            self.w = self.w + self.h * f + (self.h**2 / 2) * fp
            self.t = self.a + i * self.h
            if afficher:
                self.affichage(self.t, self.w, comparaison)

        return self.w

    def affichage(self, t, w, comparaison=False):
        if comparaison:
            y_exact = self.solution_exacte(t)
            print(f"            t = {t:.2f} | w = {w:.6f} | y = {y_exact:.6f}")
        else:
            print(f"            t = {t:.2f} | w = {w:.6f}")


def main():
    a, b, alpha, h = 0, 2, 0, 0.1
    exacte = Taylor.solution_exacte(b)

    print("Sujet 2")
    print("**Approximation en utilisant l'algorithme de Taylor d'ordre 2")
    print(f"\nAvec h = {h:.2f} ")
    
    print("\n(a) Approximation de y en utilisant l'algorithme de TAYLOR d'ordre 2 avec h=0.1:")
    Taylor(a, b, h, alpha).taylor(afficher=True, comparaison=False)
    
    print("\n(b) Comparaison de celle-ci avec la valeur actuelle de y:")
    approximation_b = Taylor(a, b, h, alpha).taylor(afficher=True, comparaison=True)

    print(f"\n==>Valeur exacte  = {exacte:.6f}\n")
    print(f"==>Valeur approchée  = {approximation_b:.6f}\n")


if __name__ == "__main__":
    main()