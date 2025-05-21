from app import index

def test_index():
    assert index().lower() == "hello, world!".lower()  
    
