import numpy as np

class Potential:
    @staticmethod
    def choose_potential():
        @staticmethod
        def choose_oscillator(omega):
            def oscillator(x):
                return 0.5 * 1 * (omega ** 2) * x ** 2

            return oscillator

        @staticmethod
        def choose_sech2(a, U0):
            def sech2(x):
                # a = 1
                # U0 = 14 / 2
                return -U0 / (np.cosh(x / a)) ** 2

            return sech2

        @staticmethod
        def choose_linear(a):
            def linear(x):
                if type(x) == float:
                    return a*x if x > 0 else -a*x

                return np.where(x > 0, a*x, -a*x)

            return linear

        print("Выберите тип потенциала: 1 - осциллятор, 2 - sech2, 3 - линейный")
        inp = input()
        if inp == "1":
            print("Введите частоту осциллятора в атомных единицах")
            chosen_omega = float(input())
            chosen_potential = choose_oscillator(chosen_omega)
        elif inp == "2":
            print("Введите характерное расстояние a в атомных единицах")
            choosen_a = float(input())
            print("Введите глубину потенциала U0 в атомных единицах")
            choosen_U0 = float(input())
            chosen_potential = choose_sech2(choosen_a, choosen_U0)
        elif inp == "3":
            print("Введите коэффициент наклона a>0")
            choosen_a = abs(float(input()))
            chosen_potential = choose_linear(choosen_a)
        else:
            raise Exception("No potential chosen")

        return chosen_potential



