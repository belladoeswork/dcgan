# from torch import nn
# import torch
# import gym
# import numpy as np
# import random
# import itertools
# from collections import deque



# GAMMA = 0.99
# BATCH_SIZE = 32
# BUFFER_SIZE = 50000
# MIN_REPLAY_SIZE = 1000
# EPSILON_START = 1.0
# EPSILON_END = 0.02
# EPSILON_DECAY = 10000
# TARGET_UPDATE_FREQ = 1000


# class Newtwork(nn.Module):
#     def __init__(self, env):
#         super().__init__()
        
        
#         in_features = int(np.prod(env.observation_space.shape))
        
#         self.net = nn.Sequential(
#             nn.Linear(in_features, 64),
#             nn.Tanh(),
#             nn.Linear(64, env.action_space.n)
#         )



#     def forward(self, x):
#         return self.net(x)
    
#     # def act(self, obs):
#     #     # obs_t = torch.as_tensor(obs, dtype=torch.float32)
#     #     obs_t = torch.as_tensor(np.array(obs), dtype=torch.float32)
#     #     # print(f"obs_t.shape: {obs_t.shape}")
#     #     q_vals = self(obs_t.unsqueeze(0))
        
#     #     # max_q = torch.max(q_vals, dim=1)[0]
#     #     # action = max_q.detach().item()
        
#     #     _, action = torch.max(q_vals, dim=1)
#     #     action = action.item()
        
#     #     return action
    
#     def act(self, obs, epsilon):
#         if random.random() < epsilon:
#             return random.randrange(env.action_space.n)
#         else:
#             obs_t = torch.as_tensor(np.array(obs), dtype=torch.float32)
#             q_vals = self(obs_t.unsqueeze(0))
#             _, action = torch.max(q_vals, dim=1)
#             action = action.item()
#             return action






# env = gym.make('CartPole-v1')

# replay_buffer = deque(maxlen=BUFFER_SIZE)
# reward_buffer = deque([0.0],maxlen=100)
# episode_reward = 0.0
# online_net = Newtwork(env)
# target_net = Newtwork(env)
# target_net.load_state_dict(online_net.state_dict())
# optimizer = torch.optim.Adam(online_net.parameters(), lr=5e-4) 

# #init replay buffer
# obs = env.reset()
# for _ in range(MIN_REPLAY_SIZE):
#     action = env.action_space.sample()
#     # print(env.step(action))
#     next_obs, reward, done, _, _ = env.step(action)
#     transition = (obs, action, reward, done, next_obs)
#     replay_buffer.append(transition)
#     obs = next_obs
#     if done:
#         obs = env.reset()


# #main training loop
# obs = env.reset()

# for step in itertools.count():
#     epsilon = np.interp(step, [0, EPSILON_DECAY], [EPSILON_START, EPSILON_END])
    
#     # rnd_sample = random.random()
    
#     # if rnd_sample <= epsilon:
#     #     action = env.action_space.sample()
#     # else:
#     #     # print(f"obs: {obs}") 
#     #     # action = online_net.act(obs)
#     #     action = online_net.act(obs, epsilon)
        
#     # next_obs, reward, done, _ = env.step(action)
#     # transition = (obs, action, reward, next_obs, done)
#     # replay_buffer.append(transition)
#     # obs = next_obs
#     # episode_reward += reward
#     # if done:
#     #     reward_buffer.append(episode_reward)
#     #     obs, _ = env.reset()
#     #     episode_reward = 0.0
#     action = online_net.act(obs, epsilon)
#     next_obs, reward, done, _, _ = env.step(action)
#     transition = (obs, action, reward, next_obs, done)
#     replay_buffer.append(transition)
#     obs = next_obs
#     episode_reward += reward
#     if done:
#         reward_buffer.append(episode_reward)
#         obs = env.reset()
#         episode_reward = 0.0
        
#     # gradient steps
#     if len(replay_buffer) >= BATCH_SIZE:
#         transitions = random.sample(replay_buffer, BATCH_SIZE)
        
#         # Ensure all observations are of the same shape
#         obses = [t[0] for t in transitions]
#         if all(isinstance(obs, np.ndarray) for obs in obses):
#             obs_shapes = [obs.shape for obs in obses]
#             if len(set(obs_shapes)) > 1:
#                 print("Warning: observations have inconsistent shapes.")
#                 continue
#         obses = np.asarray(obses)

#         obses = np.asarray([t[0] for t in transitions])
#         actions = np.asarray([t[1] for t in transitions])
#         rews = np.asarray([t[2] for t in transitions])
#         next_obses = np.asarray([t[3] for t in transitions])
#         dones = np.asarray([t[4] for t in transitions])

#         obses_t= torch.as_tensor(obses, dtype=torch.float32)
#         actions_t= torch.as_tensor(actions, dtype=torch.int64).unsqueeze(-1)
#         rews_t = torch.as_tensor(rews, dtype=torch.float32).unsqueeze(-1)
#         # next_obses_t = torch.as_tensor(next_obses, dtype=torch.float32).unsqueeze(-1)
#         next_obses_t = torch.as_tensor(next_obses, dtype=torch.float32)
#         dones_t = torch.as_tensor(dones, dtype=torch.float32)


#         #compute targets Q values
#         target_q_values = target_net(next_obses_t)
#         # max_target_q_values = torch.max(keepdim=True, dim=1)[0]
#         max_target_q_values, _ = torch.max(target_q_values, dim=1, keepdim=True)

