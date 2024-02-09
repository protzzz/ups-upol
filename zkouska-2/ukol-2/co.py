"""
Jednoduchá knihovna na paralelní výpočty.


co_call(function1, ..., functionN)

    Paralelně zavolá funkce <function1>, ..., <functionN> bez argumentů.

    Tělo každé z uvedených funkcí se vykonává v samostatném procesu.

    Čeká, než volání funkcí skončí.



co_for(function, iterable)

    Zavolá paralelně funkci <function> na každou hodnotu
    iterovatelné hodnoty <iterable>.

    Čeká, až všechna volání skončí.

random_sleep(duration=0.01)

    Čeká náhodný čas. Nevíše <duration> sekund.


safe_print(value1, ..., valueN)

    Vytiskne hodnoty <value1>, ..., <valueN>.

    Nutno použít místo print při tisku v paralelním programu.


make_lock()

    Vytvoří zámek.

    Použití:

    lock = make_lock()
    with lock:
        <block>

Třída Semaphore:

    Instance jsou semafory.

    Semaphore(value) vytvoří instanci semaforu s hodnotou <value>.

    semaphore.acquire()
        Sníží hodnotu semaforu o jedna. Případně čeká, až to bude možné.

    semaphore.relase()
        Zvýší hodnotou semaforu o jedna.
      
    
    
Třída Queue:

   Instance je fronta.

   queue.put(item) => None
       Vloží hodnotu <item> nakonec fronty.

   queue.get() => value
       Odebere a vrátí prvek ze začátku fronty. Případně čeká, až je to možné.
   

"""

import threading as _threading
import time as _time
import random as _random
import queue as _queue 
Queue = _queue.Queue
QueueEmpty = _queue.Empty

def start_process(function, *args):
    process =_threading.Thread(target=function, args=args)
    process.start()
    return process

def join_process(process):
    process.join()
    
def co_call(*functions):
    """Paralelně zavolá funkce <functions> bez argumentů."""
    processes = list(map(start_process, functions))
    for process in processes:
        process.join()

def co_for(function, iterable):
    """Paralelně zavolá funkci <function> na každý prvek <iterable>."""
    processes = list(map(lambda el: start_process(function, el), iterable))
    for process in processes:
        process.join()
        
def random_sleep(duration=0.01):
    """Čeká náhodný čas. Nevíše <duration> sekund."""
    _time.sleep(_random.random() * duration)

def make_lock():
    """Vytvoří zámek."""
    return _threading.Lock()

_print_lock = make_lock()

def safe_print(*values):
    """Vytiskne hodnoty <values>. Lze použít i ve vláknech."""
    with _print_lock:
        print(*values)
    
Semaphore = _threading.Semaphore


