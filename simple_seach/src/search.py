from pathlib import Path
from re import search


class Serach:
    def __init__(self,document_path):
        self.data = self.crawl(document_path)
        self.index = self.indexing(self.data)
        

    def crawl(self,document_path):
        data ={}
        for file_path in (Path(document_path).iterdir()):
            if file_path.suffix != '.txt':
                continue
            with open(file_path) as f:
                doc_name = file_path.stem.replace('_', ' ').title()
                data[doc_name] = f.read()
        return data
    def indexing(self,data):
        index = {}
        for doc_name, text in data.items():
            words = text.split()
            for word in words:
                word = word.lower()
                if word in index:
                    index[word].add(doc_name)
                else:
                    index[word] = {doc_name}
        return index
    def search(self,search_term):
        docs =[]
        tokens = search_term.split()
        for token in tokens:
            docs.extend(self.index.get(token, []))
        return docs
            
if __name__ == "__main__":
    search_instance = Serach('data/documents')
    while True:
        query = input("Enter search term (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        results = search_instance.search(query)
        if results:
            print("Documents found:", set(results))
        else:
            print("No documents found.")