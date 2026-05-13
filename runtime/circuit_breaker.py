import time

class CircuitBreaker:

    def __init__(
        self,
        failure_threshold=3,
        recovery_time=30
    ):

        self.failure_count = 0

        self.failure_threshold = (
            failure_threshold
        )

        self.recovery_time = (
            recovery_time
        )

        self.last_failure_time = None

    def can_execute(self):

        if (
            self.failure_count
            < self.failure_threshold
        ):

            return True

        if (
            time.time()
            - self.last_failure_time
            > self.recovery_time
        ):

            self.failure_count = 0

            return True

        return False

    def record_failure(self):

        self.failure_count += 1

        self.last_failure_time = (
            time.time()
        )