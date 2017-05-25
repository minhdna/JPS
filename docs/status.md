---
layout: default
title: Status
---

### Project Summary

The goal of JPS remains the same and it is to be able to continue solving <br />
progressingly intricate jumping puzzles. Our base line project, which we <br />
have already achieved, is to solve a small 2D maze (5x4) that is only solveable <br />
through jumping. That is, the AI may choose to walk through the maze <br />
(if it leads to the optimal reward) but it can never reach the destination <br />
block if it does not utilize jumping. Our next milestone is to be able to solve <br />
a small maze with 2 floors (5x4x2). From there on, we will continue to increase <br />
the size of the maze and add more floors. Our moonshot case is for our agent to <br />
be able to solve a large maze with 3 floors (10x10x3). 

### Approach

We started off the base of our algorithm expecting our agent to navigating <br />
through a map without using any jumping commands. We implemented a Q-learning <br />
algorithm using the agent’s coordinates as states and [movenorth, movesouth, <br />
moveeast, movewest] as our actions space. Every one step taken in any direction <br />
costs 1 point. If the agent dies, 100 points will be deducted from the total <br />
reward. Reaching the goal awards the agent 100 points. After our Q-learning <br />
algorithm started to work properly, we take it a step further toward our goal <br />
by implementing a map, where the agent must perform at least 1 jump in order to <br />
reach the goal node. 
 
We needed to expand our action list to include jumping 2 blocks actions (in <br />
order to get over gaps. This was when we face our first challenge. When we <br />
started, we originally let the agent navigate around a simple puzzle with using <br />
Discrete Movements. We realized that it is difficult (or even impossible) to <br />
have our agent jump 2 blocks (to get over gaps) since Malmo does not allow <br />
discrete movement to move more than 1 block at a time. Therefore, we have to <br />
change our approach by implementing Absolute Movement. Teleportation allows us <br />
to easily implement how far we would want our agent to “jump”, or “walk” in <br />
order to navigate the challenging jump puzzle. 


### Evaluation

### Remaining Goals and Challenges

Currently, our agent is very limited in that it is only able to solve a very small, <br />
single-dimension maze that we generated ourselves. We hope to expand our agent so that <br />
it is able to solve multi-floor mazes. The bare-minimum in which we consider our agent <br />
a success is if it is able to solve a maze of 2 floors. Once it is able to solve a 2-level <br />
maze, we are confident it can learn to solve 3 or 4-level maze. <br />

The biggest challenge is for our agent to observe that the maze has 2 floors and make smart <br />
decisions based off of that. We're currently using one Q-table to represent the reward states <br />
of a single-level maze. One solution we're thinking about is using multiple Q-tables to <br />
represent multiple floors. That is a difficult task in itself so our backup plan is to <br />
ignore the Y-value completely.
