# WARTANKER

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
>>> crypto.b16encode('flag{wartanker}', 'UTF_8')
'666C61677B77617274616E6B65727D'
```

### `wartanker.crypto.b16decode`

```python
>>> crypto.b16decode('666C61677B77617274616E6B65727D')
'flag{wartanker}'
```

### `wartanker.crypto.b32encode`

```python
>>> crypto.b32encode('flag{wartanker}')
'MZWGCZ33O5QXE5DBNZVWK4T5'
>>> crypto.b32encode('flag{wartanker}', 'UTF_8')
'MZWGCZ33O5QXE5DBNZVWK4T5'
```

### `wartanker.crypto.b32decode`

```python
>>> crypto.b32decode('MZWGCZ33O5QXE5DBNZVWK4T5')
'flag{wartanker}'
```

### `wartanker.crypto.b64encode`

```python
>>> crypto.b64encode('flag{wartanker}')
'ZmxhZ3t3YXJ0YW5rZXJ9'
>>> crypto.b64encode('flag{wartanker}', 'UTF_8')
'ZmxhZ3t3YXJ0YW5rZXJ9'
```

### `wartanker.crypto.b64decode`

```python
>>> crypto.b64decode('ZmxhZ3t3YXJ0YW5rZXJ9')
'flag{wartanker}'
```

### `wartanker.crypto.base_encode`

### `wartanker.crypto.base_decode`

### `wartanker.crypto.str2hex`

### `wartanker.crypto.hex2str`

<!-- wartanker.forensic -->
## `wartanker.forensic`
```python
>>> from wartanker import crypto
[*] Wartanker, the Python3 toolkit for solving CTF problems
```

### `wartanker.forensic.get_fileinfo`

```python
>>> from wartanker import forensic
[*] Wartanker, the Python3 toolkit for solving CTF problems
>>> forensic.get_fileinfo('./examples/dump')
'./examples/dump: ASCII text'
```

### `wartanker.forensic.find_flag`

```python
>>> from wartanker import forensic
[*] Wartanker, the Python3 toolkit for solving CTF problems
>>> forensic.find_flag('W4RT4NK3R', './examples/dump')
['W4RT4NK3R{fake}', 'W4RT4NK3R{real_flag}']
```

<!-- wartanker.hash -->
## `wartanker.hash`

### `wartanker.hash.sha256encode`

### `wartanker.hash.sha384encode`

### `wartanker.hash.sha512encode`

### `wartanker.hash.sha_encode`

### `wartanker.hash.md5encode`

<!-- wartanker.pwnable -->
## `wartanker.pwnable`

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
