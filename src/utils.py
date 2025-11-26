import nltk
import ssl

# [SSL 인증서 에러 방지용]
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


def download_nltk_data():
    nltk.download("averaged_perceptron_tagger_eng")
    nltk.download("punkt")
    nltk.download("punkt_tab")
    nltk.download("stopwords")
    nltk.download("wordnet")


# 실행
download_nltk_data()