#         targets = rews_t + GAMMA * (1 - dones_t) * max_target_q_values


#         #compute loss
#         online_q_values = online_net(obses_t)
#         # action_q_values = torch.gather(imput=online_q_values, dim=1, index=actions_t)
#         action_q_values = torch.gather(input=online_q_values, dim=1, index=actions_t)
#         loss = nn.functional.smooth_l1_loss(action_q_values, targets)


#         #gradient step
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#     #update target network
#     if step % TARGET_UPDATE_FREQ == 0:
#         target_net.load_state_dict(online_net.state_dict())
        
        
#     #log
#     if step % 1000 == 0:
#         print('step:', step)
#         print('avg rew', np.mean(reward_buffer))


from torch import nn
import torch
import gym
import numpy as np
import random
import itertools
from collections import deque

GAMMA = 0.99
BATCH_SIZE = 32
BUFFER_SIZE = 50000
MIN_REPLAY_SIZE = 1000
EPSILON_START = 1.0
EPSILON_END = 0.02
EPSILON_DECAY = 10000
TARGET_UPDATE_FREQ = 1000

class Newtwork(nn.Module):
    def __init__(self, env):
        super().__init__()
        in_features = int(np.prod(env.observation_space.shape))
        self.net = nn.Sequential(
            nn.Linear(in_features, 64),
            nn.Tanh(),
            nn.Linear(64, env.action_space.n)
        )

    def forward(self, x):
        return self.net(x)

    def act(self, obs, epsilon):
        if random.random() < epsilon:
            return random.randrange(env.action_space.n)
        else:
            obs_t = torch.as_tensor(np.array(obs), dtype=torch.float32)
            q_vals = self(obs_t.unsqueeze(0))
            _, action = torch.max(q_vals, dim=1)
            action = action.item()
            return action

env = gym.make('CartPole-v1')

replay_buffer = deque(maxlen=BUFFER_SIZE)
reward_buffer = deque([0.0],maxlen=100)
episode_reward = 0.0
online_net = Newtwork(env)
target_net = Newtwork(env)
target_net.load_state_dict(online_net.state_dict())
optimizer = torch.optim.Adam(online_net.parameters(), lr=5e-4) 

obs = env.reset()
for _ in range(MIN_REPLAY_SIZE):
    action = env.action_space.sample()
    next_obs, reward, done, _, _ = env.step(action)
    # Print the shape of each element in the obs tuple
    for i, element in enumerate(obs):
        print(f"Shape of obs[{i}]: {np.shape(element)}")
    transition = (obs, action, reward, done, next_obs)  # Changed order here
    replay_buffer.append(transition)
    obs = next_obs
    if done:
        obs = env.reset()

obs = env.reset()

for step in itertools.count():
    epsilon = np.interp(step, [0, EPSILON_DECAY], [EPSILON_START, EPSILON_END])
    action = online_net.act(obs, epsilon)
    next_obs, reward, done, _, _ = env.step(action)
    # Print the shape of each element in the obs tuple
    for i, element in enumerate(obs):
        print(f"Shape of obs[{i}]: {np.shape(element)}")
    transition = (obs, action, reward, done, next_obs)  # Changed order here
    replay_buffer.append(transition)
    obs = next_obs
    episode_reward += reward
    if done:
        reward_buffer.append(episode_reward)
        obs = env.reset()
        episode_reward = 0.0

    if len(replay_buffer) >= BATCH_SIZE:
        transitions = random.sample(replay_buffer, BATCH_SIZE)
        
        for t in transitions[:10]:
            try:
                print(np.shape(np.asarray(t[0])))
            except ValueError:
                print("Cannot convert t[0] to a numpy array: ", t[0])
        desired_shape = (4,)
        # obses = np.asarray([t[0] for t in transitions])
        # obses = np.asarray([t[0].reshape(desired_shape) for t in transitions])
        obses = [np.asarray(t[0]).reshape(desired_shape) for t in transitions if np.asarray(t[0]).size == np.prod(desired_shape)]
        actions = np.asarray([t[1] for t in transitions])
        rews = np.asarray([t[2] for t in transitions])
        next_obses = np.asarray([t[4] for t in transitions])  # Changed index here
        dones = np.asarray([t[3] for t in transitions])  # Changed index here

        obses_t= torch.as_tensor(obses, dtype=torch.float32)
        actions_t= torch.as_tensor(actions, dtype=torch.int64).unsqueeze(-1)
        rews_t = torch.as_tensor(rews, dtype=torch.float32).unsqueeze(-1)
        next_obses_t = torch.as_tensor(next_obses, dtype=torch.float32)
        dones_t = torch.as_tensor(dones, dtype=torch.float32)

        target_q_values = target_net(next_obses_t)
        max_target_q_values, _ = torch.max(target_q_values, dim=1, keepdim=True)
        targets = rews_t + GAMMA * (1 - dones_t) * max_target_q_values

        online_q_values = online_net(obses_t)
        action_q_values = torch.gather(input=online_q_values, dim=1, index=actions_t)
        loss = nn.functional.smooth_l1_loss(action_q_values, targets)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if step % TARGET_UPDATE_FREQ == 0:
        target_net.load_state_dict(online_net.state_dict())

    if step % 1000 == 0:
        print('step:', step)
        print('avg rew', np.mean(reward_buffer))