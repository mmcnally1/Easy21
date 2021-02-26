'''
- infinite deck of cards (sampled w/ replacement)
- each draw uniformly dist. b/w 1-10 (2/3 black, 1/3 red)
- start: player, dealer draw one black card (observed)
- each turn: may stick or hit
- black cards added, red cards subtracted
- > 21, < 1 = bust (reward -1)
- once player sticks, dealer's turn
- dealer sticks if sum >= 17, else hits
- rewards: win = +1, draw = 0, lose = -1
'''

class Card:
    '''
    value - int (1-10)
    color - (red/black)
    '''
    def __init__(self, value, color):
        self.value = value
        self.color = color

class Player:
    def __init__(self):
        self.cards = []
        self.stick = False

class Dealer:
    def __init__(self):
        self.cards = []
        self.stick = False

    def hit_or_stick(self):
        if score(self.cards) >= 17:
            self.stick = True
        return self.stick

class State:
    def __init__(self):
        self.dealer_card = None
        self.player_sum = None
        self.action = None
        self.terminal = False

def step(state, action):
    '''
    input: state - dealer's first card, player's sum
           action - hit/stick
    returns: next_state, reward
    '''
    pass

def deal_next_card():
    '''
    deal random card from 1-10 (1/3 prob red, 2/3 prob black)
    '''
    pass

def score(cards):
    '''
    input: list of cards
    return: score (sum of black cards minus sum of red cards)
    '''
    pass

def is_terminal(state, dealer):
    if state.player_sum > 21 or state.player_sum < 1:
        return True

    if score(dealer.cards) > 21 or score(dealer.cards) < 1:
        return True

    return False


def monte_carlo():
    '''
    initialize value funct to 0
    step_size = 1 / N(St,At)
    epsilon = N_zero / (N_zero + N(St))
        N_zero = 100 (can modify), N(s) = num times state s
        has been visited, N(s,a) = num times action
        a has been selected in state s
    plot optimal value function V*(s) = max_a(Q*(s,a))
    '''
    pass

def td_learning():
    '''
    implement sarsa(lambda) w/ same step size, epsilon as MC
    run 1000 episodes w/ lambda = {0,.1,...1}
    return mean squared error over all states, actions
        plot against lambda
    '''
    pass

def linear_funct_approx():
    '''
    use binary feature vector phi(s,a) w/ 3*6*2 = 36 features
        feature has val 1 iff (s,a) ies w/in state space and action
        intevals: dealer = {[1,4],[4,7],[7,10]}
                  player = {[1,6],[4,9],[7,12],[10,15],[13,18],[16,21]}
                  a = {hit, stick}
    repeat sarsa exp. but w/ LFA -> Q(s,a) = phi.T * theta
    epsilon = .05
    alpha = .01
    plot curve for MSE vs. lambda
    '''
    pass
