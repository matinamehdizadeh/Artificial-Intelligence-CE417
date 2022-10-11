#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install gym')


# In[54]:


import random

import gym
import numpy as np


# In[55]:


env = gym.make('MountainCar-v0')
num_actions = 3

num_states = int(((0.6-(-1.2))*10+1)*((0.07-(-0.07))*100+1))
q_table = np.zeros(shape=(num_states, num_actions))


# In[56]:


def discretize_state(x, min, step):
    """
    this is just one example of a discretization function. you can change it as you want:)
    """
    return round((x - min) / step)


# In[113]:


def env_state_to_Q_state(state):
   [position, velocity] = state
   """
   return value: [int]
   your code here.
   hint: use discretize_state func here for both of p and v and combine them somehow to reach a int.
   """
   i = discretize_state(position, -1.2, 0.1)
   j = discretize_state(velocity, -0.07, 0.01)
   return int(round(i*15 + j))


# In[114]:


def update_q(state, nState, action, reward, policy):
    """ your code here"""
    st = env_state_to_Q_state(state)
    Nst = env_state_to_Q_state(nState)
    sample = reward + 0.99 * np.max(q_table[Nst]) - q_table[st][action]
    Vupdate = 0.2 * sample
    q_table[st][action] += Vupdate
    policy[st] = action


# In[115]:


def get_action(state, epsilon):
    """your code here"""
    result = np.random.uniform()
    if result < epsilon:
        return random.randint(0, 2)
    else:
        st = env_state_to_Q_state(state)
        return np.argmax(q_table[st])


# In[124]:


def q_learning(episodes):
    """your code here"""
    epsilon = 1
    policy = [0] * num_states
    dec = (epsilon) / episodes

    for i in range(episodes):
        done = False
        state = env.reset()
        
        while not done:

            action = get_action(state, epsilon)
            new_state, reward, done, info = env.step(action)
            st = env_state_to_Q_state(state)
            if done and new_state[0] >= 0.5:
                q_table[st][action] = reward
                policy[st] = action
            else:
                update_q(state, new_state, action, reward, policy)
            state = new_state
            if epsilon > 0:
                epsilon -= dec


    env.close()
    policy =np.asarray(policy)
    return policy


# In[125]:


def save_policy():
    """save your optimal policy to a file with name policy.npy"""
    policy = q_learning(5000)
    np.save('policy.npy', policy)


# In[126]:


def score():
    policy, scores = np.load('policy.npy'), []
    print(policy)
    for episode in range(1000):
        print('******Episode ', episode)
        state, score, done, step = env_state_to_Q_state(env.reset()), 0, False, 0
        while not done:
            # time.sleep(0.04)
            action = policy[state]
            state, reward, done, _ = env.step(action)
            state = env_state_to_Q_state(state)
            step += 1
            score += int(reward)
            # env.render()
        print('Score:', score)
        scores.append(score)
        
    print("Average score over 1000 run : ", np.array(scores).mean())


if __name__ == '__main__':
    save_policy()
    score()


# In[ ]:




