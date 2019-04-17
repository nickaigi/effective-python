""" pickle can serialized python objects into a stream of bytes and deserialize bytes back into objects.
Note:
    by design, pickle is unsafe!
"""


import pickle


state_path = 'game_state.bin'


class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4


def save_game(state):
    with open(state_path, 'wb') as f:
        pickle.dump(state, f)


def load_game():
    state_after = {}
    with open(state_path, 'rb') as f:
        state_after = pickle.load(f)
    return state_after


def example_one():
    """
    >>> 
    {'level': 1, 'lives': 3}
    """
    state = GameState()
    state.level += 1
    state.lives -= 1

    save_game(state)

    saved_state = load_game()
    print(saved_state.__dict__)


class GameStateNew(object):
    def __init__(self):
        self.level = 0
        self.lives = 4
        self.points = 0


def example_two():
    """
    >>> 
    {'level': 0, 'lives': 4, 'points': 0}
    """
    state = GameStateNew()
    serialized = pickle.dumps(state)  # dumps
    state_after = pickle.loads(serialized)  # loads
    print(state_after.__dict__)


def main():
    example_two()


if __name__ == '__main__':
    main()
