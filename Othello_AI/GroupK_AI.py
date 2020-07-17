#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
COMS W4701 Artificial Intelligence - Programming Homework 2

An AI player for Othello. This is the template file that you need to  
complete and submit. 

@author: Aidan Friedsam, Seyi Oderinde, Pranav Guhathakurta
"""

import random
import sys
import time
import math

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):
    score = get_score(board)
    #returns tuple (# of dark disks, # of light disks)
    if color == 1:
      return score[0]-score[1]
    else:
      return score[1]-score[0]

############ MINIMAX ###############################

def minimax_min_node(board, color, DEPTH_LIMIT, depth):
    opp_color = 1 if color == 2 else 2  
    possible_moves = get_possible_moves(board, opp_color) 
    if depth >= DEPTH_LIMIT: 
      return compute_utility(board, color) # Or compute a different heuristic function 

    if not possible_moves: 
      return compute_utility(board, color)

    best_move = None
    best_score = math.inf
    for move in possible_moves: 
      new_board = play_move(board, opp_color, move[0], move[1])
      score = minimax_max_node(new_board, color, DEPTH_LIMIT, depth+1)
      if score < best_score: 
        best_move = move
        best_score = score
        if move == (7,7) or move == (0,0) or move == (7,0) or move == (0,7):
          best_score -= 2
        if move==(1,0) or move==(1,1) or move==(0,1) or move==(6,0) or move==(6,1) or move==(7,1) or move==(0,6) or move==(1,6) or move==(1,7) or move==(6,7) or move==(6,6) or move==(7,6):
          best_score -= 2
    return best_score 
      





def minimax_max_node(board, color, DEPTH_LIMIT, depth):

    possible_moves = get_possible_moves(board, color)
    if depth >= DEPTH_LIMIT: 
      return compute_utility(board, color) # Or compute a different heuristic function 

    if not possible_moves: 
      return compute_utility(board, color) 

    best_move = None
    best_score = -math.inf
    for move in possible_moves: 
      new_board = play_move(board, color, move[0], move[1])
      score = minimax_min_node(new_board, color, DEPTH_LIMIT, depth+1)
      if score > best_score: 
        best_move = move
        best_score = score
        if move == (7,7) or move == (0,0) or move == (7,0) or move == (0,7):
          best_score += 2
        if move==(1,0) or move==(1,1) or move==(0,1) or move==(6,0) or move==(6,1) or move==(7,1) or move==(0,6) or move==(1,6) or move==(1,7) or move==(6,7) or move==(6,6) or move==(7,6):
          best_score += 2

    return best_score 




    
def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """
    #move = tuple --> (COLUMN, ROW)
    #play_move(board, color, move)

    DEPTH_LIMIT = 3

    possible_moves = get_possible_moves(board, color) 

    best_move = None
    best_score = -math.inf
    for move in possible_moves: 
      new_board = play_move(board, color, move[0], move[1])
      score = minimax_min_node(new_board, color, DEPTH_LIMIT, 0)
      if score > best_score: 
        best_move = move
        best_score = score

    return best_move 



    
############ ALPHA-BETA PRUNING #####################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, beta): 
    return None


#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, alpha, beta):
    return None


def select_move_alphabeta(board, color): 
    return 0,0 


####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Minimax AI") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            movei, movej = select_move_minimax(board, color)
            #movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()
