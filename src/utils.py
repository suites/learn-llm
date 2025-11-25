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
    # 'punkt_tab'이 추가되어야 최신 NLTK에서 에러가 안 납니다.
    required_packages = ['punkt', 'punkt_tab', 'stopwords', 'wordnet', 'averaged_perceptron_tagger']
    
    for pkg in required_packages:
        try:
            # 데이터가 있는지 확인
            nltk.data.find(f'tokenizers/{pkg}')
        except LookupError:
            print(f"📥 Downloading NLTK package: {pkg}")
            nltk.download(pkg, quiet=True)

# 실행
download_nltk_data()
