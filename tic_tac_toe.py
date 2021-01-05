import sys


def format_board(board):
	bar = '----------------'
	cells = [str(i) if c =='.' else c for i,c in enumerate(board,start = 1)]
	cells_temp =' | {} | {} | {} | '
	f = '\n'.join([bar, 
				   cells_temp.format(*cells[:3]), 
			       bar,
			       cells_temp.format(*cells[3:6]), 
			       bar,
			       cells_temp.format(*cells[6:]),
			       bar])
	print(f)


def find_win(board):
	wins = [
			[0,1,2],[3,4,5],[6,7,8],
		    [0,3,6],[1,4,7],[2,5,8],
		    [0,4,8],[2,4,6]
		    ]
	for player in ['X','O']:
		for i,j,k in wins:
			combo = [board[i],board[j],board[k]]
			if combo == [player,player,player]:
				return player

def game_round(player:str,board:str):
	board = list(board)
	format_board(board)
	choice = input(f'Player {player} choose a cell (1-9/press q to quit): ')
	if choice == 'q' or choice == 'Q':
		sys.exit()
	if int(choice) not in range(1,10):
		print('It\'s not even on the board')
		game_round(player,board)
	if board[int(choice) - 1] == '.':
		board[int(choice) - 1] = player
	else:
		print('This cell is already taken!')
		game_round(player,board)
	return ''.join(board)
		
def main():
	print('WELCOME TO MY TIC TAC TOE GAME \n')
	board = 9* '.'
	winner = None
	turn = 1
	while not winner:
		print(f'INFO Turn {turn}')
		board = game_round('X',board)
		winner = find_win(board)
		if winner:
			print('X won!')
			format_board(board)
			break
		board = game_round('O',board)
		winner = find_win(board)
		if winner:
			print('O won!')
			format_board(board)
			break
		turn += 1
		

if __name__=='__main__':
	main()
