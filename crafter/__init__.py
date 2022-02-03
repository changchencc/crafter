from .env import Env
from .recorder import Recorder

try:
    import gym

    gym.register(
        id="CrafterReward-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True},
    )
    gym.register(
        id="CrafterNoReward-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": False},
    )
    gym.register(
        id="CrafterReward-l0-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True, "level": 0},
    )
    gym.register(
        id="CrafterNoReward-l0-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": False, "level": 0},
    )
    gym.register(
        id="CrafterReward-l1-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True, "level": 1},
    )
    gym.register(
        id="CrafterNoReward-l1-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": False, "level": 1},
    )
    gym.register(
        id="CrafterReward-l2-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True, "level": 2},
    )
    gym.register(
        id="CrafterNoReward-l2-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": False, "level": 2},
    )
    gym.register(
        id="CrafterReward-l3-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True, "level": 3},
    )
    gym.register(
        id="CrafterNoReward-l3-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": False, "level": 3},
    )
    gym.register(
        id="CrafterReward-l4-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True, "level": 4},
    )
    gym.register(
        id="CrafterNoReward-l4-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": False, "level": 4},
    )
    gym.register(
        id="CrafterReward-l5-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True, "level": 5},
    )
    gym.register(
        id="CrafterNoReward-l5-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": False, "level": 5},
    )
    gym.register(
        id="CrafterReward-l6-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True, "level": 7},
    )
    gym.register(
        id="CrafterReward-l8-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True, "level": 8},
    )
    gym.register(
        id="CrafterReward-l9-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True, "level": 9},
    )
    gym.register(
        id="CrafterReward-l10-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True, "level": 10},
    )
    gym.register(
        id="CrafterReward-l11-v1",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True, "level": 11},
    )
except ImportError:
    pass
