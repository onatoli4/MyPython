# -*- coding: utf-8 -*-

"""
Задание 23.3a

В этом задании надо сделать так, чтобы экземпляры класса Topology
были итерируемыми объектами.
Основу класса Topology можно взять из любого задания 22.1x или задания 23.3.

После создания экземпляра класса, экземпляр должен работать как итерируемый объект.
На каждой итерации должен возвращаться кортеж, который описывает одно соединение.
Порядок вывода соединений может быть любым.


Пример работы класса:

In [1]: top = Topology(topology_example)

In [2]: for link in top:
   ...:     print(link)
   ...:
(('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
(('R2', 'Eth0/0'), ('SW1', 'Eth0/2'))
(('R2', 'Eth0/1'), ('SW2', 'Eth0/11'))
(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
(('R3', 'Eth0/2'), ('R5', 'Eth0/0'))


Проверить работу класса.
"""

topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)
        
    def _normalize(self, topology_dict):
        return {min(local,remote): max(local,remote)
                for local,remote in topology_dict.items()}
    
    def delete_link(self, local, remote):
        if self.topology.get(local) == remote:
            del self.topology[local]
        elif self.topology.get(remote) == local:
            del self.topology[remote]
        else:
            print("Такого соединения нет")
    
    def delete_node(self, device):
        orig_size = len(self.topology)
        for src,dst in list(self.topology.items()):
            if device in src or device in dst:
                del self.topology[src]
        if orig_size == len(self.topology):
            print("Такого устройства нет")

    def add_link(self, local, remote):
        keys_and_values = set(self.topology.keys()) | set(self.topology.values())
        if self.topology.get(local) == remote or self.topology.get(remote) == local:
            print("Такое соединение существует")
        elif local in keys_and_values or remote in keys_and_values:
            print("Соединение с одним из портов существует")
        else:
            self.topology[local] = remote           

    def __add__(self, other):
        orig = self.topology.copy()
        orig.update(other.topology)
        return Topology(orig)

    def __iter__(self):
        return iter(self.topology.items())


if __name__ == "__main__":
    t1 = Topology(topology_example)
    for link in t1:
        print(link)