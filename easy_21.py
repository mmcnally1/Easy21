import random
import numpy as np
from copy import deepcopy

class Agent:
    def __init__(self):
        self.stick = False
        self.alpha = .5
        self.epsilon = .05
        self.values = np.zeros((21, 10, 2))

    def step(self, state, action):
        if action == 0:
            state[0] += deal_card(False)
        else:
            self.stick = True
            while state[1] < 17 and state[1] >= 1:
                state[1] += deal_card(False)

        return give_reward(state, self)

    def choose_action(self, state, policy):
        greedy = random.random()
        if greedy > self.epsilon:
            action = policy[state[0] - 1][state[1] - 1]
        else:
            action = random.randint(0,1)
        return action

def deal_card(is_first):
    '''
    First card for dealer and agent is black (positive value),
    for subsequent cards prob(black) = 2/3, prob(red) = 1/3
    '''
    value = random.randint(1,10)
    if is_first:
        return value
    else:
        color = random.random()
        if color < .33:
            value = 0 - value
        return value

def is_terminal(state, agent):
    if state[0] > 21 or state[0]< 1:
        return True

    elif agent.stick and (state[1] >= 17 or state[1] < 1):
        return True

    return False

def give_reward(state, agent):
    if is_terminal(state, agent):
        if state[0] > 21 or state[0] < 1:
            return -1
        elif state[1] > 21 or state[1] < 1:
            return 1
        elif state[0] > state[1]:
            return 1
        elif state[0] < state[1]:
            return -1
    return 0


def monte_carlo(agent, num_episodes):
    policy = [[0 for i in range(10)] for i in range(21)]
    returns = [[[[],[]] for i in range(10)] for i in range(21)]

    for i in range(num_episodes):
        agent.stick = False
        G = 0
        state = [deal_card(True), deal_card(True)]
        while not is_terminal(state, agent):
            last_state = deepcopy(state)
            action = agent.choose_action(state, policy)
            reward = agent.step(state, action)
            G += reward
            returns[last_state[0] - 1][last_state[1] - 1][action].append(G)
            agent.values[last_state[0] - 1][last_state[1] - 1][action] = np.average(returns[last_state[0] - 1][last_state[1] - 1][action])
            policy[last_state[0] - 1][last_state[1] - 1] = np.argmax(agent.values[last_state[0] - 1][last_state[1] - 1])
    return policy

def sarsa(agent, num_episodes):
    policy = [[0 for i in range(10)] for i in range(21)]
    for i in range(num_episodes):
        state = [deal_card(True), deal_card(True)]
        action = agent.choose_action(state, policy)
        while not is_terminal(state, agent):
            last_state = deepcopy(state)
            last_action = action
            reward = agent.step(state, action)
            if not is_terminal(state, agent):
                action = agent.choose_action(state, policy)
                agent.values[last_state[0] - 1][last_state[1] - 1][last_action] += agent.alpha * (reward + agent.values[state[0] - 1][state[1] - 1][action] -
                                                                                                    agent.values[last_state[0] - 1][last_state[1] - 1][last_action])
            else:
                agent.values[last_state[0] - 1][last_state[1] - 1][last_action] += agent.alpha * (reward - agent.values[last_state[0] - 1][last_state[1] - 1][last_action])

            policy[last_state[0] - 1][last_state[1] - 1] = np.argmax(agent.values[last_state[0] - 1][last_state[1] - 1])


def linear_funct_approx(agent, num_episodes):
    policy = [[0 for i in range(10)] for i in range(21)]
    for i in range(num_episodes):
        state = [deal_card(True), deal_card(True)]
        action = agent.choose_action(state, policy)
        while not is_terminal(state, agent):
            last_state = deepcopy(state)
            last_action = action
            reward = agent.step(state, action)
            if not is_terminal(state, agent):
                action = agent.choose_action(state, policy)
                agent.values[last_state[0] - 1][last_state[1] - 1][last_action] += agent.alpha * (reward + agent.values[state[0] - 1][state[1] - 1][action] -
                                                                                                    agent.values[last_state[0] - 1][last_state[1] - 1][last_action])
            else:
                agent.values[last_state[0] - 1][last_state[1] - 1][last_action] += agent.alpha * (reward - agent.values[last_state[0] - 1][last_state[1] - 1][last_action])

            policy[last_state[0] - 1][last_state[1] - 1] = np.argmax(agent.values[last_state[0] - 1][last_state[1] - 1])


if __name__ == "__main__":
    #mc_agent = Agent()
    #sarsa_agent = Agent()
    lfa_agent = Agent()
    #monte_carlo(mc_agent, 10000)
    #sarsa(sarsa_agent, 10000)
    linear_funct_approx(lfa_agent, 10000)
