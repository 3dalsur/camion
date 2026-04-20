# ------------------------------------------------------------
# PROGRAMA: CAMIÓN
# DESCRIPCIÓN:
#   Análisis de momentos máximos en una viga simplemente apoyada
#   debido a una carga móvil de camión de tres ejes,
#   más peso propio distribuido.
#
#   Traducción directa desde Fortran 77 a Python
#   (misma lógica y algoritmo)
# ------------------------------------------------------------

def camion():
    print("\n" + " " * 20 + "INGRESO DE DATOS")
    print(" " * 20 + "*" * 16)

    # -----------------------------
    # INGRESO DE DATOS
    # -----------------------------
    P1 = float(input("\nCarga del eje delantero [Ton] ===> "))
    P2 = float(input("Carga del eje central   [Ton] ===> "))
    P3 = float(input("Carga del eje trasero   [Ton] ===> "))

    Q1, Q2, Q3 = P1, P2, P3

    L  = float(input("\nLuz de la viga [m] ===> "))
    A  = float(input("Distancia eje delantero-central [m] ===> "))
    B  = float(input("Distancia eje central-trasero   [m] ===> "))
    PL = float(input("Incremento longitudinal Δx [m] ===> "))
    Q  = float(input("Carga de peso propio [Ton/m] ===> "))

    print("\n" + " " * 23 + "***** RESOLVIENDO *****\n")

    # -----------------------------
    # FACTOR DINÁMICO
    # -----------------------------
    IM = 1.0 + 15.24 / (L + 38.11)
    IM = min(IM, 1.3)   # límite superior

    # -----------------------------
    # DISCRETIZACIÓN DE LA VIGA
    # -----------------------------
    num_puntos = int(L / PL) + 1
    MM = [0.0] * num_puntos  # momentos máximos por coordenada

    # -----------------------------
    # BUCLE DE DESPLAZAMIENTO DEL CAMIÓN
    # -----------------------------
    X = 0.0
    while X <= (L + A + B):

        Y = X - A
        Z = Y - B

        # Cargas activas
        p1, p2, p3 = Q1, Q2, Q3

        if X > L:
            p1 = 0.0
        if X > L + A:
            p2 = 0.0
        if Y <= 0.0:
            p2 = 0.0
            p3 = 0.0
        if Z <= 0.0:
            p3 = 0.0

        # -----------------------------
        # REACCIONES
        # -----------------------------
        RA = (p1*(L - X) + p2*(L - Y) + p3*(L - Z)) / L
        RB = (p1*X + p2*Y + p3*Z) / L

        # -----------------------------
        # MOMENTOS EN LA VIGA
        # -----------------------------
        S = 0.0
        n = 0
        while S <= L:
            U = max(S - X, 0.0)
            V = max(S - Y, 0.0)
            W = max(S - Z, 0.0)

            M = (RA * S - p1 * U - p2 * V - p3 * W) * IM

            if M > MM[n]:
                MM[n] = M

            S += PL
            n += 1

        X += PL

    # -----------------------------
    # SALIDA DE RESULTADOS
    # -----------------------------
    print("\nDISTRIBUCIÓN DE MOMENTOS\n")
    print(f"Carga eje delantero   = {Q1:6.3f} Ton")
    print(f"Carga eje central     = {Q2:6.3f} Ton")
    print(f"Carga eje trasero     = {Q3:6.3f} Ton")
    print(f"Luz de la viga        = {L:6.3f} m")
    print(f"Separación ejes A     = {A:6.3f} m")
    print(f"Separación ejes B     = {B:6.3f} m")
    print(f"Peso propio           = {Q:6.3f} Ton/m")

    print("\n" + "*" * 70)
    print(" Coordenada | Momento Camión | Momento P.P. | Momento Total")
    print("    [m]     |  [Ton·m]       |  [Ton·m]     |  [Ton·m]")
    print("*" * 70)

    DI = 0.0
    for n in range(num_puntos):
        MP = 0.5 * Q * DI * (L - DI)   # momento peso propio
        MT = MM[n] + MP               # momento total

        print(f" {DI:8.2f} | {MM[n]:14.4f} | {MP:12.4f} | {MT:14.4f}")
        DI += PL

    print("*" * 70)


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------
if __name__ == "__main__":
    camion()