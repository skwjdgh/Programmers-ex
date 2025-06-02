<p align>
  <img src = "https://capsule-render.vercel.app/api?type=blur&height=200&color=gradient&text=Coding%20Ex&descAlign=59&section=header">

이 저장소는 [프로그래머스(programmers.co.kr)](https://programmers.co.kr)에서 제공하는 코딩 문제들의 풀이 예제를 모아둔 공간입니다.
문제 해결 능력 향상과 알고리즘 학습을 위해 다양한 언어로 구현된 예제들을 제공합니다.

디렉토리 구조

```
Programmers-ex/
├── Python3/
│   └── 프로그래머스/
│       └── [문제별 폴더]/
│           └── [문제풀이 파일].py
├── C/
│   └── [문제별 폴더]/
│       └── [문제풀이 파일].c
└── README.md
```

- `Python3/`: Python 3로 작성된 문제 풀이 코드가 위치합니다.
- `C/`: C 언어로 작성된 문제 풀이 코드가 위치합니다.
- `[문제별 폴더]`: 각 문제에 대한 고유 폴더로, 문제 제목이나 번호로 명명됩니다.

사용 방법

1. 저장소를 클론합니다:
   ```bash
   git clone https://github.com/skwjdgh/Programmers-ex.git
   ```
2. 원하는 언어 디렉토리로 이동합니다:
   ```bash
   cd Programmers-ex/Python3/프로그래머스
   ```
3. 문제별 폴더로 이동하여 코드를 확인하거나 실행합니다.

문제 풀이 예시

각 문제 폴더에는 해당 문제의 설명과 함께 풀이 코드가 포함되어 있습니다.
예를 들어, `Python3/프로그래머스/문제1/solution.py` 파일에는 다음과 같은 구조로 작성되어 있습니다:

```python
def solution(param1, param2):
    # 문제 해결 로직
    return result
```

또한, 각 코드 파일에는 문제에 대한 간단한 설명과 접근 방법이 주석으로 포함되어 있어 학습에 도움이 됩니다.

기여 방법

이 저장소는 오픈 소스로, 누구나 기여하실 수 있습니다. 기여를 원하신다면 다음 절차를 따라주세요:

1. 저장소를 포크합니다.
2. 새로운 브랜치를 생성합니다:
   ```bash
   git checkout -b feature/문제이름
   ```
3. 문제 풀이 코드를 추가하거나 수정합니다.
4. 변경 사항을 커밋합니다:
   ```bash
   git commit -m "Add solution for 문제이름"
   ```
5. 브랜치를 푸시합니다:
   ```bash
   git push origin feature/문제이름
   ```
6. Pull Request를 생성하여 변경 사항을 제출합니다.

라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참고해주세요.
