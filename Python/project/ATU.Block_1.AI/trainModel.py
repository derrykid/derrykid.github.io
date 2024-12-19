import gym
from stable_baselines3 import A2C, PPO

env = gym.make("ALE/SpaceInvaders-v5")
env.reset()



model = A2C('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=100)

episodes = 200

for e in range(episodes):
    observation = env.reset()
    done = False

    while not done:
        env.render()
        obs, reward, done, info = env.step(env.action_space.sample())

env.close()
