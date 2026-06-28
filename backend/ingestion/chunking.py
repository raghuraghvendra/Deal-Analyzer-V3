from langchain_text_splitters import RecursiveCharacterTextSplitter


class Chunker:

    def __init__(self):

        self.child_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
    ]
)

    def create_child_chunks(self, text: str):

        chunks = self.child_splitter.split_text(text)

        return chunks