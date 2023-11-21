from multiprocessing import Process
import MyDatabaseWrapper
import MyLogger
import time
import sys


class APIProcessor:
    def __init__(self, database_wrapper: MyDatabaseWrapper, logger: MyLogger):
        self.database_wrapper = database_wrapper
        self.logger = logger

    def process(self, id: list) -> list:
        db_call_process = Process(target=self.insert_data, args=(id,), daemon=True)
        db_call_process.start()

        # Further code which processes the request.

    def insert_data(self, id: list) -> bool:
        for i in id:
            self.logger.info("Processing request for id: %s", i)
            self.database_wrapper.insert(i)
            time.sleep(1)
        return True


if __name__ == "__main__":
    args = sys.argv[1:]  # assuming the ids are passed as command line arguments
    my_processor = APIProcessor(MyDatabaseWrapper(), MyLogger())
    proc = Process(target=my_processor.process, args=(args,))
    proc.start()
