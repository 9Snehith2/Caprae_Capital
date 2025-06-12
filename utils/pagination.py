def paginate(data, page, size):
    start = page * size
    end = start + size
    return data[start:end], start
