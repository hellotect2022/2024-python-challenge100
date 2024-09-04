import logging
# 색상을 적용한 로그 출력 형식 설정
color_log_format = "\033[1;32m%(levelname)s\033[1;0m: %(message)s"
logging.basicConfig(level=logging.DEBUG,format=color_log_format)
logging.debug("이것은 디버그 메세지 입니다.")
logging.info("이것은 정보 메시지입니다.")
logging.warning("이것은 경고 메시지입니다.")
logging.error("이것은 에러 메시지입니다.")
logging.critical("이것은 심각한 에러 메시지입니다.")

list  = [1,2,3,4]
print(list.pop())
list.insert(0,4)
print(list)