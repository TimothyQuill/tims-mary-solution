from generate import DataGenerator

generator = DataGenerator("data/document_ocr.txt", model="gpt")
generator.generate()
