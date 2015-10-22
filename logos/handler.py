from tabulate import tabulate
import os
import sys

CURRENT_DIR = os.getcwd()
PADDING = 40

def set_teams():
	os.chdir(CURRENT_DIR + os.sep + 'teams')
	files = [f for f in os.listdir('.') if f[0] != '.']
	teams = [team[:-4] for team in files]
	os.chdir(CURRENT_DIR)
	return teams

def get_done():
	teams = set_teams()
	matches = []

	i = 0
	while i != len(teams):
		j = 0
		while j != len(teams):
			if teams[i] != teams[j]:
				matches.append((teams[i], teams[j]))
			j += 1
		i += 1

	whole_space = [a + '_' + b + '.png' for a, b in matches]

	os.chdir(CURRENT_DIR + os.sep + 'combined' + os.sep + 'loser')
	loser_files = [f for f in os.listdir('.') if f[0] != '.']
	os.chdir(CURRENT_DIR)

	os.chdir(CURRENT_DIR + os.sep + 'combined' + os.sep + 'tie')
	tie_files = [f for f in os.listdir('.') if f[0] != '.']
	os.chdir(CURRENT_DIR)

	table = [[team] + [0 for _ in range(len(teams))] for team in teams]
	headers = [""] + [_ for _ in teams]
	tabulation = tabulate(table, headers, tablefmt="fancy_grid")

	difference = {}

	for itm in whole_space:
		if itm not in loser_files:
			if itm in difference:
				difference[itm][0] = 'loser'
			else:
				difference[itm] = ['loser', '']
		if itm not in tie_files:
			if itm in difference:
				difference[itm][1] = 'tie'
			else:
				difference[itm] = ['', 'tie']

	return difference

def main():
	team = None
	if len(sys.argv) == 2:
		team = sys.argv[1]

	dct = get_done()
	keys = sorted(dct.keys())

	for itm in keys:
		if team:
			if itm.split('_')[0] == team:
				print itm + (' ' * (PADDING - len(itm))) + '\t' + dct[itm][0] + '\t' + dct[itm][1]
		else:
			print itm + (' ' * (PADDING - len(itm))) + '\t' + dct[itm][0] + '\t' + dct[itm][1]

if __name__ == '__main__':
	main()