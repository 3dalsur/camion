def calcular_camion(P1, P2, P3, L, A, B, PL, Q):
    IM = 1.0 + 15.24 / (L + 38.11)
    IM = min(IM, 1.3)

    num_puntos = int(L / PL) + 1
    MM = [0.0] * num_puntos

    X = 0.0
    while X <= (L + A + B):
        Y = X - A
        Z = Y - B

        p1, p2, p3 = P1, P2, P3
        if X > L:
            p1 = 0.0
        if X > L + A:
            p2 = 0.0
        if Y <= 0.0:
            p2 = 0.0
            p3 = 0.0
        if Z <= 0.0:
            p3 = 0.0

        RA = (p1*(L-X) + p2*(L-Y) + p3*(L-Z)) / L

        S = 0.0
        n = 0
        while S <= L:
            U = max(S - X, 0.0)
            V = max(S - Y, 0.0)
            W = max(S - Z, 0.0)
            M = (RA*S - p1*U - p2*V - p3*W) * IM
            if M > MM[n]:
                MM[n] = M
            S += PL
            n += 1

        X += PL

    resultados = []
    DI = 0.0
    for n in range(len(MM)):
        MP = 0.5 * Q * DI * (L - DI)
        MT = MM[n] + MP
        resultados.append((DI, MM[n], MP, MT))
        DI += PL

    return resultados