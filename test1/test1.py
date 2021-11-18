with open('test_r.txt', 'r') as a:
    content = a.read()
    with open('test_w.txt', 'w') as b:
        b.write(content)
