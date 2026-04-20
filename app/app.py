import reflex as rx

# ======================================================
# ESTADO DE LA APLICACIÓN
# ======================================================
class CamionState(rx.State):

    # Entradas
    P1: float = 0.0
    P2: float = 0.0
    P3: float = 0.0
    L: float = 0.0
    A: float = 0.0
    B: float = 0.0
    PL: float = 0.2
    Q: float = 0.0

    # Resultados
    output: str = ""

    def calcular(self):
        Q1, Q2, Q3 = self.P1, self.P2, self.P3

        # Factor dinámico
        IM = 1.0 + 15.24 / (self.L + 38.11)
        IM = min(IM, 1.3)

        # Discretización
        num_puntos = int(self.L / self.PL) + 1
        MM = [0.0] * num_puntos

        # Desplazamiento del camión
        X = 0.0
        while X <= (self.L + self.A + self.B):

            Y = X - self.A
            Z = Y - self.B

            p1, p2, p3 = Q1, Q2, Q3

            if X > self.L:
                p1 = 0.0
            if X > self.L + self.A:
                p2 = 0.0
            if Y <= 0.0:
                p2 = 0.0
                p3 = 0.0
            if Z <= 0.0:
                p3 = 0.0

            RA = (p1*(self.L-X) + p2*(self.L-Y) + p3*(self.L-Z)) / self.L

            S = 0.0
            n = 0
            while S <= self.L:
                U = max(S - X, 0.0)
                V = max(S - Y, 0.0)
                W = max(S - Z, 0.0)

                M = (RA * S - p1 * U - p2 * V - p3 * W) * IM

                if M > MM[n]:
                    MM[n] = M

                S += self.PL
                n += 1

            X += self.PL

        # Salida
        resultado = []
        DI = 0.0
        resultado.append("Coord (m) | M_camión | M_p.p | M_total")
        resultado.append("-" * 40)

        for n in range(len(MM)):
            MP = 0.5 * self.Q * DI * (self.L - DI)
            MT = MM[n] + MP
            resultado.append(
                f"{DI:8.2f} | {MM[n]:8.2f} | {MP:6.2f} | {MT:8.2f}"
            )
            DI += self.PL

        self.output = "\n".join(resultado)


# ======================================================
# INTERFAZ WEB
# ======================================================
def index():
    return rx.container(
        rx.heading("Análisis de Viga – Carga Móvil de Camión"),

        rx.vstack(
            rx.input(placeholder="Carga eje delantero", on_change=CamionState.set_P1),
            rx.input(placeholder="Carga eje central", on_change=CamionState.set_P2),
            rx.input(placeholder="Carga eje trasero", on_change=CamionState.set_P3),
            rx.input(placeholder="Luz de la viga", on_change=CamionState.set_L),
            rx.input(placeholder="Distancia eje A", on_change=CamionState.set_A),
            rx.input(placeholder="Distancia eje B", on_change=CamionState.set_B),
            rx.input(placeholder="Incremento ?x", on_change=CamionState.set_PL),
            rx.input(placeholder="Peso propio [Ton/m]", on_change=CamionState.set_Q),

            rx.button("Calcular", on_click=CamionState.calcular),
            rx.text_area(value=CamionState.output, rows=20),
        )
    )


app = rx.App()
app.add_page(index)