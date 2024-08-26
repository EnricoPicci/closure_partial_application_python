from numpy import dot
from numpy.linalg import norm
from openai import OpenAI
import pandas as pd


def calculate_embedding(text: str, openai_client: OpenAI, embedding_model: str):
    emb = (
        openai_client.embeddings.create(input=[text], model=embedding_model)
        .data[0]
        .embedding
    )
    return emb


def calculate_cos_similarity(embedding_1: list[float], embedding_2: list[float]):
    return dot(embedding_1, embedding_2) / (norm(embedding_1) * norm(embedding_2))


def cos_similarity_between_texts(
    text_1: str, text_2: str, openai_client: OpenAI, embedding_model: str
):
    embedding_1 = calculate_embedding(text_1, openai_client, embedding_model)
    embedding_2 = calculate_embedding(text_2, openai_client, embedding_model)
    return calculate_cos_similarity(embedding_1, embedding_2)


def cos_similarity_between_texts_partial(openai_client: OpenAI):
    def inner(text_1: str, text_2: str, embedding_model: str):
        print(
            f"Calculating cosine similarity between {text_1} and {text_2} with {embedding_model}"
        )
        return cos_similarity_between_texts(
            text_1, text_2, openai_client, embedding_model
        )

    return inner


cos_sim_table = pd.DataFrame(
    {
        "Text_1": [
            "The cat is on the table",
            "The cat is on the table",
            "The cat is on the table",
            "The cat is on the table",
            "The cat is on the table",
            "The cat is on the table",
            "The cat is on the table",
            "The cat is on the table",
            "The cat is on the table",
        ],
        "Text_2": [
            "The cat is under the table",
            "A dog is in the kitchen",
            "Yesterday I did not sleep",
            "The cat is under the table",
            "A dog is in the kitchen",
            "Yesterday I did not sleep",
            "The cat is under the table",
            "A dog is in the kitchen",
            "Yesterday I did not sleep",
        ],
        "Embedding_Model": [
            "text-embedding-3-large",
            "text-embedding-3-large",
            "text-embedding-3-large",
            "text-embedding-3-small",
            "text-embedding-3-small",
            "text-embedding-3-small",
            "text-embedding-ada-002",
            "text-embedding-ada-002",
            "text-embedding-ada-002",
        ],
    }
)


def fill_cos_sim_table():
    openai_client = OpenAI()
    cos_sim_partial = cos_similarity_between_texts_partial(openai_client)
    cos_sim_table["Cosine_Similarity"] = cos_sim_table.apply(
        lambda row: cos_sim_partial(
            row["Text_1"], row["Text_2"], row["Embedding_Model"]
        ),
        axis=1,
    )
    print(cos_sim_table)


if __name__ == "__main__":
    fill_cos_sim_table()

# python -m partial_function_application.calculate_cosine_diff
