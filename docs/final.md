---
layout: default
title: Final Report
---

## Video

## Project Summary

The concept of a jumping puzzle has been around for decades. Think of a regular maze, where you have a <br/>
start point and must reach the end point through a series of up, down, left, right actions. Now add holes <br/>
in this maze along with a jumping action to the action space and you have a jumping puzzle. <br/>

<img src="http://s3.vidimg.popscreen.com/original/2/ZHZuS0tvOEIxLWsx_o_funny-minecraft-jump.jpg" height="260" width="380">

The ability for a character to jump is a key mechanism in many successful games. Jumping puzzles takes <br/>
this mechanism to a whole new level in which the player’s knowledge of where to jump and when to jump <br/>
can decide whether they pass the level or not. Games like Guild Wars and Assassin’s creed implement this <br/>
feature to some extent while games like Super Mario are a giant jumping puzzle in itself. A jumping puzzle <br/>
AI would allow game developers to test whether a jumping puzzle is able to be completed/whether it is too <br/>
easy or hard. The field of robotics is fairly new but that doesn’t stop researchers from having visions <br/>
of robots saving people from catastrophes or fighting in wars in place of humans. Like Minecraft, the real <br/>
world is not just flat lands. If a robot is going to perform those functions, it will need to be able to, <br/>
not only walk, but to learn to climb and maybe even jump! <br/>

<img src="http://i.imgur.com/djUfPkH.jpg" height="260" width="380">

In our project, we give our agent, JPS, progressingly intricate jumping puzzles to solve. What separates a <br/>
jumping puzzle from a regular maze is that it is only solveable by jumping. That is, JPS may choose to walk <br/>
through the maze (if it leads to the optimal reward) but it can never reach the destination block if it does <br/>
not utilize jumping. <br/>

<img src="http://i42.tinypic.com/2a4tipu.png" height="260" width="380">

Sounds simple enough right? Wrong. There are many complex attributes to a jumping puzzle. Jumping across a <br/>
single-block hole is easy but what happens when the hole is 2-blocks large? Increasing the size of the maze is trivial <br/>
(we deal with x and z coordinates) but how does the complexity scale when we add multiple layers to the maze (now <br/>
we're dealing with x, z, AND y). How would the agent even know to jump to the floor above it? Stay tuned and <br/>
JPS will help unearth the answers to some of these questions! <br/>

<img src="http://i61.servimg.com/u/f61/15/81/88/32/jump_210.png" height="260" width="380">



## Approaches

Once we got our project working, we tested it on a simple 5x4x1 dimension maze. The dimensions of this maze <br/>
means that there is a 5 by 4 square of height one. This map and our agent's performance on this map is determined <br/>
our baseline performance. The next step to increase the complexity was to create more complex maps. From here we <br/>
generated maps with dimension 5x4x2 with the goal of the maze in the level above the start. This would require our <br/>
agent to jump vertically, in addition to jumping horizontally. <br/>

To do this we needed to introduce a Y-axis to our agent. We modified the agent's action state so that our agent will <br/>
jump in the vertical Y-axis. The tabular Q agent now also accepts a vertical component into its world state and can <br/>
progress vertically through a puzzle. To implement this into discreteMovementCommands() get our current position: <br/>
   
   obs = json.loads(world_state.observations[-1].text)
   
We then look at our current state and choose the optimal policy. <br/>

   total_reward += self.act(world_state, agent_host, current_r)

Once our agent is able to traverse puzzles of height 2, height becomes trivial and in theory, the agent should be able <br/>
to solve puzzles of any height. From here is it a matter of creating more mazes for agent to run through and seeing how <br/>
it performs. <br/>
    
## Evaluation

## References

### Images
- https://www.technologyuk.net/computer-gaming/gaming-landmarks/images/gaming_landmarks_0094.gif
- http://www.gamersdecide.com/sites/default/files/authors/u14586/4.jpg
- https://cdn3.vox-cdn.com/uploads/chorus_asset/file/6276971/mad-preview-still-06.0.jpg
- http://static.mnium.org/images/contenu/unes/big/gw2_jumping_puzzle_05.jpg
- http://s3.vidimg.popscreen.com/original/2/ZHZuS0tvOEIxLWsx_o_funny-minecraft-jump.jpg
- http://i42.tinypic.com/2a4tipu.png
- http://i61.servimg.com/u/f61/15/81/88/32/jump_210.png

