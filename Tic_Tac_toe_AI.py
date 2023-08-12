# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:50:27 2023

@author: gnana
"""
""" board :   0   =    _
              -1   =    x
              1  =    O
"""
def minmax(board, player):
    y = analyze_board(board)
    if y != 0:
        return y * player

    position = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = player
            score = -minmax(board, player * -1) # returns 1 for the player who is winning
            board[i] = 0
            if score > value:
                value = score
                position = i

    if position == -1:
        return 0
    return value


def analyze_board(board):
    dp = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in range(0, 8):
        if board[dp[i][0]] != 0 and board[dp[i][0]] == board[dp[i][1]] == board[dp[i][2]]:
            return board[dp[i][0]]
    return 0


def computer_turn(L):
    position = -1
    value = -2
    for i in range(0, 9):
        if L[i] == 0:
            L[i] = 1
            score = -minmax(L, -1)
            L[i] = 0
            if score > value:
                value = score
                position = i
    L[position] = 1


def show_board(l):
    print("Current state of the board: \n\n")
    for i in range(0, 9):
        if i > 0 and i % 3 == 0:
            print("\n")
        if l[i] == 0:
            print("_", end=" ")
        if l[i] == -1:
            print("X", end=" ")
        if l[i] == 1:
            print("O", end=" ")
    print("\n\n")


def user1_turn(l):
    position = int(input("Enter a valid position of X from 1 to 9: "))
    if l[position - 1] != 0:
        print("Invalid move \n\n")
        return user1_turn(l)
    l[position - 1] = -1


def user2_turn(l):
    position = int(input("Enter a valid position of O from 1 to 9: "))
    if l[position - 1] != 0:
        print("Invalid move")
        
    l[position - 1] = 1


def main():
    
    choice = int(input("If you want to have chances of winning, enter 2. If you are desperate to lose, enter 1: \n"))
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if choice == 1:
        print("Computer: O Vs. You: X \n")
        player = int(input("Play 1st or 2nd:\n "))
        for i in range(0, 9):
            if analyze_board(board) != 0:
                break
            if (i + player) % 2 == 0:
                computer_turn(board)
            else:
                show_board(board)
                user1_turn(board)
    else:
        for i in range(0, 9):
            if analyze_board(board) != 0:
                break
            if i % 2 == 0:
                show_board(board)
                user1_turn(board)
            else:
                show_board(board)
                user2_turn(board)

    x = analyze_board(board)
    if x == 0:
        show_board(board)
        print("Draw!")
    elif x == -1:
        show_board(board)
        print("Player X wins! Player O loses!")
    elif x == 1:
        show_board(board)
        print("Player O wins! Player X loses!")

print("convention: \n")
print("1 2 3")
print("4 5 6")
print("7 8 9 \n\n")
main()   