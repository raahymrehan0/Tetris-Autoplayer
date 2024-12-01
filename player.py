from board import Direction, Rotation, Action, NoBlockException, Shape, Board
from random import Random
import time

class Player:
        
    def __init__(self):
            pass
    
    def choose_action(self, board):
        try:
            self.hello = board.score
            min_score = float('inf')
            best_action = []
            # First 40 permutations (only pieces)
            for rotations in range(4):
                sandbox = board.clone()
                rotation_actions = [Rotation.Clockwise] * rotations
                for _ in range(rotations):
                    sandbox.rotate(Rotation.Clockwise)
                for x_offset in range(-5, 5):
                    temp_sandbox = sandbox.clone()
                    move_actions = []
                    for _ in range(abs(x_offset)):
                        direction = Direction.Left if x_offset < 0 else Direction.Right
                        temp_sandbox.move(direction)
                        move_actions.append(direction)
                    temp_sandbox.move(Direction.Drop)
                    first_actions = rotation_actions + move_actions + [Direction.Drop]

                    # Second 40 permutations (only pieces)
                    for rotations_2 in range(4):
                        sandbox_2 = temp_sandbox.clone()
                        for _ in range(rotations_2):
                            sandbox_2.rotate(Rotation.Clockwise)
                        for x_offset_2 in range(-5, 5):
                            temp_sandbox_2 = sandbox_2.clone()
                            move_actions_2 = []

                            for _ in range(abs(x_offset_2)):
                                direction = Direction.Left if x_offset_2 < 0 else Direction.Right
                                temp_sandbox_2.move(direction)
                                move_actions_2.append(direction)
                            temp_sandbox_2.move(Direction.Drop)
                            score = self.calculate_score(temp_sandbox_2)
                            if temp_sandbox_2.score - temp_sandbox.score > 1600 or temp_sandbox_2.score - temp_sandbox.score > 1600:
                                score -= 1600
                            elif temp_sandbox_2.score - temp_sandbox.score > 400 or temp_sandbox_2.score - temp_sandbox.score > 400:
                                score -= 800
                            if score < min_score:
                                min_score = score
                                best_action = first_actions  
        
            return best_action if best_action else Direction.Drop
        except NoBlockException:
            return best_action if best_action else Direction.Down

    def calculate_score(self, boards):
        return 10 * self.calculate_holes(boards) + 3 * self.calculate_max_height(boards) + 4 * self.calculate_bumpiness(boards) - 1000 * self.calculate_empty_columns(boards) + self.calculate_complete_lines(boards)

    def calculate_complete_lines(self, board):
        if board.score - self.hello > 1600:
            return -1000
        elif board.score - self.hello > 400:
            return -800
        else:
            return 80

    
    def calculate_holes(self, boards):
        holes = 0
        for x in range(boards.width):
            for y in range(boards.height):
                if (x, y) not in boards.cells:
                    if (x, y - 1) in boards.cells:
                        holes += 1
        return holes
    
    def calculate_bumpiness(self, board):
        bumpiness = 0
        for x in range(board.width-1):
            for y in range(board.height):
                if (x, y) not in board.cells:
                    if (x + 1, y) in board.cells or (x + 1, y -1) in board.cells:
                        bumpiness += 1
                    if (x - 1, y) in board.cells or (x - 1, y -1) in board.cells:
                        bumpiness += 1
        return bumpiness
    
    def calculate_empty_columns(self, board):
        empty_columns = 0
        for x in range(board.width):
            for y in range(board.height):
                if (x, y) in board.cells:
                    break
                empty_columns += 1
        return empty_columns if empty_columns == 1 else -100
    
    
    def calculate_max_height(self, board):
        height = 0
        for y in range(board.height):
            for x in range(board.width):
                if (x, y) in board.cells:
                    current_height = board.height - y
                    height += current_height
        return height

SelectedPlayer = Player

