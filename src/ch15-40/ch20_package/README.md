### pyinstaller 사용방법

```bash
pyinstaller --onefile example.py
pyinstaller --onefile --icon=icon.ico example.py
pyinstaller --onefile --noconsole example.py
pyinstaller --onefile --debug=all example.py
```

- <code>--onefile</code>: 하나의 실행 파일로 패키징합니다.
- <code>--icon</code>: 실행 파일에 아이콘을 설정
- <code>--noconsole</code>: 콘솔 창 숨기기
- <code>--debug</code>: 디버그 모드로 실행
