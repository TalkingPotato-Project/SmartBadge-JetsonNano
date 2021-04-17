## Vim Command
### ※ upper case is shift + ( letter )
```
hjkl # 화살표 이동
w # 단어 단위로 넘김
W # 제일 마지막
shitf $ # End Key
shift ^ # Home Key
ctrl+f #: page down
ctrl+u / b # page up
cw # 한단어 수정
dw # 한단어 삭제
v # 블록
y # 복사
yy # 한라인 복사
p # 붙혀넣기
dd # 한라인 삭제
x # delete
X # backspace
u # ctrl + z
A # insert mode at line end
o # 다음줄에 입력모드
O # 윗줄 입력모드


( 명령모드 ':' )
:w # save
:q # quit
:q! # 저장하지 않고 quit
:set nu # line number
:set noun # rm line num
:라인번호 # 해당하는 라인으로 이동
:! # 커맨드 라인으로 이동
:!명령 # 커맨드라인에서 명령 수행
:HML - 화면의 제일 위H, 중간M, 아래L로 커서이동

:%s/<before>/<after>/g # 바꾸고싶은 단어  /g 전부 /ig 대소문자 구분 X

/검색어 # search
:n # 다음찾기
:N # 이전찾기
``` #
