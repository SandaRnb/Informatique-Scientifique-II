import math

class Taylor:
    def __init__(self, a, b, h, alpha):
        self.a = a
        self.b = b
        self.h = h
        self.alpha = alpha
        self.N = round((b - a) / h)

    def fonction(self, t, y):
        return 1 + t * math.sin(t * y)

    def derivee_fonction(self, t, y):
        df_dt = math.sin(t * y) + t * y * math.cos(t * y)
        df_dy = t**2 * math.cos(t * y)
        return df_dt + df_dy * self.fonction(t, y)

    @staticmethod
    def solution_exacte(t):
        return math.exp(-t) + t

    def taylor(self, afficher=False):
        self.t = self.a
        self.w = self.alpha
        if afficher:
            self.affichage(self.t, self.w)

        for i in range(1, self.N + 1):
            f = self.fonction(self.t, self.w)
            fp = self.derivee_fonction(self.t, self.w)

            self.w = self.w + self.h * f + (self.h**2 / 2) * fp
            self.t = self.a + i * self.h
            if afficher:
                self.affichage(self.t, self.w)

        return self.w

    def affichage(self, t, w):
        print(f"            t = {t:.6f} | w = {w:.6f}")


def main():
    a, b, alpha, h = 0, 2, 0, 0.1
    exacte = Taylor.solution_exacte(b)

    print("Sujet 3")
    print("Approximation de y(2) en utilisant l'algorithme de Taylor d'ordre 2")
    print(f"\nAvec h = {h:.2f} ")

    approximation = Taylor(a, b, h, alpha).taylor(afficher=True)

    print(f"\n==>Valeur exacte  = {exacte:.6f}\n")
    print(f"==>Valeur approchée  = {approximation:.6f}\n")


if __name__ == "__main__":
    main()