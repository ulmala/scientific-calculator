import queue


class OutputQueue:
    """
    Output queue used in Shunting Yard algorithm
    """
    def __init__(self) -> None:
        """
        Class constructor
        """
        self._queue = queue.Queue()

    def __str__(self) -> str:
        """
        Returns the queue as string

        Returns:
            str: queue
        """
        return str(list(self._queue.queue))

    def put(
            self,
            token: str
    ):
        """
        Puts token into the queue

        Args:
            token (str): token
        """
        self._queue.put(token)

    def get(self) -> str:
        """
        Returns token from the queue

        Returns:
            str: token
        """
        return self._queue.get()

    def as_list(self) -> list:
        """
        Returns the queue as list

        Returns:
            list: queue
        """
        return list(self._queue.queue)
