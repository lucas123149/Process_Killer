import psutil
import time


# Defina em segundos quanto tempo deseja que seja aguardado após
# executar o script, para que o processo seja morto!
QuandoExecutar = 10  # Em segundos
NomeProcesso = ['AnyDesk']  # Pode ser passado mais de um nome por vez
# Example: ['AnyDesk', 'Discord']


class Process():
    def __init__(self, processo_vivo):
        self.time_max = time.time() + QuandoExecutar
        self.processo_vivo = processo_vivo

    def timer(self):
        time_now = time.time()
        if time_now >= self.time_max:
            return True
        else:
            time.sleep(10)
            return False

    def kill_process(self):
        for proc in psutil.process_iter():
            # Será checado até que o nome escrito abaixo
            # tenha o mesmo nome do processo.
            if any(procstr in proc.name() for procstr in NomeProcesso):
                proc.kill()

    def run(self):
        if self.timer() is True:
            self.kill_process()
            self.processo_vivo = False
            return self.processo_vivo
        else:
            return True


if __name__ == "__main__":
    processo_vivo = True
    processo = Process(processo_vivo)
    while processo.processo_vivo is True:
        processo.run()
