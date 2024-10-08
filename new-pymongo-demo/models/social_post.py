class SocialPost:
    def __init__(self, source, content, metadata):
        self.source = source
        self.content = content
        self.metadata = metadata

    def to_dict(self):
        return {
            'source': self.source,
            'content': self.content,
            'metadata': self.metadata
        }
