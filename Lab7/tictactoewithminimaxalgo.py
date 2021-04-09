class my_class(object):
    pass
import os
import platform 
from os import system 
from random import choice 
from math import inf as infinity 

movenum=0
manush = -1 #max
ai = +1 #min
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]



def clean():
    #console clean kori, notun shikha jinish
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')






def render(state,com,human):
    #protibar board ta print kora
     chars = {
         -1 : human,
         +1 : com,
          0 : ' '
         }
     bline = '---------------'

     print('\n'+bline)

     for row in state:
         for cell in row:
             symbol=chars[cell]
             print(f'| {symbol} |', end='')

         print('\n'+bline)



def empty_cells(state):
    #current board nicche state a
    #cells list a shob empty cell gula jabe
    cells=[]

    for x,row in enumerate(state):
        for y,cell in enumerate(row):
            if cell==0:
                cells.appned([x,y])

        return cells



def valid_move(x,y):
    #manusher vorosha nai, ekbar chal diye abr override korte chaite pare, override korle to r game hoilo na
    #tai ei jaigay ami override korte dibo na, space khali ache naki oi  validity check korbo
    if [x,y] in empty_cells(board):
        return True
    else:
        return False



def set_move(x,y,player):
    #move deyar jaiga valid hoile tokhon e se dite parbe move
    if valid_move(x,y):
        board[x][y]=player
        return True
    else:
        return False




def ai_khelbe(com,human):
    #minimax chalabe jodi steps <9

    depth = len(empty_cells(board))
    if depth == 0 or game_sesh(board):
        return depth
    print(f'computer khelche [{com}]')
    render(board,com,human)

    if depth == 9 :
        x= choice ([0,1,2])
        y= choice ([0,1,2])

    else:
        move = minimax(board,depth,ai)
        x,y=move[0],move[1]

    set_move(x,y,ai)
    time.sleep(.300)



def human_khelbe(com,human):
    depth=len(empty_cells(board))

    if depth == 0 or game_sesh(board):
        return #break kore dicchi
    move = -1
    #dict for valid moves 
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

    print(f'Human khelbe [{human}]')
    render(state,com,human)

    while move<1 or move>9 :
        try:
            move = int(input('Use the number pad for choosing where you want to put '))
            coord= moves[move]
            can_move= set_move(coord[0], coord[1], manush)

            if not can_move:
                print('Bad move! ')
                move=-1

            else:
                movenum=move+movenum

        except(EOFError,KeyboardInterrupt):
            print('Sorry and Bye!')
        except(KeyError, ValueError):
            print('Bad human! Allahafez')





def wins(state,player):

    #katakati khelay jitbe kivhabe sei parameter eita
    #mane cloumn, row, diagonal a mile gele jite gese oi shob state gula eikhane store ase
    win_state= [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
        ]
    #tana tinbar millei to jitbe
    if [player,player,player] in win_state:
        return True
    else:
        return False


def game_sesh(state):
    #current board er obtha check kore and dekhbe khela sesh naki
    return wins(state,manush) or wins(state,ai)



def evalute(state):
    if wins(state,ai):
        score=+1 #computer jitse
    elif wins(state,manush):
        score =-1
    else:
        score = 0 #keu jite nai mane draw 

    return score 




def minimax(state,depth,player):
    #best move choose korbe ai er jonno
    
    if player == ai :
        best = [-1,-1,-infinity]

    else:
        best = [-1,-1,+infinity]

    if depth == 0 and gave_sesh(state):
        score=evaluate(state)
        return [-1,-1,score]

    for cell in empty_cells(state):
        x,y= cell[0],cell[1]
        state[x][y]=player
        score = minimax(state,depth-1,player)
        state[x][y]=0
        score[0],score[y]=x,y


    if player==ai:
        if score[2] > best[2] :
            best=score #max value

    else:
        if score[2] < best[2]:
            best=score #min value

    return best



def main():
    clean()
    human='' # human er choice X or O
    com = '' # computer er choice 
    first='' # jodi human prothom hoy

    #input nicchi khelar jonno, sathe error o handle kortesi ;)
    while human != 'O' and human !='X':
        try:
            print('')
            human= input('Choose X OR O\nChoosen: ').upper()

        except (EOFError, KeyboardInterrupt):
            print('Sorry and Bye!')

        except (KeyError, ValueError):
            print('Bad human! Allahafez :(')

   #choice set kori 
    if human =='X':
        com = 'O'
    else :
        com='X'

    #ke age start korbe 
    while first !='Y' and first != 'N':
        try:
            first= input('Start First ? Y/N : ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Sorry and Bye! ')
        except (KeyError, ValueError):
            print('Bad human! Allahafez :(')

        #ebar game start kori
        while len(empty_cellls(board)) > 0 and not game_sesh(board):
            if first == 'N' :
                ai_khelbe(com,human)
                first=''

            human_khelbe(com,human)
            ai_khelbe(com,human)

        #khela sesher dike 
        if wins(board,manush):
            print(f'Human turn [{human}]')
            render(board, com,human)
            print('Aww Congo!! you win')
            finalscore=evalute(state) -movenum 
            print('Your score is ',finalscore)


        elif wins(board,ai):
            print(f'Computer turn [{com}]')
            render(board,com, human)
            print("You lose! shomossha nai Try again! Don't give up! ") 
            finalscore=evalute(state) -movenum
            print('Your score is ',finalscore)

        else:
            render(board,com,human)
            finalscore=evalute(state) -movenum
            print('Your score is ',finalscore)
            print("Draw!") 

        exit()




if __name__=='__main__':
    main()





