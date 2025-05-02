import numpy as np
from scipy.special import ai_zeros


class Potential:
    @staticmethod
    def choose_potential(m: float):
        @staticmethod
        def choose_oscillator(omega, m: float):
            def oscillator(x):
                return 0.5 * 1 * (omega ** 2) * x ** 2

            @staticmethod
            def theoretical_energies(n: int):
                return [0.5 * omega * i for i in range(1, n)]

            return oscillator, theoretical_energies

        @staticmethod
        def choose_sech2(a, U0, m: float):
            def sech2(x):
                return -U0 / (np.cosh(x / a)) ** 2

            @staticmethod
            def theoretical_energies(n: int):
                s = 0.5 * (-1 + np.sqrt(1 + 8 * m * U0 * a ** 2))
                n = np.max([n, int(s - 1e-5) + 1])

                return [float(-(2 * m * a ** 2) ** (-1) * (s - i) ** 2) for i in range(0, n)]

            return sech2, theoretical_energies

        @staticmethod
        def choose_linear(F, m: float):
            def linear(x):
                if type(x) == float:
                    return F*x if x > 0 else -F*x

                return np.where(x > 0, F*x, -F*x)

            @staticmethod
            def theoretical_energies(n: int):
                nAiprimezeros = int(-0.1 + n / 2) + 1
                nAizeros = n - nAiprimezeros
                Aizeros, Aiprimezeros = ai_zeros(nAiprimezeros)[:2]

                energies = []

                for i in range(nAizeros):
                    energies.append(float((F ** 2 / (2 * m)) ** (1 / 3) * abs(Aiprimezeros[i])))
                    energies.append(float((F ** 2 / (2 * m)) ** (1 / 3) * abs(Aizeros[i])))
                if nAiprimezeros > nAizeros:
                    energies.append(float((F ** 2 / (2 * m)) ** (1 / 3) * abs(Aiprimezeros[-1])))

                return energies

            return linear, theoretical_energies

        print("Выберите тип потенциала: 1 - осциллятор, 2 - sech2, 3 - линейный")
        inp = input()
        if inp == "1":
            print("Введите частоту осциллятора в атомных единицах")
            chosen_omega = float(input())
            chosen_potential = choose_oscillator(chosen_omega, m)
        elif inp == "2":
            print("Введите характерное расстояние a в атомных единицах")
            choosen_a = float(input())
            print("Введите глубину потенциала U0 в атомных единицах")
            choosen_U0 = float(input())
            chosen_potential = choose_sech2(choosen_a, choosen_U0, m)
        elif inp == "3":
            print("Введите силу F>0")
            chosen_F = abs(float(input()))
            chosen_potential = choose_linear(chosen_F, m)
        else:
            raise Exception("No potential chosen")

        return chosen_potential



