import robel
import gym

if __name__ == "__main__":
    env = gym.make("DKittyStandFixed-v0") # basic task
    # env = gym.make('DKittyWalkFixed-v0') # advance task
    # env = gym.make("DKittyWalkRandomDynamics-v0") # bonus task
    obs = env.reset()
    done = False
    episodes = 10

    for i in range(episodes):
        while not done:
            env.render()
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            print(info['score/success'])  # the flag indicates whether it's successful or not
