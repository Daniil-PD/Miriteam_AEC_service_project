import re

from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,

    Doc
)
from sentence_transformers import SentenceTransformer

from .models import Information

segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)

wrong_poses = ['INTJ', 'PUNCT']

sentence_transformer = SentenceTransformer('distiluse-base-multilingual-cased')

def text2doc(text: str):
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    for token in doc.tokens:
        if token.pos not in wrong_poses:
            token.lemmatize(morph_vocab)
    return doc


def encode_text(text):
    """Кодируем текст"""
    sub_texts = re.split(r'\n+', text)
    for stext in sub_texts:
        doc = text2doc(stext)
        for i in range(1, len(doc.sents), 5):
            lemma_text = '. '.join([sen.text for sen in doc.sents[i-1:i+5]])
            lemma_text_vector = sentence_transformer.encode(lemma_text)
            text_inf = Information(text=lemma_text, vector=lemma_text_vector.tolist())
            text_inf.save()

