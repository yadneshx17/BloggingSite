from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_getBlogs():
    res = client.get("/blogs/1")
    assert res.status_code == 200

def test_getBlog():
    res = client.get("/blogs/1")
    assert res.status_code == 200

def test_createBlog():
    res = client.post("/blogs/", json={'title': 'Test Blog', 'content': 'Content of the test blog', 'published': 'True'})
    assert res.status_code == 200  

def test_deleteBlog():
    res = client.post("/blogs/7")
    assert res.status_code == 200

def test_updateBlog():
    res = client.put("/blogs/6", json={'title':'Updated title', 'content':'Updated content of the blog'})
    assert res.status_code == 200