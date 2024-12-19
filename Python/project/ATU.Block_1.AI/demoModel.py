import gym
import time
from stable_baselines3 import A2C, PPO

env = gym.make("ALE/SpaceInvaders-v5")
env.reset()

model_path = "/home/derry/atu/master/block1/ai/DRL-space-invader-assignment/PPO_900000.zip"
model = A2C.load(model_path, env=env)

episodes = 5

for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        time.sleep(0.01)
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        env.render()
