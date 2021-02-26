import random
import numpy as np

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

class Agent:
    def __init__self():
        self.alpha = 0
        self.epsilon = 0
        self.last_state = None
        self.last_action = None
        self.values = np.zeros((21, 10, 2))

    def arg_max(self, state):
        if self.values[state[0]][state[1]][0] > self.values[state[0]][state[1]][1]:
            return 0
        elif self.values[state[0]][state[1]][0] < self.values[state[0]][state[1]][1]:
            return 1
        else:
            return random.choice([0,1])

    def policy(self, state):
        greedy = random.random()
        if greedy > epsilon:
            return self.argmax(state)
        else:
            return random.choice([0,1])

    def step(self, state):
        action = self.policy(state)
        if action == 0:
            state[0] += deal_card(False)
        else:
            while state[1] < 17 and state[1] > 1:
                state[1] += deal_card(False)

        reward = give_reward(state)
        '''
        Update?
        '''

    def run_episode(self):
        '''
        generate start state
        step until terminal
        update?
        run_episode for i in range(num_episodes)
        '''


def deal_card(is_first):
    value = random.randint(1,10)
    if is_first:
        return value
    else:
        color = random.random()
        if color < .33:
            value = 0 - value
        return value

def is_terminal(state):
    if state[0] > 21 or state[0]< 1:
        return True
    elif agent.stick and (state[1] >= 17 or state[1] < 1):
        return True

    return False

def give_reward(state):
    if is_terminal(state):
        if state[0] > 21 or state[0] < 1:
            return -1
        elif state[1] > 21 or state[1] < 1:
            return 1
        elif state[0] > state[1]:
            return 1
        elif state[0] < state[1]:
            return -1
    return 0

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
