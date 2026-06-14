def rotate_and_concat(str, n):
    if n > len(str):
        return

    head_flipped = str[:n][::-1]
    head_remaining = str[n:]
    head_result = head_flipped + head_remaining

    tail_flipped = str[-n:][::-1]
    tail_remaining = str[:-n]
    tail_result = tail_flipped + tail_remaining
    
    print(head_result)
    print(tail_result) 

rotate_and_concat('ruomei', 10)