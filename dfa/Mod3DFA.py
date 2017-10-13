class Mod3DFA:
    @staticmethod
    def processString(stringx):
        state = 0
        dfa = {
            0: {'0': 0, '1': 1},
            1: {'0': 2, '1': 0},
            2: {'0': 1, '1': 2},
            3: {'0': 3, '1': 3}
        }

        for s in stringx:
            state = dfa[state].get(s, 3)

        return state == 0
