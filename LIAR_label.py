!wget -q https://www.cs.ucsb.edu/~william/data/liar_dataset.zip -O liar_dataset.zip
!unzip -q -o liar_dataset.zip

import pandas as pd, os, collections

colnames = [
    "id", "label", "statement", "subject", "speaker", "job_title",
    "state_info", "party_affiliation",
    "barely_true_counts", "false_counts", "half_true_counts",
    "mostly_true_counts", "pants_on_fire_counts",
    "context"
]

train_df = pd.read_csv("train.tsv", sep="\t", header=None, names=colnames, quoting=3)
valid_df = pd.read_csv("valid.tsv", sep="\t", header=None, names=colnames, quoting=3)
test_df  = pd.read_csv("test.tsv",  sep="\t", header=None, names=colnames, quoting=3)

false_set = {"pants-fire", "false", "barely-true"}
true_set  = {"half-true", "mostly-true", "true"}

def to_binary(df):
    df["label_norm"] = df["label"].astype(str).str.strip().str.lower()
    df["labels"] = df["label_norm"].apply(lambda s: 1 if s in true_set else 0)  # 1=true, 0=false
    ### keep only statement + labels
    return df[["statement", "labels"]]

train_df_b = to_binary(train_df)
valid_df_b = to_binary(valid_df)
test_df_b  = to_binary(test_df)

def stats(df, name):
    cnt = dict(collections.Counter(df["labels"].astype(int).tolist()))
    print(f"{name:5s} | n={len(df):4d} | class balance (0/1) = {cnt}")

stats(train_df_b, "train")
stats(valid_df_b, "valid")
stats(test_df_b,  "test")

#see 3 example（statement + labels）
train_df_b.head(3)
