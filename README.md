# Programming AlphaGo Zero algorithm for Tic-Tac-Toe

Primary reference used: [AppliedDataSciencePartners's github repo](https://github.com/AppliedDataSciencePartners/DeepReinforcementLearning). Used most of their functions, so they deserve due credits for this code. My main contributions are:
- Reimplementing `game.py` for tic-tac-toe. It's mostly implementing the physics of the tic-tac-toe world. Additionally minor modifications to `agents.py` and `config.py`.
- Introducting my own CNN architecture
- Tuning the various hyperparameters for better training

## Usage

See `run-tictactoe.ipynb` to see the overall flow of the code, how the training process works and how it performs against itself and against a random agent.

## Introduction

This is an RLagent that plays the game tic-tac-toe using the same algorithm as [AlphaGo Zero](https://deepmind.com/blog/alphago-zero-learning-scratch/). It's wins 986-14 in a 1000 game match against an agent who choose her moves randomly. The results are not good yet, will work on improving them in future. 

Approaches tried:
- Using `TD(lambda)` rule and various montecarlo simulated episodes to train for the value function for each state. Started using my `TD(lambda)` [implementation](https://github.com/psurya1994/algorithmsFromScratch/blob/master/ImplementingTD1Rule.ipynb) from the scratch. But it was computationally very inefficient and had to give up on the approach.
- I started implementing it on my own from scratch using the references: [AlphaGo Zero cheatsheet](https://medium.com/applied-data-science/alphago-zero-explained-in-one-diagram-365f5abf67e0) and the [original paper](https://www.nature.com/articles/nature24270.epdf). But it was taking a lot more time than I initially estimated (because of the MCTS step). So did not go ahead.
- Adopted those parts directly from a [repo on github](https://github.com/AppliedDataSciencePartners/DeepReinforcementLearning) that already implemented it. **This is the present implementation.**

## Background

I made a [public commitment](https://www.facebook.com/psurya1994/posts/10216832807642140) about in mid-July that I will build a reinforcement learning agent that can play the game Tic-Tac-Toe before my birthday. So today, August 21st (one day before my birthday), I'm ready to show the world the results of the RLagent. I'm also making the code public. It likely still has bugs and optimizations, which I'll be working on in future.

## Results

Here's an example of the algorithm playing against itself. `X -> ReinforcementLearningAgent, O -> ReinforcementLearningAgent`

```
step:  0
['X', '-', '-']
['-', '-', '-']
['-', '-', '-']
step:  1
['X', '-', '-']
['-', 'O', '-']
['-', '-', '-']
step:  2
['X', '-', '-']
['-', 'O', '-']
['X', '-', '-']
step:  3
['X', '-', '-']
['O', 'O', '-']
['X', '-', '-']
step:  4
['X', '-', '-']
['O', 'O', 'X']
['X', '-', '-']
step:  5
['X', 'O', '-']
['O', 'O', 'X']
['X', '-', '-']
step:  6
['X', 'O', '-']
['O', 'O', 'X']
['X', 'X', '-']
step:  7
['X', 'O', '-']
['O', 'O', 'X']
['X', 'X', 'O']
step:  8
['X', 'O', 'X']
['O', 'O', 'X']
['X', 'X', 'O']
=== game ended
```

Here's an example of the RL agent playing against an algorithm that randomly chooses it's actions. In a 1000 game simulation, it performed 986-14. Since this is an easy game, that's a bad score. It has to win everytime, need to optimize the code more to get such results. Also, as shown below, it's not playing the optimal moves. 

Example 1: `X -> ReinforcementLearningAgent, O -> RandomActionAgent`
```
step:  0
['X', '-', '-']
['-', '-', '-']
['-', '-', '-']
step:  1
['X', 'O', '-']
['-', '-', '-']
['-', '-', '-']
step:  2
['X', 'O', '-']
['-', 'X', '-']
['-', '-', '-']
step:  3
['X', 'O', '-']
['-', 'X', 'O']
['-', '-', '-']
step:  4
['X', 'O', 'X']
['-', 'X', 'O']
['-', '-', '-']
step:  5
['X', 'O', 'X']
['-', 'X', 'O']
['-', '-', 'O']
step:  6
['X', 'O', 'X']
['-', 'X', 'O']
['X', '-', 'O']
```
