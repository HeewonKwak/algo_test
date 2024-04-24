# README 작성 관련 변수 정보 저장
MD_NAME = "README.md"
MD_HEADER = {
    "programmers": "Programmers 문제 풀이 내역"
}
CONCAT_MD_HEADER = """\
# Problem Solving
- 알고리즘 풀이 내역을 정리합니다.
- 풀이 내역은 업로드 시, [자동으로 업데이트](https://github.com/HeewonKwak/Algorithm)됩니다.
- 스스로 풀이에 성공한 경우 ✔️를, 다른 사람의 풀이를 참고해서 풀었으면 ❌로 표시했습니다.
### 사이트 별 문제 확인
"""
MD_TABLE = """\
| \# | Date | Problem | Solution | Difficulty | Solved |
| :----: | :------: | :---------------: | :-----: | :------: | :-------: |\
"""
MD_DIFFICULTY = {
    # Programmers
    "LV1": "⭐☆☆☆☆",
    "LV2": "⭐⭐☆☆☆",
    "LV3": "⭐⭐⭐☆☆",
    "LV4": "⭐⭐⭐⭐☆",
    "LV5": "⭐⭐⭐⭐⭐",
}
# 파일명 사용 불가로 사용할 수 없는 문자들
MD_S_CHARS = {
    "＼": "\\",
    "／": "/",
    "：": ":",
    "＊": "*",
    "？": "?",
    "＂": '"',
    "＜": "<",
    "＞": ">",
    "｜": "|"
}