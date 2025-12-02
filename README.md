# learn-llm

M1 Pro (Apple Silicon) 환경에 최적화된 LLM 및 CV 학습용 샌드박스입니다.  
Miniforge(Mamba)를 사용하여 PyTorch(MPS)와 TensorFlow(Metal) 하이브리드 환경을 코드로 관리합니다.

## 1\. Prerequisites

### System Requirements

- **OS:** macOS (Apple Silicon M1/M2/M3)
- **Package Manager:** Homebrew

### Install Miniforge

Anaconda 대신 경량화된 Miniforge(Mamba 포함)를 사용합니다.

```bash
brew install miniforge
conda init zsh
source ~/.zshrc
```

---

## 2\. Environment Setup (IaC)

본 프로젝트는 `environment.yml`을 **Single Source of Truth**로 관리합니다.

### Initialization & Update (Idempotent)

환경 생성 및 변경 사항 반영은 아래 명령어로 수행합니다. (`--prune` 옵션으로 미사용 패키지 자동 삭제)

```bash
mamba env create -f environment.yml

# base 환경에서 실행 권장
conda deactivate
mamba env update --file environment.yml --prune
```

---

### 가상환경 활성화

```bash
conda activate learn-llm
python -m ipykernel install --user --name=learn-llm --display-name "Python (learn-llm)"
```

## 3. JupyterLab

환경 활성화 후 주피터랩을 실행합니다.

```bash
conda activate learn-llm
jupyter lab
```
