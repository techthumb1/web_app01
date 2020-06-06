

import basilica
with basilica.Connection('579a7484-3ec5-33f4-cd05-f72712c2590e') as c:
    print(type(connection))
    sentences = ['Hello World!', 'How are you?']
    embeddings = connection.embed_sentences(sentences)
    print(list(embeddings))
