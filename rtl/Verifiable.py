class Verifiable:
    @classmethod
    def verify(cls) -> bool:
        raise NotImplementedError

    @staticmethod
    def main(cls) -> None:
        raise NotImplementedError
