#### SELF PLAY
EPISODES = 20
MCTS_SIMS = 30	
MEMORY_SIZE = 1000
TURNS_UNTIL_TAU0 = 10 # turn on which it starts playing deterministically
CPUCT = 1
EPSILON = 0.2
ALPHA = 0.8


#### RETRAINING
BATCH_SIZE = 128
EPOCHS = 3
REG_CONST = 0.0001
LEARNING_RATE = 0.01 # from 0.1
MOMENTUM = 0.9 # from 0.9
TRAINING_LOOPS = 10

# HIDDEN_CNN_LAYERS = [
# 	{'filters':75, 'kernel_size': (4,4)}
# 	 , {'filters':75, 'kernel_size': (4,4)}
# 	 , {'filters':75, 'kernel_size': (4,4)}
# 	 , {'filters':75, 'kernel_size': (4,4)}
# 	 , {'filters':75, 'kernel_size': (4,4)}
# 	 , {'filters':75, 'kernel_size': (4,4)}
# 	]

HIDDEN_CNN_LAYERS = [
	{'filters':10, 'kernel_size': (2,2)},
	{'filters':10, 'kernel_size': (2,2)}
	 # , {'filters':75, 'kernel_size': (4,4)}
	 # , {'filters':75, 'kernel_size': (4,4)}
	 # , {'filters':75, 'kernel_size': (4,4)}
	 # , {'filters':75, 'kernel_size': (4,4)}
	 # , {'filters':75, 'kernel_size': (4,4)}
	]

#### EVALUATION
EVAL_EPISODES = 20
SCORING_THRESHOLD = 1.3
