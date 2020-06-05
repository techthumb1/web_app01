

import basilica
with basilica.Connection('579a7484-3ec5-33f4-cd05-f72712c2590e') as c:
    embeddings = c.embed_sentences(["Hello world!", "How are you?"])
    print(list(embeddings))
