
import MalmoPython
import os
import json
import logging
import math
import sys
import time
import random

class TabQAgent:
    """Reinforcement learning agent for discrete state/action spaces."""
    def __init__(self, alpha=0.2, gamma=0.8, n=0.9):
        """Constructing an RL agent.
                Args
                    alpha:  <float>  learning rate      (default = 0.3)
                    gamma:  <float>  value decay rate   (default = 1)
                    n:      <int>    number of back steps to update (default = 1)
                """
        self.epsilon = 0.01 # chance of taking a random action instead of the best
        self.actions = ["movenorth 1", "movesouth 1", "movewest 1", "moveeast 1", ]
        self.q_table = {}
        self.n, self.gamma, self.alpha = n, alpha, gamma

    def act(self, world_state, agent_host, current_r):
        """take 1 action in response to the current world state"""

        obs_text = world_state.observations[-1].text
        obs = json.loads(obs_text)  # most recent observation
        if not u'XPos' in obs or not u'ZPos' in obs:
            return 0
        current_s = "%d:%d" % (int(obs[u'XPos']), int(obs[u'ZPos']))
        if not self.q_table.has_key(current_s):
            self.q_table[current_s] = ([0] * len(self.actions))

        # update Q values
        if self.prev_s is not None and self.prev_a is not None:
            old_q = self.q_table[self.prev_s][self.prev_a]
            self.q_table[self.prev_s][self.prev_a] = old_q + self.alpha * (current_r
                                                                           + self.gamma * max(
                self.q_table[current_s]) - old_q)

        # select the next action
        rnd = random.random()
        if rnd < self.epsilon:
            a = random.randint(0, len(self.actions) - 1)
        else:
            m = max(self.q_table[current_s])
            l = list()
            for x in range(0, len(self.actions)):
                if self.q_table[current_s][x] == m:
                    l.append(x)
            y = random.randint(0, len(l) - 1)
            a = l[y]

        # send the selected action
        agent_host.sendCommand(self.actions[a])
        self.prev_s = current_s
        self.prev_a = a

        return current_r

    def run(self, agent_host):
        """run the agent on the world"""

        total_reward = 0
        current_r = 0
        tol = 0.01

        self.prev_s = None
        self.prev_a = None

        # wait for a valid observation
        world_state = agent_host.peekWorldState()
        while world_state.is_mission_running and all(e.text == '{}' for e in world_state.observations):
            world_state = agent_host.peekWorldState()
        # wait for a frame to arrive after that
        num_frames_seen = world_state.number_of_video_frames_since_last_state
        while world_state.is_mission_running and world_state.number_of_video_frames_since_last_state == num_frames_seen:
            world_state = agent_host.peekWorldState()
        world_state = agent_host.getWorldState()
        for err in world_state.errors:
            print err

        if not world_state.is_mission_running:
            return 0  # mission already ended

        assert len(world_state.video_frames) > 0, 'No video frames!?'

        obs = json.loads(world_state.observations[-1].text)
        prev_x = obs[u'XPos']
        prev_z = obs[u'ZPos']
        print 'Initial position:', prev_x, ',', prev_z

        # take first action
        total_reward += self.act(world_state, agent_host, current_r)

        require_move = True
        check_expected_position = True

        # main loop:
        while world_state.is_mission_running:

            # wait for the position to have changed and a reward received
            print 'Waiting for data...',
            while True:
                world_state = agent_host.peekWorldState()
                if not world_state.is_mission_running:
                    print 'mission ended.'
                    break
                if len(world_state.rewards) > 0 and not all(e.text == '{}' for e in world_state.observations):
                    obs = json.loads(world_state.observations[-1].text)
                    curr_x = obs[u'XPos']
                    curr_z = obs[u'ZPos']
                    if require_move:
                        if math.hypot(curr_x - prev_x, curr_z - prev_z) > tol:
                            print 'received.'
                            break
                    else:
                        print 'received.'
                        break
            # wait for a frame to arrive after that
            num_frames_seen = world_state.number_of_video_frames_since_last_state
            while world_state.is_mission_running and world_state.number_of_video_frames_since_last_state == num_frames_seen:
                world_state = agent_host.peekWorldState()

            num_frames_before_get = len(world_state.video_frames)

            world_state = agent_host.getWorldState()
            for err in world_state.errors:
                print err
            current_r = sum(r.getValue() for r in world_state.rewards)

            if world_state.is_mission_running:
                assert len(world_state.video_frames) > 0, 'No video frames!?'
                num_frames_after_get = len(world_state.video_frames)
                assert num_frames_after_get >= num_frames_before_get, 'Fewer frames after getWorldState!?'
                frame = world_state.video_frames[-1]
                obs = json.loads(world_state.observations[-1].text)
                curr_x = obs[u'XPos']
                curr_z = obs[u'ZPos']
                print 'New position from observation:', curr_x, ',', curr_z, 'after action:', self.actions[
                    self.prev_a],  # NSWE
                if check_expected_position:
                    expected_x = prev_x + [0, 0, -1, 1][self.prev_a]
                    expected_z = prev_z + [-1, 1, 0, 0][self.prev_a]
                    if math.hypot(curr_x - expected_x, curr_z - expected_z) > tol:
                        print ' - ERROR DETECTED! Expected:', expected_x, ',', expected_z
                        raw_input("Press Enter to continue...")
                    else:
                        print 'as expected.'
                    curr_x_from_render = frame.xPos
                    curr_z_from_render = frame.zPos
                    print 'New position from render:', curr_x_from_render, ',', curr_z_from_render, 'after action:', \
                    self.actions[self.prev_a],  # NSWE
                    if math.hypot(curr_x_from_render - expected_x, curr_z_from_render - expected_z) > tol:
                        print ' - ERROR DETECTED! Expected:', expected_x, ',', expected_z
                        raw_input("Press Enter to continue...")
                    else:
                        print 'as expected.'
                else:
                    print
                prev_x = curr_x
                prev_z = curr_z
                # act
                total_reward += self.act(world_state, agent_host, current_r)

        # process final reward
        total_reward += current_r

        # update Q values
        if self.prev_s is not None and self.prev_a is not None:
            old_q = self.q_table[self.prev_s][self.prev_a]
            self.q_table[self.prev_s][self.prev_a] = old_q + self.alpha * (current_r - old_q)

        return total_reward




sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

# More interesting generator string: "3;"

# -- set up the mission -- #
agent_host = MalmoPython.AgentHost()

# add some args
agent_host.addOptionalStringArgument('mission_file',
    'Path/to/file from which to load the mission.', './mazes/maze_simple.xml')
agent_host.addOptionalFloatArgument('alpha',
    'Learning rate of the Q-learning agent.', 0.1)
agent_host.addOptionalFloatArgument('epsilon',
    'Exploration rate of the Q-learning agent.', 0.01)
agent_host.addOptionalFloatArgument('gamma', 'Discount factor.', 1.0)
agent_host.addOptionalFlag('load_model', 'Load initial model from model_file.')
agent_host.addOptionalStringArgument('model_file', 'Path to the initial model file', '')
agent_host.addOptionalFlag('debug', 'Turn on debugging.')

try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print 'ERROR:',e
    print agent_host.getUsage()
    exit(1)
if agent_host.receivedArgument("help"):
    print agent_host.getUsage()
    exit(0)

num_maps = 1

for imap in xrange(num_maps):
    # -- set up the agent -- #
    action_set = []

    agent = TabQAgent(
        alpha=agent_host.getFloatArgument('alpha'),
        gamma=agent_host.getFloatArgument('gamma'),
        n = imap
        )

    # -- set up the mission -- #
    mission_file = agent_host.getStringArgument('mission_file')
    with open(mission_file, 'r') as f:
        print "Loading mission from %s" % mission_file
        mission_xml = f.read()
        my_mission = MalmoPython.MissionSpec(mission_xml, True)
    my_mission.removeAllCommandHandlers()
    my_mission.allowAllDiscreteMovementCommands()
    my_mission.requestVideo(320, 240)
    my_mission.setViewpoint(1)

    my_clients = MalmoPython.ClientPool()
    my_clients.add(MalmoPython.ClientInfo('127.0.0.1', 10000))  # add Minecraft machines here as available

    max_retries = 3
    agentID = 0
    expID = 'tabular_q_learning'

    num_repeats = 150
    cumulative_rewards = []
    for i in range(num_repeats):

        print "\nMap %d - Mission %d of %d:" % (imap, i + 1, num_repeats)

        my_mission_record = MalmoPython.MissionRecordSpec("./save_%s-map%d-rep%d.tgz" % (expID, imap, i))
        my_mission_record.recordCommands()
        my_mission_record.recordMP4(20, 400000)
        my_mission_record.recordRewards()
        my_mission_record.recordObservations()

        for retry in range(max_retries):
            try:
                agent_host.startMission(my_mission, my_clients, my_mission_record, agentID, "%s-%d" % (expID, i))
                break
            except RuntimeError as e:
                if retry == max_retries - 1:
                    print "Error starting mission:", e
                    exit(1)
                else:
                    time.sleep(2.5)

        print "Waiting for the mission to start",
        world_state = agent_host.getWorldState()
        while not world_state.has_mission_begun:
            sys.stdout.write(".")
            time.sleep(0.1)
            world_state = agent_host.getWorldState()
            for error in world_state.errors:
                print "Error:", error.text
        print

        # -- run the agent in the world -- #
        cumulative_reward = agent.run(agent_host)
        print 'Cumulative reward: %d' % cumulative_reward
        cumulative_rewards += [cumulative_reward]

        # -- clean up -- #
        time.sleep(0.5)  # (let the Mod reset)

    print "Done."

    print
    print "Cumulative rewards for all %d runs:" % num_repeats
    print cumulative_rewards
