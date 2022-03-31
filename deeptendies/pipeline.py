

class Pipeline:
    def __init__(self, pipeline, **kwargs):
        self.pipeline = pipeline
        self.__dict__.update(kwargs)
        pass

    def run(self, df, **kwargs):
        for p in self.pipeline:
            df = p(df, **kwargs)
        return df
