from typing import Dict

from runtime.checkpoint import Checkpoint


class CheckpointStore:

    def __init__(self):

        self.storage: Dict[str,Checkpoint] = {}

    def save(
        self,
        checkpoint: Checkpoint
    ):

        self.storage[
            checkpoint.workflow_id
        ] = checkpoint

    def load(
        self,
        workflow_id:str
    ):

        return self.storage.get(
            workflow_id
        )