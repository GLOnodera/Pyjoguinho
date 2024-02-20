import time
from util import Mapa

class Control(Mapa):
    def __init__(self):
        super().__init__()

        # maquina de estados
        self.robot_state = 'stop'
        self.state_machine = {
            'forward': self.forward,
            'left': self.left,
            'right': self.right,
            'stop': self.stop,
        }
    
    def forward(self) -> None:
        new_position = (self.posicao[0] - 1, self.posicao[1])  # Move subtraindo 1 da linha
        self.atualizar_posicao(new_position)
        self.mostrar()
        if new_position[0] == 0:
            self.robot_state = 'stop'

    def left(self) -> None:
        new_position = (self.posicao[0], self.posicao[1] - 1)  # Move subtraindo 1 da coluna
        self.atualizar_posicao(new_position)
        self.mostrar()

    def right(self) -> None:
        new_position = (self.posicao[0], self.posicao[1] + 1)  # Move somando 1 à coluna
        self.atualizar_posicao(new_position)
        self.mostrar()
    
    def stop(self) -> None:
        pass

    def control(self) -> None:
        if self.robot_state == 'stop':
            return

        if self.posicao[0] > 0 and self.grade[self.posicao[0] - 1, self.posicao[1]] == 0:
            self.robot_state = 'forward'
        elif self.posicao[1] > 0 and self.grade[self.posicao[0], self.posicao[1] - 1] == 0:
            self.robot_state = 'left'
        elif self.posicao[1] < self.colunas - 1 and self.grade[self.posicao[0], self.posicao[1] + 1] == 0:
            self.robot_state = 'right'
        else:
            self.robot_state = 'stop'

        self.state_machine[self.robot_state]()

def main():
    control = Control()
    control.mostrar()

    i = 40
    
    while not control.robot_state == 'stop' and i > 0:
        control.control()
        time.sleep(1)
        i -= 1

if __name__=="__main__":
    main()
