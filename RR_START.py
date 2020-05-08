import numpy as np
from multiprocessing import shared_memory

existing_shm = shared_memory.SharedMemory(name='R3E')
