import queue


class OutputQueue:
    def __init__(self) -> None:
        self._queue = queue.Queue()

    def __str__(self) -> str:
        return str(list(self._queue.queue))
    
    def put(
            self,
            token: str
    ):
        self._queue.put(token)