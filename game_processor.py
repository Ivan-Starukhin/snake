
from game_info import game_info
from game_info import point2d
import time

class game_processor: #подправлено для pygame
    def run(self, game, command):
        #print(f'command: {command}, direction: {game.snake.move_direction}')
    
        if (command == 'up' and game.snake.move_direction != 'down') or (game.snake.move_direction == 'up' and command == 'down'):
            if command == 'up' and game.snake.move_direction != 'down':
                game.snake.move_direction = command
            game.snake.location.insert(0, (game.snake.location[0] + point2d(0, 10)).rest(game.field_size))
            
        elif (command == 'down' and game.snake.move_direction != 'up') or (game.snake.move_direction == 'down' and command == 'up'):
            if command == 'down' and game.snake.move_direction != 'up':
                game.snake.move_direction = command
            game.snake.location.insert(0, (game.snake.location[0] + point2d(0, -10)).rest(game.field_size))

        elif (command == 'left' and game.snake.move_direction != 'right') or (game.snake.move_direction == 'left' and command == 'right'):
            if command == 'left' and game.snake.move_direction != 'right': 
                game.snake.move_direction = command
            game.snake.location.insert(0, (game.snake.location[0] + point2d(-10, 0)).rest(game.field_size))

        elif (command == 'right' and game.snake.move_direction != 'left') or (game.snake.move_direction == 'right' and command == 'left'):
            if command == 'right' and game.snake.move_direction != 'left': 
                game.snake.move_direction = command
            game.snake.location.insert(0, (game.snake.location[0] + point2d(10, 0)).rest(game.field_size))

        game.snake.head = game.snake.location[0]
        game.snake.tail = game.snake.location[-2]
        
        if game.snake.location[0]  in game.food:
            game.food.remove(game.snake.location[0] )            
            return game
        
        if game.snake.head in game.snake.location[1:]:
            game.is_valid = False
            time.sleep(0.5)
        
        if game.snake.head in game.barriers:
            game.is_valid = False
            time.sleep(0.5)
            
        game.snake.location = game.snake.location[:-1]
    
        return game