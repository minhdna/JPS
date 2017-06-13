---
layout: default
title: Status
---
<iframe width="560" height="315" src="https://www.youtube.com/embed/1st-fbm4XwM" frameborder="0" allowfullscreen></iframe>

### Project Summary

The goal of JPS remains the same and it is to be able to continue solving progressingly intricate <br/>
jumping puzzles. Our base line project, which we have already achieved, is to solve a small 2D maze <br/>
(5x4) that is only solveable through jumping. That is, the AI may choose to walk through the maze <br/>
( if it leads to the optimal reward ) but it can never reach the destination block if it does not <br/>
utilize jumping. Our next milestone is to be able to solve a small maze with 2 floors (5x4x2). From <br/>
there on, we will continue to increase the size of the maze and add more floors. Our moonshot case <br/>
is for our agent to be able to solve a large maze with 3 floors (10x10x3). 

### Approach

We started off the base of our algorithm expecting our agent to navigate
through a map without using any jumping commands. We implemented a Q-learning
algorithm using the agent’s coordinates as states and [movenorth, movesouth, 
moveeast, movewest] as our action space with an epsilon-greedy exploration policy. Every
one step taken in any direction costs 1 point. If the agent dies, 100 points will
be deducted from the total reward. Reaching the goal awards the agent 100 points. 
After our Q-learning algorithm started to work properly, we took it a step further 
toward our goal by implementing a map, where the agent must perform at least 1 jump 
in order to reach the goal node. The update equation of the Q-learning algorithm: 

  Q(s<sub>t</sub>,a<sub>t</sub>) = Q(s<sub>t</sub>,a<sub>t</sub>) + a<sub>t</sub> * (r<sub>t+1</sub> + gamma * maxQ(s<sub>t+1</sub>,a) - Q(s<sub>t</sub>,a<sub>t</sub>))
 
We needed to expand our action list to include jumping 2 blocks in
order to get over gaps. This was when we faced our first challenge. When we 
started, we originally let the agent navigate around a simple puzzle without using
Discrete Movements. We realized that it is difficult (or even impossible) to
have our agent jump 2 blocks (to get over gaps) since Malmo does not allow 
discrete movements to move more than 1 block at a time. Therefore, we have to 
change our approach by implementing Absolute Movement. Teleportation allows us 
to easily implement how far we would want our agent to “jump”, or “walk” in 
order to tackle the challenging jumping puzzle. 

After creating an agent that will successfully converge on a simple map, we then created more 
complex maps for our agent to solve. This tested the convergence rate of our agent and allowed us 
to tweak the agent to perform better. We noticed the agent converged slowly for the simple puzzle
so we changed some parameters of our agent. We mainly focused on speeding up convergence 
speeds so we lowered the discount factor, gamma, from 1.0 to 0.8. We also decided to lower
epsilon to 0.01. We also changed the learning rate, alpha, to 0.2 from 0.3. We believe that
these changes have helped our agent find the optimal solution to the puzzle faster.


### Evaluation

To evaluate our learning agent, we keep track of 2 different values: the number of 
steps taken and the cumulative rewards. First, for the number of steps taken, we 
expect our agent to take a random number of steps (from 1 to 10) in the beginning. 
Later on, as the agent learns the map, it should plateau around 4 steps, which is the 
optimal amount of steps to reach the goal. 
<img src="https://puu.sh/w25BG/124e5bad71.jpg" height="260" width="380" alt="Steps Taken"> 
As you can see from our graph above, the number of steps taken at the beginning are small, 
but fluctuate between 1 and 7. This is different than other solving mazes, where it should be 
very large in the beginning. This is because the simple jumping puzzle that the agent runs
on have very limited amount of possible moves (where he can survive) in the beginning.
The graph also plateaued as expected around 4 moves, which means our agent is learning 
the jumping puzzle successfully.

Another evaluation we did on our learning agent is to assess the 
cumulative reward. For this evaluation, we expect the agent's reward to be extremely low (> -100) 
in the beginning, where it dies alot. Later on, we expect the cummulative reward to be consistently 
high (96 points) as the agent converges. 
<img src="https://puu.sh/w25Za/618b9e08f2.jpg" height="260" width="380" alt="Cumulative Reward"> 
As expected, the graph above shows that our agent is able to learn and navigate through the jumping 
puzzle. After dying a lot in the beginning, where it reaches really low negative rewards, the agent 
was able to learn to navigate correctly. Converging around 45th iteration, the graph flattens out at 
96 points, where the agent takes the optimal 4 steps to reach the destination. 

### Remaining Goals and Challenges

Currently, our agent is very limited in that it is only able to solve a very small, 
single-dimension maze that we generated ourselves. We hope to expand our agent so that 
it is able to solve multi-floor mazes. The bare-minimum in which we consider our agent 
a success is if it is able to solve a maze of 2 floors. Once it is able to solve a 2-level 
maze, we are confident it can learn to solve 3 or 4-level maze. 

The biggest challenge is for our agent to observe that the maze has 2 floors and make smart
decisions based off of that. We're currently using a Q-table to represent the X and Z 
of a single-level maze. One solution we're thinking about is to represent a multi-level maze in 
a larger Q-table, keeping track of the X, Y, and Z. That is a difficult task in itself so our backup
plan is to ignore the Y-value completely.
