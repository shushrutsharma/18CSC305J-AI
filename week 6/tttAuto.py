import numpy
import time
import sys
import pickle
start = time.time()
try:
  with open('mydict','rb') as f:
    print('using previous file')
    mydict = pickle.load(f)
except:
  mydict = {}
class Player:

    def __init__(self, id):
        self.id = id
        self.win_seq = numpy.array([id, id, id])

    def get_actions(self, state):
        coords = numpy.asarray(numpy.where(state == 0)).T
        return [tuple(i) for i in coords]

    def apply_action(self, state, action):
        state[action] = self.id
        return state

    def undo_action(self, state, action):
        state[action] = 0
        return state

    def is_win(self, state):
        for i, row in enumerate(state):
            if search_sequence(row, self.win_seq):
                return True

            if search_sequence(state[:, i], self.win_seq):
                return True

        for diag in get_diags(state):
            if search_sequence(diag, self.win_seq):
                return True

        return False

    def get_decision(self, state, enemy):
        self.enemy = enemy
        actions = self.get_actions(state)
        best_i = None
        best_val = -sys.maxsize

        for i, action in enumerate(actions):
            val = self.minimax(self.apply_action(state, action), 0, False)
            state[action] = 0

            if val > best_val:
                best_i = i
                best_val = val

        return actions[best_i]

    def minimax(self, state, depth, is_max):
        try:
          return mydict[tuple(state.flatten())]
        except:
          pass
        if self.is_win(state):
            return 10 - depth
        elif self.enemy.is_win(state):
            return -10 + depth
        elif self.is_full(state):
            return 0

        actions = self.get_actions(state)

        if is_max:
            best = -sys.maxsize

            for action in actions:
                val = self.minimax(self.apply_action(state, action), depth + 1, False)
                self.undo_action(state, action)
                best = max(best, val)
        else:
            best = sys.maxsize

            for action in actions:
                val = self.minimax(self.enemy.apply_action(state, action), depth + 1, True)
                self.undo_action(state, action)
                best = min(best, val)

        mydict[tuple(state.flatten())]=best

        return best

    def is_full(self, state):
        fields = state == 0
        return not fields.any()

def search_sequence(arr, seq):
    r_seq = numpy.arange(seq.shape[0])
    M = (arr[numpy.arange(arr.shape[0] - seq.shape[0] + 1)[:, None] + r_seq] == seq).all(1)
    return M.any() > 0

def get_diags(state):
    diags = [state[::-1,:].diagonal(i) for i in range(-state.shape[0] + 1, state.shape[1])]
    diags.extend(state.diagonal(i) for i in range(state.shape[1]-1,-state.shape[0],-1))
    return diags

me = Player(1)
enemy = Player(2)

state = numpy.array([
    [1, 0, 0, 1],
    [0, 2, 0, 0],
    [0, 0, 1, 0],
    [1, 2, 2, 1]
])

decision = me.get_decision(state, enemy)

print(state)
print(decision)
print(me.apply_action(state, decision))

print(time.time() - start, "s")

with open('mydict','wb') as f:
  pickle.dump(mydict,f)