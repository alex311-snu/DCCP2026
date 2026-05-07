def trace(n: int) -> int:
    print(f"호출: trace({n})")
    if n <= 1:
        print(f" 기저: return 1")
        return 1
    result: int = n + trace(n - 2)
    print(f" 반환: trace({n}) = {result}")
    return result

trace(5)